# Persistence of Memory

An open source system under MIT license for providing persistent memory to stateless AI sessions, ensuring continuity across interactions.

## Overview

This project addresses the stateless nature of AI conversations by using a version-controlled repository as a single source of truth. It builds on Phase 1 (static Markdown in SCM) and extends to structured files (Phase 2) and automated API/CLI tools (Phase 3).

## License

MIT - See [LICENSE](./LICENSE) for details.

## Phases

### Phase 1: MVP - Single Public Markdown File

- Core: A single  file as ground truth.
- Access: Public URL via SCM web UI (originally Fossil, now mirrored to GitHub).
- Usage: AIs fetch and internalize this file at the start of each session.
- Files: 

### Phase 2: Structured Repository with Automation

- Extension: Multiple Markdown files for projects (e.g., Q-series), blockers, architecture.
- Automation: Python script to update files, commit, and push changes.
- Usage: Run  to append updates.
- Files: Additional MD files in , 

### Phase 3: API and Full Automation

- Extension: REST API for reading/updating memory without manual commits.
- Tech: Flask-based API running on local server (e.g., HP t630).
- Usage: Deploy with , query via HTTP (e.g., GET /memory, POST /update).
- Integration: AIs can use web tools to interact; local automation for commits.
- Files: 

## Installation

1. Clone the repo: `git clone https://github.com/MJcar12/persistence-of-memory.git`
2. Install dependencies: `pip install -r requirements.txt` (Flask for Phase 3)
3. For Phase 3: Run `python api/app.py`

## Usage

- Phase 1: Fetch  from GitHub raw URL.
- Phase 2: Use  to automate updates.
- Phase 3: Start the API and use endpoints for dynamic access.

## Contributing

Fork, modify, PR. Follow non-negotiable rules from .

## Relation to Q-Series

This persistence layer supports the Q-series projects (voice-enabled inventory systems) by storing state, blockers, and architecture.

