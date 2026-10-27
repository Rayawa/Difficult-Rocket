# Difficult-Rocket

[English](README.md) | 简体中文

支持模组及可选 Rust 游戏组件的 Python 火箭游戏框架。

## 项目概述

仓库包含 Difficult Rocket 运行框架、渲染素材、配置及游戏/模组组件，分支保留上游架构与许可，Python 入口启动桌面运行环境。

## 技术栈与依赖

`pyproject.toml` 声明 Python 3.8 及以上，依赖 uv、pyglet、Pillow、psutil、defusedxml、TOML 库及 lib-not-dr。锁文件与配置包含 Git 来源依赖；构建对应原生组件另需 Rust 工具链。

## 文件结构

- `DR.py` — 桌面入口
- `Difficult_Rocket/` — 运行框架与 API
- `mods/` — 游戏和模组组件
- `assets/` — 纹理、字体与翻译
- `config/` — 运行配置
- `pyproject.toml` — 依赖与工具配置
- `uv.lock` — 锁定环境

## 快速上手

安装 uv 后，在仓库根目录执行：

```bash
uv sync
uv run python DR.py
```

运行需要桌面图形环境，首次获取 Git 依赖需要网络。可选原生组件的构建配置见 `mods/`，MPL-2.0 许可见 [LICENSE](LICENSE)。
