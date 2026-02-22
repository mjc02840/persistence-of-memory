#!/usr/bin/env python3
# scripts/update_memory.py - Append to file, git commit & push

import sys, os, subprocess, argparse

def run(cmd): subprocess.run(cmd, check=True, cwd=os.path.dirname(__file__)+"/..")

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Target file e.g. PROJECT_MEMORY.md")
parser.add_argument("section", help="Section heading")
parser.add_argument("content", help="Content to append")
args = parser.parse_args()

path = args.file
if not os.path.isabs(path): path = os.path.join(os.getcwd(), path)

os.makedirs(os.path.dirname(path), exist_ok=True)

with open(path, "a") as f:
    f.write(f"\n## {args.section}\n\n{args.content}\n")

run(["git", "add", path])
run(["git", "commit", "-m", f"Auto-update: {args.section} in {args.file}"])
run(["git", "push", "origin", "main"])
print("Update committed and pushed.")
