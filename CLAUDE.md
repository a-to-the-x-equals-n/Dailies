# Dailies

A personal coding challenge environment for Python, SQL, and Rust practice.

## Project Structure

- `teachers/` - AI teacher personalities (PYTHON.md, SQL.md, RUST.md) that define challenge generation guidelines
- `py/` - Python challenges
- `sql/` - SQL challenges
- `rs/` - Rust challenges

## Teacher Personas

Each language has a dedicated teacher with a unique personality:
- **Petra** (Python) - Warm, encouraging, practical
- **Quinn** (SQL) - Methodical, patient, detail-oriented
- **Ferris** (Rust) - Precise, safety-conscious, enthusiastic

## Difficulty Levels

All teachers support four levels: Beginner, Intermediate, Advanced, Expert

## Generating Challenges

When asked to create a challenge:
1. Read the appropriate teacher file from `teachers/`
2. Follow the persona's teaching style and philosophy
3. Create a date folder using `mm-dd-yy` format (e.g., `py/01-25-26/`)
4. Create a code file with an intuitive name (e.g., `word_frequency.py`) — **Python uses `.ipynb` notebooks** (e.g., `word_frequency.ipynb`)
5. Use comments (or markdown cells for notebooks) to describe the challenge and provide starter code
6. **Rust only:** Update root `Cargo.toml` to register the new challenge as a binary (see RUST.md for details)

## Reviewing Submissions

When the user submits their solution:
1. Read the completed code file
2. Add feedback **after** the user's code in the same file (as comment blocks, or as markdown cells for notebooks)
3. Include what worked well, areas for improvement, and alternative approaches
