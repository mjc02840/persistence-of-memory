#!/usr/bin/env python3
# api/app.py
# Phase 3: Flask API for reading/updating memory.

from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

REPO_PATH = os.path.dirname(os.path.dirname(__file__))

@app.route('/memory/<file_name>', methods=['GET'])
def get_memory(file_name):
    file_path = os.path.join(REPO_PATH, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return jsonify({'content': f.read()})
    return jsonify({'error': 'File not found'}), 404

@app.route('/update', methods=['POST'])
def update_memory():
    data = request.json
    file_name = data.get('file')
    section = data.get('section')
    content = data.get('content')
    
    file_path = os.path.join(REPO_PATH, file_name)
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(f'# {section}\n\n{content}\n')
    else:
        with open(file_path, 'a') as f:
            f.write(f'\n## {section}\n\n{content}\n')
    
    subprocess.run(['git', 'add', file_path], cwd=REPO_PATH, check=True)
    subprocess.run(['git', 'commit', '-m', f'API update to {file_name}'], cwd=REPO_PATH, check=True)
    subprocess.run(['git', 'push', 'origin', 'main'], cwd=REPO_PATH, check=True)
    
    return jsonify({'status': 'Updated'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
