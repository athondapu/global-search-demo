# Contributing

1. Create a branch from `main`.
2. Run `make check` (lint + tests) before opening a pull request.
3. Open a pull request and request a review from a lab tooling maintainer
   (Alex Chen or Jordan Lee).
4. Changes to `config/lab_env.yaml` also need a review from Ravi Menon (platform).

## Running tests

```bash
uv run pytest
```

## Release

Merges to `main` are picked up by the lab environment on the next cohort start.
