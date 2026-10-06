# Lab environment architecture

- **Lab API** (`lab-api.lumen-labs.example`): issues lab API tokens and manages seats.
- **Seat pool:** 40 seats shared by all running cohorts (`config/lab_env.yaml`). A seat is
  held by one trainee for the lifetime of their cohort.
- **Lab image:** `ghcr.io/lumen-labs/lab-env`, currently built for amd64 only. On Apple
  Silicon it runs under emulation.
- **Tokens:** expire after 14 days; `lab doctor` and `lab token` warn before expiry.

Owners: Jordan Lee (lab infrastructure), Ravi Menon (platform and security).
