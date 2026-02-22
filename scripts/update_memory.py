#!/usr/bin/env python3
# scripts/update_memory.py
# Phase 2: Automated script to update Markdown files, commit, and push.

import sys
import os
import subprocess
import argparse

def run_command(cmd):
    subprocess.run(cmd, check=True)

def main():
    parser = argparse.ArgumentParser(description='Update Persistence Memory')
    parser.add_argument('file', help='File to update (e.g., PROJECT_MEMORY.md)')
    parser.add_argument('section', help='Section heading to append under')
    parser.add_argument('content', help='Content to append')
    args = parser.parse_args()

    file_path = args.file if os.path.isabs(args.file) else os.path.join(os.getcwd(), args.file)
    
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(f'# {args.section}\n\n{args.content}\n')
    else:
        with open(file_path, 'a') as f:
            f.write(f'\n## {args.section}\n\n{args.content}\n')
    
    run_command(['git', 'add', file_path])
    run_command(['git', 'commit', '-m', f'Update {args.file} with {args.section}'])
    run_command(['git', 'push', 'origin', 'main'])

if __name__ == '__main__':
    main()
