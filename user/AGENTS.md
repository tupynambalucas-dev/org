# User Professional Subsystem Agent Context Router

This document serves as the Layer 2 context router for AI agents operating within the
individual developer professional namespace (`user/`) of the `tupynambalucas-dev/org` meta-repository.

## Workspace Navigation

- [README.md](./README.md): Primary developer documentation and subsystem overview.
- [mani.yaml](./mani.yaml): Declarative multi-repository manifest for user repositories.
- [tupynambalucas-user.code-workspace](./tupynambalucas-user.code-workspace): Dedicated VS Code workspace for the developer persona.
- [profile](./profile/AGENTS.md): Developer profile repository, stats layout, and portfolio positioning.
- [academic-lab](./academic-lab/AGENTS.md): Academic research monorepo, technical notes, and Docusaurus documentation preset.

## Identity & Governance Standards

- **Git Identity**: `Tupynamba Lucas V. R.` (`tupynambalucas@gmail.com`).
- **Cryptographic Signature**: Commits must be signed with `~/.ssh/github_tupynambalucas_ed25519.pub`.
- **Zero-Emoji Policy**: Emojis are strictly forbidden across code, commits, and PR descriptions.
- **Conventional Commits**: All commit messages must follow `<type>(<scope>): <description>`.

## Multi-Repository Operations

```bash
mani sync
mani run status
mani run branch
```
