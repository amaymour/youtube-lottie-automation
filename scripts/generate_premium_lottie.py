#!/usr/bin/env python3
"""
Premium Lottie Generator Script for GitHub Actions
Generates high-quality animations for YouTube content
"""

import json
import argparse
import os
from pathlib import Path
import sys

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from premium_lottie_generator import generate_premium_animation, AnimationStyle

def parse_args():
    parser = argparse.ArgumentParser(description='Generate premium Lottie animations')
    parser.add_argument('--scenes', required=True, help='JSON string of scenes')
    parser.add_argument('--style', default='cinematic-premium', help='Animation style')
    parser.add_argument('--output', default='animations/', help='Output directory')
    return parser.parse_args()

def generate_scenes(scenes_data, style, output_dir):
    """Generate animations for each scene"""
    os.makedirs(output_dir, exist_ok=True)
    
    if isinstance(scenes_data, str):
        scenes_data = json.loads(scenes_data)
    
    animations = []
    
    for i, scene in enumerate(scenes_data):
        scene_type = scene.get('type', 'intro')
        content = scene.get('content', '')
        duration = scene.get('duration', 5.0)
        
        print(f"Generating premium animation {i+1}/{len(scenes_data)}: {scene_type}")
        
        animation = generate_premium_animation(
            scene_type=scene_type,
            content=content,
            style=style,
            duration=duration
        )
        
        # Save animation
        filename = f"scene_{i+1:02d}_{scene_type}.json"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(animation, f, indent=2)
        
        animations.append({
            'id': f'scene_{i+1}',
            'type': scene_type,
            'file': filename,
            'duration': duration
        })
        
        print(f"  ✓ Saved: {filename}")
    
    # Create manifest
    manifest = {
        'style': style,
        'total_scenes': len(scenes_data),
        'animations': animations,
        'metadata': {
            'fps': 60,
            'resolution': '1920x1080',
            'quality': 'premium'
        }
    }
    
    manifest_path = os.path.join(output_dir, 'manifest.json')
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\n✓ Generated {len(scenes_data)} premium animations")
    print(f"✓ Manifest saved to {manifest_path}")
    
    return manifest

def main():
    args = parse_args()
    
    print("🎬 Premium Lottie Animation Generator")
    print(f"Style: {args.style}")
    print(f"Output: {args.output}")
    print("-" * 50)
    
    manifest = generate_scenes(args.scenes, args.style, args.output)
    
    print("\n✅ Premium animations ready for video assembly")
    print(f"   Total scenes: {manifest['total_scenes']}")
    print(f"   Style: {manifest['style']}")
    print(f"   Quality: {manifest['metadata']['quality']}")

if __name__ == '__main__':
    main()
