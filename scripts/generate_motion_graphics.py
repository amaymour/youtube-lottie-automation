#!/usr/bin/env python3
"""
Motion Graphics Generator Script for GitHub Actions
Generates premium motion graphics for YouTube videos
"""

import json
import argparse
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from motion_graphics_engine import generate_motion_graphic, MotionGraphicType

def parse_args():
    parser = argparse.ArgumentParser(description='Generate premium motion graphics')
    parser.add_argument('--scenes', required=True, help='JSON scenes')
    parser.add_argument('--style', default='cinematic-premium', help='Animation style')
    parser.add_argument('--output', default='motion_graphics/', help='Output directory')
    return parser.parse_args()

def generate_scene_graphics(scenes_data, style, output_dir):
    """Generate motion graphics for scenes"""
    os.makedirs(output_dir, exist_ok=True)
    
    if isinstance(scenes_data, str):
        scenes_data = json.loads(scenes_data)
    
    graphics = []
    
    for i, scene in enumerate(scenes_data):
        scene_type = scene.get('type', 'slide_reveal')
        content = scene.get('content', '')
        duration = scene.get('duration', 3.0)
        
        # Map scene types to motion graphics
        motion_map = {
            'intro': 'logo_reveal',
            'outro': 'end_screen',
            'title': 'kinetic_typing',
            'transition': 'particle_burst',
            'lower_third': 'lower_third',
            'call_to_action': 'call_to_action',
            'default': 'slide_reveal'
        }
        
        motion_type = motion_map.get(scene_type, 'slide_reveal')
        
        print(f"Generating motion graphic {i+1}/{len(scenes_data)}: {motion_type}")
        
        graphic = generate_motion_graphic(
            motion_type=motion_type,
            content=content,
            style=style,
            duration=duration
        )
        
        # Save graphic
        filename = f"motion_{i+1:02d}_{motion_type}.json"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(graphic, f, indent=2)
        
        graphics.append({
            'id': f'motion_{i+1}',
            'type': motion_type,
            'file': filename,
            'duration': duration
        })
        
        print(f"  ✓ Saved: {filename}")
    
    # Create manifest
    manifest = {
        'style': style,
        'total_graphics': len(scenes_data),
        'graphics': graphics,
        'metadata': {
            'fps': 60,
            'resolution': '1920x1080',
            'quality': 'premium_motion_graphics'
        }
    }
    
    manifest_path = os.path.join(output_dir, 'manifest.json')
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\n✓ Generated {len(scenes_data)} premium motion graphics")
    
    return manifest

def main():
    args = parse_args()
    
    print("🎬 Premium Motion Graphics Generator")
    print(f"Style: {args.style}")
    print(f"Output: {args.output}")
    print("-" * 50)
    
    manifest = generate_scene_graphics(args.scenes, args.style, args.output)
    
    print("\n✅ Motion graphics ready for video assembly")
    print(f"   Total: {manifest['total_graphics']}")
    print(f"   Style: {manifest['style']}")

if __name__ == '__main__':
    main()
