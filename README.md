# Difficult-Rocket

English | [简体中文](README_zh.md)

A Python rocket-game framework with mod support and optional Rust game components.

## Overview

The repository contains the Difficult Rocket runtime, rendering assets, configuration and game/mod components. The fork retains the upstream architecture and licensing; the Python entry point starts the desktop runtime.

## Technology and Dependencies

Python 3.8+ as declared by `pyproject.toml`, uv, pyglet, Pillow, psutil, defusedxml, TOML libraries and lib-not-dr. The lock/configuration includes Git-sourced dependencies. Rust tooling is needed only for building the associated native component.

## Repository Structure

- `DR.py` — desktop entry point
- `Difficult_Rocket/` — runtime and API
- `mods/` — game/mod components
- `assets/` — textures, fonts and translations
- `config/` — runtime configuration
- `pyproject.toml` — dependencies and tooling
- `uv.lock` — locked environment

## Quick Start

With uv installed, run from the repository root:

```bash
uv sync
uv run python DR.py
```

A desktop graphics environment is required. Git dependencies need network access on first setup. Consult `mods/` for optional native-component build configuration and [LICENSE](LICENSE) for MPL-2.0 licensing.
