# dotfiles

Personal development environment configuration.

## Overview

This repository contains my personal dotfiles, currently featuring Neovim and OpenCode AI configurations.

## Neovim Configuration

### Features

Based on [kickstart.nvim](https://github.com/nvim-lua/kickstart.nvim) with the following custom additions:

| Plugin | Description |
|--------|-------------|
| [diffview.nvim](https://github.com/sindrets/diffview.nvim) | Git diff viewer |
| [neoscroll.nvim](https://github.com/karb94/neoscroll.nvim) | Smooth scrolling |
| [render-markdown.nvim](https://github.com/MeanderingProgrammer/render-markdown.nvim) | Enhanced Markdown rendering with images and mermaid diagrams |
| [smear-cursor.nvim](https://github.com/sphamba/smear-cursor.nvim) | Smooth cursor animation |

### Installation

1. Clone this repository:

```sh
git clone https://github.com/earvinpiamonte/dotfiles.git ~/dotfiles
```

2. Symlink the Neovim configuration:

```sh
ln -s ~/dotfiles/nvim ~/.config/nvim
```

3. Start Neovim - plugins will install automatically:

```sh
nvim
```

### Requirements

- Neovim >= 0.10 (stable or nightly)
- Git

## OpenCode Configuration

### Overview

Configuration for [OpenCode](https://opencode.ai), an AI-powered coding assistant.

### Installation

1. Symlink the OpenCode configuration:

```sh
ln -s ~/dotfiles/opencode ~/.config/opencode
```

### Files

| File | Description |
|------|-------------|
| `opencode.json` | Main configuration file (model settings, etc.) |

## License

[MIT](LICENSE) - Copyright (c) 2026 Noel Earvin Piamonte
