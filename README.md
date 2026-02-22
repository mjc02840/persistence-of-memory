# Persistence of Memory

MIT-licensed system providing persistent memory for stateless AI sessions (e.g., Grok, Claude) via GitHub-hosted ground truth.

## Phases Included

- **Phase 1**: Single Markdown ground truth file ().
- **Phase 2**: Structured docs + Python automation script.
- **Phase 3**: Flask REST API for read/update with auto-git commit.

See [PROJECT_MEMORY.md](./PROJECT_MEMORY.md) for rules and usage.

Install: `pip install -r requirements.txt`
Run API: `python3 api/app.py`
Update via script: `python3 scripts/update_memory.py PROJECT_MEMORY.md "New Blocker" "Content here"`
