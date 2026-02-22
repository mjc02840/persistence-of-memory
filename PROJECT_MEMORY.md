# Project Persistent Memory – Ground Truth

## Version

Phase 1 MVP – created 2026,02,22,00,03,14  
Updated for GitHub: 2026,02,22

## Public URL

https://github.com/MJcar12/persistence-of-memory/blob/main/PROJECT_MEMORY.md  
(Raw: https://raw.githubusercontent.com/MJcar12/persistence-of-memory/main/PROJECT_MEMORY.md)

## Project Overview

Single source of truth for continuity across stateless AI sessions.

All AI assistants must read this file first in every new session via the public URL above. 

Treat this file as immutable ground truth unless updated via git commit.

## Non-Negotiable Rules

* Never contradict facts, decisions or rules stated here.
* Formal tone only. No banter, no repeated introductions.
* Automate all setup and file creation. Never require manual code pasting.
* Output complete, ready-to-use files. No brevity placeholders.
* Treat this file as ground truth unless explicitly updated via git commit.

## Key Project Facts

* Goal: Long-term memory persistence without provider-side state.
* Source of truth: Git repository on GitHub.
* Phase: Full implementation - Phases 1, 2, 3.
* Current directory isolation: docs/ for MD, scripts/ for automation, api/ for Phase 3.
* Public access: Must load without authentication.

## Usage Instructions for All AI Interfaces

1. Read this entire file first via its public GitHub raw URL.
2. Internalize every section before any response or action.
3. Reference sections by heading when relevant.
4. Confirm internalization when requested (e.g., summarize rules in one sentence).

## Key Decisions & Rationale

- Moved from Fossil to Git/GitHub for open source publication and easier collaboration.
- Automation via scripts and API to avoid manual intervention.

## Current Architecture Overview

- Static: Markdown files.
- Dynamic: Python CLI for updates, Flask API for access.

## Glossary & Terms

- Ground Truth: This repository.
- Q-Series: Related projects using this persistence (e.g., Q19 voice inventory).

## Open Questions / Blockers

(Commit updates here as needed.)

