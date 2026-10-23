#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--video", required=True)
parser.add_argument("--title", required=True)
args = parser.parse_args()
print(f"✓ Ready to upload {args.video} as '{args.title}'")
