# Lumen Lab Tools

Command-line tools and starter code for the **Lumen Labs Agent Engineering Training Program**.
Trainees use `lab` to set up their environment, check out a lab seat, and validate their work
before each session.

> All content in this repository is fictional and was created for a demo.

## Quick start

```bash
./setup.sh          # installs uv, pulls the lab container image, creates .venv
uv run lab doctor   # checks Docker, Python and your lab API token
uv run lab seat     # reserves a seat in the shared lab environment
```

## Sessions

| Session | Topic | Starter code |
|---|---|---|
| 1 | LLM fundamentals | — |
| 2 | Prompting and tool use | `examples/cadence_template.yaml` |
| 3 | RAG lab | `labs/session3_rag/` |
| 4 | MCP connectors | `labs/session4_mcp/` |
| 5 | Agents and evaluation | — |
| 6 | Capstone | — |

## Commands

| Command | What it does |
|---|---|
| `lab doctor` | Checks your machine is ready for the labs |
| `lab seat` | Reserves a seat in the shared lab environment for your cohort |
| `lab validate <file>` | Validates a cadence template before you submit it |
| `lab token` | Shows when your lab API token expires |

## Maintainers

Lab tooling is maintained by Alex Chen and Jordan Lee. See [CONTRIBUTING.md](CONTRIBUTING.md).
