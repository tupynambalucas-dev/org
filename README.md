# Enterprise Organization Meta-Repository (`tupynambalucas-dev/org`)

Master enterprise orchestrator and unified multi-repository workspace for the `tupynambalucas-dev` organization. This umbrella meta-repository coordinates foundational organizational repositories (`core`), the nested product portfolio sub-meta-repository (`ecosystem/`), and the developer's individual professional namespace (`user/`) via [Mani](https://manicli.com) and multi-root IDE workspaces while preserving completely independent Git histories, branches, release cycles, and CI/CD pipelines.

---

## 1. Architecture Overview

`org` forms Layer 0 (Master Enterprise Host) of the organization's hierarchical meta-repository topology. Rather than coupling repositories with Git submodules (`160000` gitlinks), `org` binds each repository declaratively in [`mani.yaml`](./mani.yaml) with `sync_gitignore: false`, `ignore_non_existing: true`, and explicit search negation rules in [`.ignore`](./.ignore) and [`.rgignore`](./.rgignore).

```mermaid
flowchart TD
  direction TB

  Host["org (Master Mani Orchestrator & Workspace Host)"]

  subgraph Tier1["Tier 1: Core Enterprise Foundation (tags: core)"]
    Repo1[".github (Public Governance & Profile)"]
    Repo2[".github-private (Internal Governance & Copilot)"]
    Repo3["agent-mesh (Universal AI Agent Mesh)"]
    Repo4["platform (Core Platform Monorepo)"]
    Repo5["docs (Sovereign Documentation Hub)"]
    Repo6["foundation (WSL2 DaC, Identities & CLI Monorepo)"]
  end

  subgraph Tier2["Tier 2: Product Portfolio Ecosystem (tags: ecosystem)"]
    Eco["ecosystem (Portfolio Sub-Meta-Repository)"]
    Omni["ecosystem/commercial/omnichannel"]
    Elo["ecosystem/commercial/elo-organico"]
    Tessel["ecosystem/internal/tessel"]
    Eco --> Omni
    Eco --> Elo
    Eco --> Tessel
  end

  subgraph Tier3["Tier 3: Developer Professional Space (tags: user)"]
    Profile["user/profile (@tupynambalucas/profile)"]
    AcadLab["user/academic-lab (@tupynambalucas/academic-lab)"]
    External["user/external/* (Third-Party & Client Contracts)"]
  end

  Host -. "mani sync --tags core" .-> Tier1
  Host -. "mani sync --tags ecosystem" .-> Tier2
  Host -. "mani sync --tags user" .-> Tier3

  classDef repo fill:#1e1e2e,stroke:#89b4fa,stroke-width:2px,color:#cdd6f4;
  class Host,Repo1,Repo2,Repo3,Repo4,Repo5,Repo6,Eco,Omni,Elo,Tessel,Profile,AcadLab,External repo;
```

---

## 2. Managed Repositories & Navigation

