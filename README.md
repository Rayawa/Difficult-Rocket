# Difficult Rocket

English | [简体中文](README_zh.md)


For the README, see [dr.shenjack.top](https://dr.shenjack.top/main/readme)

Readme please check out [dr.shenjack.top](https://dr.shenjack.top/main/readme-en)

## below is an old, synchronized readme
## An older, unsynchronized README follows

# Difficult Rocket

English | [简体中文](./README_zh.md)

- [GitHub](https://github.com/shenjackyuanjie/Difficult-Rocket)
- [Gitee](https://gitee.com/shenjackyuanjie/Difficult-Rocket)
- [AtomGit](https://atomgit.com/shenjackyuanjie/Difficult-Rocket)

- [Discord](https://discord.gg/kWzw2JrG6M)
- [Kook](https://kook.top/sRPjFG)

> Note: This repository will only publish updates to `DR SDK` in the future. Updates to `DR game` will be published [here](https://github.com/shenjackyuanjie/DR-game).

[![996.icu](https://img.shields.io/badge/996.icu-996.icu-red.svg)](https://996.icu)
[![semver](https://img.shields.io/badge/SemVer-2.0.0-blue.svg)](https://Semver.org/)
[![python-3.8.10](https://img.shields.io/badge/Written%20with%20Python-3.8.10-blue.svg)](https://Python.org)
[![pyglet-2.x](https://img.shields.io/badge/Written%20with%20Pyglet-2.x-blue.svg)](https://pyglet.org)
[![support python 3.8~12](https://img.shields.io/badge/Python-_3.8_~_3.12_-blue.svg)](https://Python.org)

## Versions

[Version numbering](./docs/src/version.md)

[![release version](https://img.shields.io/badge/Release-0.9.2.0-blue.svg)](https://github.com/shenjackyuanjie/Difficult-Rocket/releases)
[![pre version](https://img.shields.io/badge/Pre_Release-0.9.2.0-blue.svg)](https://github.com/shenjackyuanjie/Difficult-Rocket/releases)
[![develop version](https://img.shields.io/badge/Devloping-0.9.3-blue.svg)](https://github.com/shenjackyuanjie/Difficult-Rocket/releases)

[![language badge](https://stats.deeptrain.net/repo/shenjackyuanjie/Difficult-Rocket?theme=dark)](https://stats.deeptrain.net/repo/shenjackyuanjie/Difficult-Rocket?theme=dark)

[Latest DR SDK Actions build](https://nightly.link/shenjackyuanjie/Difficult-Rocket/workflows/nuitka/main)

[Latest DR rs Actions build](https://nightly.link/shenjackyuanjie/Difficult-Rocket/workflows/dr_rs/main)

## Introduction

A Python game similar to Simple Rockets (SR), a rocket simulator. It is lighter than the original SR.

[Planned features](docs/src/plan_features/README.md)

[YouTrack](https://difficult-rocket.youtrack.cloud/projects/8dafd498-59c0-4ce7-9900-d9292e9ed1f0)

[Changelog](docs/src/change_log/readme.md)

## Running

### 1. Clone

```bash title="clone.sh"
git clone https://github.com/shenjackyuanjie/Difficult-Rocket.git
# Or
git clone https://gitee.com/shenjackyuanjie/Difficult-Rocket.git
# Or alternatively
git clone git@github.com:shenjackyuanjie/Difficult-Rocket.git
```

### 2. Install dependencies

```bash title="install.sh"
python -m pip install --upgrade uv
python -m uv sync
```

### 3. Run

```bash title="run.sh"
python DR.py
```

## Environment requirements

> The development environment uses Python `3.8.18`, but `3.8+` also works.
>
> After `3.8` reaches EOL, `3.11` will be used for development.
>
> Python 3.8 is currently used because it officially supports Windows 7, whereas 3.9+ does not.

- `开发平台 1 - Windows 10 x64 22H2`
  - Python `3.8.18+`
    - `Python 3.8.18+ (heads/3.8:7f59c4c1d4, Aug 26 2023, 00:20:02) [MSC v.1900 64 bit (AMD64)] on win32`
  - `AMD R5 5800X`
  - `AMD RX 580 8G`

## Required Python modules

> Run: uv sync
> Build: uv sync --group build
> Compile: uv sync --all-groups

- `pyglet` (V2.x is bundled at `./libs/pyglet`)
- `xmltodict` (V0.12.0 is bundled at `./libs/xmltodict`)
- `pyperclip` (V1.8.2 is bundled at `./libs/pyperclip`)

## Acknowledgments

- Open-source projects
  - [pyglet](https://github.com/pyglet/pyglet): GUI and graphics rendering
  - tomls
    - `tomlkit`
    - `tomli`
    - `rtoml`
  - `xmltodict`: XML/dict conversion
  - `pyperclip`: Clipboard support
  - [rapier2d](https://rapier.rs/): Physics engine
  - [pyo3](https://pyo3.rs/main): Rust Python extensions

- Jundroo
  - Thanks for creating SR, a ~~magical~~ enjoyable game

- Main contributors
  - Contributor: Lead development
  - Contributor: DR game development
  - Contributor: DR rs development
  - Contributor: Documentation corrections and some language translations
  - Contributor: Language translations
  - Contributor: Documentation corrections
  - Contributor: Code optimization

## Related links

[Official documentation](https://dr.shenjack.top)

## License

[MPL-2.0](LICENSE)
