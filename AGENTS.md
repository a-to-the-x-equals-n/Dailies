# Repository Guidelines

## Project Structure & Module Organization

- `teachers/` holds the persona guides (`PYTHON.md`, `SQL.md`, `RUST.md`) that define challenge format and tone.
- `py/`, `sql/`, `rs/` store generated challenges and solutions for each language.
- Repo docs live at the root (`README.md`, `CLAUDE.md`).

## Build, Test, and Development Commands

This repository is documentation-first and does not ship a build system.
- No build step is required; edit Markdown files directly.
- Suggested quick checks: `rg` to locate topics (`rg "window functions" sql/`) and `ls` to verify new files landed in the right folder.
If you add automation (e.g., a test runner), document the commands here and in `README.md`.

## Coding Style & Naming Conventions

- Use clear Markdown structure with headings and short paragraphs.
- Favor fenced code blocks with language tags (e.g., ```python, ```sql, ```rust).
- Keep filenames descriptive and scoped by language, e.g., `py/list_comprehensions_01.md`.
- Match the teacher persona guidance for tone, difficulty labels, and challenge format.

## Testing Guidelines

There is no automated test framework in this repo today.
- If you add runnable code or tests, keep them alongside the relevant language folder and document how to run them.
- Prefer lightweight, self-contained examples that can be reviewed without extra setup.

## Commit & Pull Request Guidelines

Recent commit history uses short, lowercase summaries (e.g., “added teacher personas”).
- Keep commit messages concise and action-oriented.
- PRs should include: a brief summary, any new challenge files listed, and screenshots only if visual docs change.

## Agent-Specific Instructions

When generating new challenges:
- Read the relevant persona file in `teachers/` first.
- Follow the persona’s difficulty scale and formatting.
- Save outputs to the matching language directory (`py/`, `sql/`, or `rs/`).