| Repository | Path / Namespace | Tier Tag | Branch | Documentation | Agent Context | Purpose |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| [`.github`](./.github/README.md) | `.github` | `core` | `main` | [`README.md`](./.github/README.md) | [`AGENTS.md`](./.github/AGENTS.md) | Organization-wide governance, community health files, public profile, and IDE templates. |
| [`.github-private`](./.github-private/README.md) | `.github-private` | `core` | `main` | [`README.md`](./.github-private/README.md) | [`AGENTS.md`](./.github-private/AGENTS.md) | Member-only profile, enterprise Copilot custom agents, managed AI settings, and internal references. |
| [`agent-mesh`](./agent-mesh/README.md) | `agent-mesh` | `core` | `main` | [`README.md`](./agent-mesh/README.md) | [`AGENTS.md`](./agent-mesh/AGENTS.md) | Universal AI agent governance monorepo, domain plugins, sovereign MCP servers, and modular skills. |
| [`platform`](./platform/README.md) | `platform` | `core` | `main` | [`README.md`](./platform/README.md) | [`AGENTS.md`](./platform/AGENTS.md) | Core domain monorepo hosting Kubernetes GitOps manifests, Cortex AI gateway, studio tools, and corporate services. |
| [`docs`](./docs/README.md) | `docs` | `core` | `main` | [`README.md`](./docs/README.md) | [`AGENTS.md`](./docs/AGENTS.md) | Sovereign documentation portal built on Docusaurus v3 with Crowdin localization. |
| [`foundation`](./foundation/README.md) | `foundation` | `core` | `main` | [`README.md`](./foundation/README.md) | [`AGENTS.md`](./foundation/AGENTS.md) | Sovereign foundation monorepo hosting WSL2 custom distributions (`distributions/`), developer toolchain & CLI (`tools/`), machine identities and Token Broker (`identity/`), host virtualization (`virtualization/`), and documentation hub (`references/`). |
| [`ecosystem`](./ecosystem/README.md) | `ecosystem` | `ecosystem` | `main` | [`README.md`](./ecosystem/README.md) | [`AGENTS.md`](./ecosystem/AGENTS.md) | Product portfolio sub-meta-repository orchestrating `commercial/`, `internal/`, `oss/`, and `clients/`. |
| [`omnichannel`](./ecosystem/commercial/omnichannel/README.md) | `ecosystem/commercial/omnichannel` | `ecosystem`, `commercial` | `main` | [`README.md`](./ecosystem/commercial/omnichannel/README.md) | [`AGENTS.md`](./ecosystem/commercial/omnichannel/AGENTS.md) | Commercial multi-tenant omnichannel messaging gateway and FSM workflow engine. |
| [`elo-organico`](./ecosystem/commercial/elo-organico/README.md) | `ecosystem/commercial/elo-organico` | `ecosystem`, `commercial` | `main` | [`README.md`](./ecosystem/commercial/elo-organico/README.md) | [`AGENTS.md`](./ecosystem/commercial/elo-organico/AGENTS.md) | Commercial organic product sharing and community management platform. |
| [`tessel`](./ecosystem/internal/tessel/README.md) | `ecosystem/internal/tessel` | `ecosystem`, `internal` | `main` | [`README.md`](./ecosystem/internal/tessel/README.md) | [`AGENTS.md`](./ecosystem/internal/tessel/AGENTS.md) | Proprietary hybrid spatial social ecosystem and WebGPU/Three.js 3D simulation engine. |
| [`profile`](./user/profile/README.md) | `user/profile` | `user` | `main` | [`README.md`](./user/profile/README.md) | [`AGENTS.md`](./user/profile/AGENTS.md) | Developer special GitHub profile repository and automated SVG stats renderer (`@tupynambalucas/profile`). |
| [`academic-lab`](./user/academic-lab/README.md) | `user/academic-lab` | `user` | `main` | [`README.md`](./user/academic-lab/README.md) | [`AGENTS.md`](./user/academic-lab/AGENTS.md) | Structured knowledge engineering and AI-assisted research monorepo (`@tupynambalucas/academic-lab`). |

### Multi-Root IDE Workspace

Open [`tupynambalucas-dev.code-workspace`](./tupynambalucas-dev.code-workspace) in VS Code or Antigravity IDE to mount foundation, ecosystem, and developer user repositories in a unified workspace with integrated Mani tasks.

---

## 3. Environment, Secret & Plugin Governance

### A. Three-Tier Secret Resolution Architecture

The ecosystem resolves development credentials across three cascading tiers so workflows operate seamlessly with or without active cloud sessions:

1. **Process Environment**: Variables exported in the active shell session or injected via `infisical run --projectId <PROJECT_ID> --env dev -- <command>`.
2. **Local and Ancestor `.env` Files**: If environment variables are absent from the shell, sovereign MCP launchers (`scripts/launcher.cjs`) walk up the directory tree to discover `.env` files in the child repository or at the `org` root (copied from [`.env.example`](./.env.example)).
3. **Infisical CLI Fallback**: If neither process variables nor `.env` files satisfy required keys, launchers invoke `infisical export` using authenticated Machine Identity credentials or developer login sessions.

### B. Enterprise AI Agent Mesh Dual Consumption Model

```mermaid
flowchart LR
  subgraph LocalMetaRepo["org (Hierarchical Relative Mode)"]
    OCP["org/.agents/plugins.json"] -->|"agent-mesh/plugins/packages"| AMP["agent-mesh/plugins/packages"]
    ECP["ecosystem/.agents/plugins.json"] -->|"../agent-mesh/plugins/packages"| AMP
    UCP["user/*/.agents/plugins.json"] -->|"../../agent-mesh/plugins/packages"| AMP
  end

  subgraph ExternalConsumers["Standalone Checkouts & CI Runners"]
    EPJ[".agents/plugins.json"] -->|umbrella package fallback| NMA["node_modules/@tupynambalucas-dev/agent-mesh/plugins/packages"]
  end

  AMP -.->|releases to| NMA
  classDef box fill:#1e1e2e,stroke:#89b4fa,stroke-width:2px,color:#cdd6f4;
  class OCP,ECP,UCP,AMP,EPJ,NMA box;
```

