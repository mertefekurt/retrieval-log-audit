# Retrieval Log Audit

Find retrieval logs with empty hits, weak scores, and missing source metadata. This repo keeps the work close to the terminal: clear input, predictable output, and no service to babysit.

## Project card

<img src="assets/readme-cover.svg" alt="Retrieval Log Audit cover" width="100%" />

| Detail | Value |
| --- | --- |
| Area | developer tools |
| Command | `retrieval-log-audit` |
| Example | `examples/sample.txt` |

## What would make me stop a review

| Stopper | Level | Why it matters |
| --- | --- | --- |
| `empty-retrieval` | high | retrieval returned no documents |
| `low-top-score` | medium | top retrieval score appears weak |
| `missing-source` | low | source metadata is missing |

## Run from a fresh clone

```bash
git clone https://github.com/mertefekurt/retrieval-log-audit.git
cd retrieval-log-audit
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
retrieval-log-audit examples/sample.txt
retrieval-log-audit examples/sample.txt --json
```
