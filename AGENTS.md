# tupynambalucas-dev Master Organization Meta-Repository Agent Context

This document serves as the root context router (Layer 1) for AI agents operating in the
`tupynambalucas-dev/org` master enterprise meta-repository (`projects/org/`).

## Workspace Navigation

- [README.md](./README.md): Primary developer documentation and Mani workspace orchestration runbook.
- [mani.yaml](./mani.yaml): Declarative multi-repository manifest managing foundation (`core`), product portfolio (`ecosystem`), and developer (`user`) repositories, remotes, and batch tasks.
- [tupynambalucas-dev.code-workspace](./tupynambalucas-dev.code-workspace): Canonical multi-root IDE workspace binding foundation, product ecosystem, and developer repositories.
- [LICENSE](./LICENSE): Apache License 2.0 governing meta-repository orchestration assets.
- [.github](./.github/AGENTS.md): Organization governance, community health standards, and public profile.
- [.github-private](./.github-private/AGENTS.md): Organization internal governance, member-only profile, and enterprise AI settings.
- [agent-mesh](./agent-mesh/AGENTS.md): Enterprise AI agent mesh context router, MCP packages, domain plugins, and modular skills.
- [platform](./platform/AGENTS.md): Core platform monorepo containing services, apps, and Kubernetes manifests.
- [docs](./docs/AGENTS.md): Sovereign documentation hub built with Docusaurus v3 and Crowdin.
- [foundation](./foundation/AGENTS.md): Sovereign foundation monorepo hosting WSL2 custom distributions (`distributions/`), developer toolchain & GitHub CLI extensions (`tools/`), machine identities and Token Broker (`identity/`), Windows host virtualization (`virtualization/`), and Diataxis documentation hub (`references/`).
- [ecosystem](./ecosystem/AGENTS.md): Product portfolio sub-meta-repository (`tupynambalucas-dev/ecosystem`) orchestrating commercial SaaS solutions (`ecosystem/commercial/`), internal proprietary assets (`ecosystem/internal/`), open-source packages (`ecosystem/oss/`), and corporate B2B client projects (`ecosystem/clients/`).
- [user](./user/AGENTS.md): Individual developer professional namespace (`@tupynambalucas`) housing the developer's special GitHub profile repository (`user/profile`), knowledge research monorepo (`user/academic-lab`), and external contractor/client engagements (`user/external/`).

## Governance Standards

- **Branching Model**: Single-Branch GitHub Flow on `main`. Short-lived branches MUST use Conventional Commit prefixes (`feat/`, `fix/`, `docs/`, `chore/`, `refactor/`, `ci/`, `perf/`, `test/`, `build/`, `style/`, `revert/`, `hotfix/`).
- **Cryptographic Signature**: All Git commits and annotated tags MUST be signed with SSH (`git commit -S -m "..."`). Multi-tier `.gitconfig` conditional includes automatically route `@tupynambalucas-dev` inside `projects/org/` and `@tupynambalucas` inside `projects/org/user/`.
- **Conventional Commits**: All commit messages must follow `<type>[optional (<scope>)][!]: <description>` (`<= 72` chars target, `<= 100` chars maximum).
- **Zero-Emoji Policy**: Emojis are strictly forbidden across all code, PRs, comments, and agent interactions.
- **Secret Hygiene**: Never commit plaintext tokens. Environment variables cascade via Infisical or local/parent `.env` files.
- **License**: `Apache-2.0` (`Copyright (c) 2026 tupynambalucas.dev`) across all public repositories, packages, and plugins.
- **Workspace Orchestration**: Repositories are managed as sovereign Git repositories coordinated via `mani`. Git submodules and `160000` commit gitlinks are deprecated and removed.

## Multi-Repository Operations with Mani

Cross-repository commands and queries are executed using `mani`:

```bash
# Synchronize all repositories (or filter by tier tag: core, ecosystem, user)
mani sync
mani sync --tags core
mani sync --tags ecosystem
mani sync --tags user

# Check status across all synced repositories
mani run status

# Comprehensive multi-repository audit table (branch, dirty status, last commit)
mani run overview

# Fetch remote changes for all repositories
mani run fetch

# Pull latest main across all repositories
mani run pull

# Display current branches
mani run branch
```

## AI Agent Plugin Consumption (Hierarchical & Standalone Dual Consumption Model)

The organization operates under a unified Dual Consumption Model for AI agent plugins and skills without requiring NTFS directory junctions:

