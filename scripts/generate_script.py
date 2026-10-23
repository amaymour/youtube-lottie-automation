#!/usr/bin/env python3
import json, argparse
parser = argparse.ArgumentParser()
parser.add_argument("--prompt", required=True)
parser.add_argument("--output", default="script.json")
args = parser.parse_args()
script = {"prompt": args.prompt, "script": "Generated script"}
json.dump(script, open(args.output, "w"))
print(f"✓ Script saved to {args.output}")
