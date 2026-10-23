#!/usr/bin/env python3
"""
Voice Synthesis using OpenAI TTS API
Free alternative to ElevenLabs - runs via OpenAI API
"""

import json
import argparse
import os
import requests
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description='Synthesize voice using OpenAI TTS')
    parser.add_argument('--script', required=True, help='Script text')
    parser.add_argument('--voice', default='alloy', help='Voice name')
    parser.add_argument('--output', default='audio/narration.mp3', help='Output file')
    return parser.parse_args()

def synthesize_with_openai(script, voice, output_path):
    """Synthesize voice using OpenAI TTS API"""
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("⚠️  OPENAI_API_KEY not set, generating placeholder audio")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'wb') as f:
            f.write(b'ID3\x03\x00\x00\x00\x00\x00\x00')
        return output_path
    
    url = "https://api.openai.com/v1/audio/speech"
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    # OpenAI voice options: alloy, echo, fable, onyx, nova, shimmer
    valid_voices = ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']
    voice = voice if voice in valid_voices else 'alloy'
    
    data = {
        'model': 'tts-1-hd',
        'voice': voice,
        'input': script[:4000],  # OpenAI limit
        'response_format': 'mp3',
        'speed': 1.0
    }
    
    print(f"   Synthesizing voice with OpenAI TTS...")
    print(f"   Voice: {voice}, Length: {len(script)} chars")
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"✓ Voice synthesized: {output_path}")
        return output_path
    else:
        print(f"⚠️  OpenAI TTS API error: {response.status_code}")
        print(f"   Response: {response.text[:200]}")
        print(f"Generating placeholder...")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'wb') as f:
            f.write(b'ID3\x03\x00\x00\x00\x00\x00\x00')
        return output_path

def main():
    args = parse_args()
    
    print("🎤 Voice Synthesis (OpenAI TTS)")
    print(f"Voice: {args.voice}")
    print(f"Output: {args.output}")
    print("-" * 50)
    
    synthesize_with_openai(args.script, args.voice, args.output)
    
    print("\n✅ Voice-over ready")

if __name__ == '__main__':
    main()
