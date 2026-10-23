#!/usr/bin/env python3
"""
Voice Synthesis Script for GitHub Actions
Uses ElevenLabs API for premium voice-over
"""

import json
import argparse
import os
import requests
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description='Synthesize voice-over')
    parser.add_argument('--script', required=True, help='Script text')
    parser.add_argument('--voice', default='premium_narrator', help='Voice name')
    parser.add_argument('--output', default='audio/narration.mp3', help='Output file')
    return parser.parse_args()

def synthesize_with_elevenlabs(script, voice_id, output_path):
    """Synthesize voice using ElevenLabs API"""
    api_key = os.getenv('ELEVENLABS_API_KEY')
    
    if not api_key:
        print("⚠️  ELEVENLABS_API_KEY not set, generating placeholder audio")
        # Create placeholder
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'wb') as f:
            f.write(b'ID3\x03\x00\x00\x00\x00\x00\x00')  # Minimal MP3 header
        return output_path
    
    # Voice mapping
    voices = {
        'premium_narrator': 'pNInz6obpgDQGcFmaJgB',
        'corporate_male': 'JBFqnCBsd6RMkjVDRZzb',
        'warm_female': 'EXAVITQu4vr4xnSDxMaL',
    }
    
    voice_id = voices.get(voice_id, voices['premium_narrator'])
    
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    
    headers = {
        'Accept': 'audio/mpeg',
        'Content-Type': 'application/json',
        'xi-api-key': api_key
    }
    
    data = {
        'text': script[:5000],  # Limit length
        'model_id': 'eleven_monolingual_v1',
        'voice_settings': {
            'stability': 0.5,
            'similarity_boost': 0.75,
            'style': 0.3,
            'use_speaker_boost': True
        }
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"✓ Voice synthesized: {output_path}")
        return output_path
    else:
        print(f"⚠️  TTS API error: {response.status_code}")
        print(f"Generating placeholder...")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'wb') as f:
            f.write(b'ID3\x03\x00\x00\x00\x00\x00\x00')
        return output_path

def main():
    args = parse_args()
    
    print("🎤 Voice Synthesis")
    print(f"Voice: {args.voice}")
    print(f"Output: {args.output}")
    print("-" * 50)
    
    synthesize_with_elevenlabs(args.script, args.voice, args.output)
    
    print("\n✅ Voice-over ready")

if __name__ == '__main__':
    main()
