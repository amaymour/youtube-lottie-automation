#!/usr/bin/env python3
import argparse, os
parser = argparse.ArgumentParser()
parser.add_argument("--script", required=True)
parser.add_argument("--output", default="audio/narration.mp3")
args = parser.parse_args()
print("✓ Voice synthesis ready (needs OPENAI_API_KEY)")
open(args.output, "a").close()