1. **Meta-Repository & Hierarchical Workspace Mode (`org`, `ecosystem`, `user`)**:
   - The root [`.agents/plugins.json`](./.agents/plugins.json) registers local relative paths directly:
     ```json
     {
       "entries": [
         { "path": "agent-mesh/plugins/packages" }
       ]
     }
     ```
   - Nested sub-workspaces inside `org/` (`ecosystem/`, `user/*`, `ecosystem/commercial/*`, `ecosystem/internal/*`) resolve `agent-mesh/plugins/packages` via ascending relative paths (`../agent-mesh/plugins/packages`, `../../agent-mesh/plugins/packages`, `../../../agent-mesh/plugins/packages`) with automatic fallback to `node_modules/@tupynambalucas-dev/agent-mesh/plugins/packages`.
   - This enables real-time hot-reloading of agent plugins and MCP servers across the entire multi-root IDE workspace without intermediate package building or directory junctions.
2. **External & Standalone Monorepo Mode (`omnichannel`, `platform`, `docs`)**:
   - External services and isolated child repository checkouts consume the unified umbrella package `@tupynambalucas-dev/agent-mesh` via `catalogs.plugins-stack` in `pnpm-workspace.yaml`:
     ```yaml
     catalogs:
       plugins-stack:
         '@tupynambalucas-dev/agent-mesh': 'github:tupynambalucas-dev/agent-mesh'
     ```
   - All 11 domain plugins (`appsheet`, `atelier`, `docusaurus`, `github-actions`, `github-flow`, `github-org`, `github-releases`, `github-repo`, `gwork`, `profile`, `research`, `secrets`, `web`) and 9 sovereign MCP servers execute seamlessly via self-contained launchers (`scripts/launcher.cjs`) and committed bundles (`dist/bin.cjs`).

## Architectural Plans & Artifact Dual-Storage Standard

Architectural blueprints, technical analyses, and execution reports follow strict enterprise lifecycle and storage standards:
- **3-Folder Lifecycle Taxonomy**: Plans reside inside `<target-repo>/.agents/plans/` partitioned into `pending/<plan-slug>/` (all new and active suites), `completed/<plan-slug>/` (finished suites moved only after authoring `report.md`), and `superseded/<plan-slug>/` (obsolete or consolidated plans). Creating a root `plans/` directory or loose plan files is strictly prohibited.
- **Mandatory Folder-Suite Format (`pt-BR`)**: Every plan suite MUST be authored in Brazilian Portuguese (`pt-BR`) with `README.md`, ordered technical modules (`01-*.md`, ...), `manual-actions.md`, living `roadmap.md` (updated after every executed step), and post-execution `report.md` prior to archiving into `completed/`.
- **Dual-Storage Invariant**: Whenever an agent creates or updates a plan suite in the Antigravity conversation directory (`<appDataDir>/brain/<conversation-id>/<plan-slug>/`), an identical synchronized copy MUST ALWAYS be mirrored in `<target-repo>/.agents/plans/{pending,completed}/<plan-slug>/`.
- **Ignore & Index Triad**: All repositories ignore `.agents/plans/` in `.gitignore`, while explicitly un-ignoring it in `.ignore` and `.rgignore` (`!.agents/plans/`, `!.agents/plans/**`) and setting `"search.useIgnoreFiles": false` in `.vscode/settings.json` so files can always be attached with `@`.

## Required Skills

Agents operating at the `org` meta-repository layer MUST autonomously engage the domain skills provided by [`agent-mesh`](./agent-mesh/plugins/README.md):

- **Atelier Plugin (`@tupynambalucas-dev/plugin-atelier`)**: `router-architect`, `skill-architect`, `rule-architect`, `hook-architect`, `plugin-architect`, `plan-architect`.
- **GitHub Domain Plugins (`@tupynambalucas-dev/plugin-github-*`)**:
  - **`github-org`**: `github-org-operator`, `github-ruleset-operator`, `github-security-auditor`, `github-app-operator`.
  - **`github-repo`**: `github-repo-architect`, `readme-architect`, `readme-auditor`, `monorepo-architect`, `community-health-architect`, `license-architect`, `github-standards-architect`, `mani-operator`.
  - **`github-flow`**: `github-flow-operator`.
  - **`github-actions`**: `github-actions-operator`.
  - **`github-releases`**: `github-releases-operator`.
- **Secrets Plugin (`@tupynambalucas-dev/plugin-secrets`)**: `infisical-vault-operator`, `secret-rotation-operator`.
- **Profile Plugin (`@tupynambalucas-dev/plugin-profile`)**: `developer-profile-architect`, `developer-advancement-strategist`, `linkedin-profile-architect`, `linkedin-job-operator`, `linkedin-application-auditor`, `linkedin-outreach-operator`.