| Mode | Environment | Discovery Manifest (`.agents/plugins.json`) | Package Dependency |
| :--- | :--- | :--- | :--- |
| **Meta-Repository Mode** | `org`, `ecosystem`, and `user/*` inside `projects/org/` | Relative path to `agent-mesh/plugins/packages` (`./`, `../`, `../../`, `../../../`) | None (zero build steps, zero NTFS junctions, direct local path resolution) |
| **External Service Mode** | Standalone Repositories (`omnichannel`, `platform`, `docs`) | `node_modules/@tupynambalucas-dev/agent-mesh/plugins/packages` | `@tupynambalucas-dev/agent-mesh` via `catalogs.plugins-stack` |

---

## 4. Getting Started

### Prerequisites

- **Git**: `>= 2.40` (configured with Ed25519 SSH commit signing)
- **Mani CLI**: `>= 0.30` (multi-repository orchestrator)
- **Infisical CLI**: `>= 0.31` (secret management)

Install `mani` on Windows via Scoop (or via the corporate WSL2 distribution `tupynambalucas-dev`):

```powershell
scoop bucket add poldi https://github.com/aliesbelik/poldi
scoop install mani
```

### Workspace Initialization

Clone the master orchestrator into `projects/org` and synchronize repositories:

```bash
git clone git@github.com:tupynambalucas-dev/org.git
cd org

# Synchronize all tiers (core + ecosystem + user)
mani sync

# Or synchronize selectively by tier tag
mani sync --tags core
mani sync --tags ecosystem
mani sync --tags user
```

---

## 5. Multi-Repository Operations

| Command | Target Scope | Description |
| :--- | :--- | :--- |
| `mani sync` | All repositories | Clones missing repositories across `core`, `ecosystem`, and `user` declared in [`mani.yaml`](./mani.yaml). |
| `mani sync --tags <tag>` | Tagged tier | Selectively clones repositories matching `core`, `ecosystem`, `commercial`, `internal`, or `user`. |
| `mani run status` | All synced repos | Executes `git status -s` in parallel across all existing repositories. |
| `mani run dirty` | Dirty repos only | Displays a formatted table of only repositories containing uncommitted changes. |
| `mani run overview` | All synced repos | Displays a consolidated audit table with active branch, dirty status, and latest commit. |
| `mani run fetch` | All synced repos | Executes `git fetch origin --prune` in parallel across all managed repositories. |
| `mani run pull` | All synced repos | Pulls latest `main` branch updates across all managed repositories. |
| `mani run branch` | All synced repos | Displays the active Git branch for every repository in a formatted table. |
| `mani run verify-workstation` | `foundation` | Runs the workstation compliance verification script via `gh tl verify`. |

```bash
# Execute daily multi-repository health checks
mani run status
mani run overview
mani run fetch
mani run pull
```

---

## 6. Governance & Contributing Standards

All contributions across `org` and its managed repositories must comply with organizational engineering governance:

1. **Cryptographic Commit Signing**: All Git commits and annotated tags MUST be signed using SSH (`git commit -S -m "..."`). Unsigned commits are rejected by repository rulesets.
2. **Conventional Commits**: Commit messages must follow the Conventional Commits v1.0.0 specification (`<type>(<scope>): <description>`).
3. **Single-Branch GitHub Flow**: Each repository operates independently on `main`. Developers create short-lived branches (`feat/<slug>`, `fix/<slug>`, `docs/<slug>`, `chore/<slug>`), push them, and open Pull Requests against `main`.
4. **Zero-Emoji Invariant**: Emojis are strictly prohibited in commit messages, documentation, code comments, and agent interactions.
5. **Secret Hygiene**: Never commit `.env` files or plaintext credentials; use [`.env.example`](./.env.example) templates and Infisical secret injection.
6. **AI Agent Context**: Autonomous agents operating in this workspace MUST read [AGENTS.md](./AGENTS.md) prior to executing tasks.

---

## 7. License

Licensed under the [Apache License 2.0](./LICENSE). Copyright (c) 2026 tupynambalucas.dev.
