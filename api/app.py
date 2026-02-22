#!/usr/bin/env python3
# api/app.py - Flask API for memory read/update + git auto-commit

from flask import Flask, request, jsonify
import os, subprocess

app = Flask(__name__)
BASE = os.path.dirname(os.path.dirname(__file__))

def git_run(cmd):
    subprocess.run(cmd, cwd=BASE, check=True)

@app.route('/memory/<path:file_name>', methods=['GET'])
def get_memory(file_name):
    path = os.path.join(BASE, file_name)
    if os.path.exists(path):
        with open(path) as f: return jsonify({"content": f.read()})
    return jsonify({"error": "Not found"}), 404

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    file_name = data.get("file")
    section = data.get("section")
    content = data.get("content")
    if not all([file_name, section, content]):
        return jsonify({"error": "Missing fields"}), 400

    path = os.path.join(BASE, file_name)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "a") as f:
        f.write(f"\n## {section}\n\n{content}\n")

    git_run(["git", "add", path])
    git_run(["git", "commit", "-m", f"API update: {section} in {file_name}"])
    git_run(["git", "push", "origin", "main"])

    return jsonify({"status": "Updated and pushed"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
