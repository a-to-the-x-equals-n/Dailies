# Dailies <!-- omit in toc -->

_I wanted to keep my programmer skills tuned post grad school, so I tried out a few websites--exercism, leetcode, etc.  Usually, I copy/paste the exercises into my own editing environment anyways, so I figured why not just use `Codex` or `Claude` to create a custom learning environment customized exactly to my preferences._

## Table of Contents <!-- omit in toc -->
- [Tour](#tour)
- [Start](#start)


## Tour

```
dailies/
├── teachers/       # AI teacher personalities for challenge generation
│   ├── PYTHON.md   # Petra - warm and practical
│   ├── SQL.md      # Quinn - methodical and patient
│   └── RUST.md     # Ferris - precise and safety-conscious
├── py/             # Python challenges
├── sql/            # SQL challenges
└── rs/             # Rust challenges
```

Each teacher personality defines four difficulty levels: Beginner, Intermediate, Advanced, and Expert.

## Start

Claude will read the appropriate teacher file from teachers/, adopt that persona, and generate a challenge following the format and guidelines defined there.

Just ask naturally. For example:

- "Give me a beginner Python challenge"
- "Create an intermediate SQL challenge"
- "I want an advanced Rust challenge"

Claude will read the appropriate teacher file from teachers/, adopt that persona, and generate a challenge following the format and guidelines defined there.

You could also be more specific:
- "Give me an intermediate Python challenge focused on list comprehensions"
- "Create a SQL challenge about window functions"

The challenges would be saved to the corresponding directory (`py/`, `sql/`, `rs/`) so you can work on them and keep a history.