# Python Learning Workspace

Welcome to your personal Python learning repository! This project is designed to be a tidy home for your practice code, notes, and experiments while you study with ChatGPT (or any other resource). It contains a suggested folder structure, starter exercises, and lightweight tooling so you can stay organized as you learn.

## Repository structure

```
.
├── exercises/        # Guided practice problems grouped by topic
│   └── basics/       # Introductory exercises about syntax and data types
├── notes/            # Markdown notes, snippets, and links you want to remember
├── projects/         # Larger experiments or mini-projects you build along the way
├── tests/            # Automated tests to check your exercise solutions
├── hello.py          # A quick "Hello, Python" example you can modify freely
└── requirements.txt  # Optional dependencies for running tests or tooling
```

Feel free to expand or reorganize the folders as you discover what works best for your learning style. The goal is to make it easy to find what you built later.

## Getting started

1. **Create a virtual environment** (optional, but keeps dependencies isolated):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
   On Windows, use `.venv\Scripts\activate` instead of the `source` command.

2. **Install dependencies** (currently just `pytest` for running the included tests):
   ```bash
   pip install -r requirements.txt
   ```

3. **Pick an exercise** from `exercises/` and follow the instructions in its README file. Start with the basics folder to practice Python fundamentals.

4. **Run tests** whenever you want to check your progress:
   ```bash
   pytest
   ```

5. **Take notes** in the `notes/` folder and commit them regularly. Logging what you learned is a powerful way to reinforce new concepts.

6. **Explore projects** by creating new subfolders under `projects/` for experiments or mini apps. Document what you tried and what you learned.

## Working with ChatGPT's study mode

If you're using ChatGPT's study and learn features:

- Keep a running list of questions or prompts in `notes/questions.md` so you can revisit them later.
- Copy example code that you find helpful into the relevant exercise file, then explain it back to yourself in a note.
- Summarize each learning session in a dated Markdown file under `notes/sessions/` (a template is provided).

## Making the most of Git

Treat this repository like a learning journal:

- Create a branch for a topic or project if you want to explore without cluttering the main branch.
- Commit early and often with messages that describe what you practiced (e.g., `Add list comprehension exercises`).
- Use GitHub issues or TODO comments to track future topics you want to study.

## Next steps

- Complete the starter exercise in `exercises/basics/variables.py`.
- Add your own exercises or copy challenges you find online.
- Consider creating a `resources.md` note with links to tutorials, videos, or articles you enjoy.

Happy learning, and have fun exploring Python!
