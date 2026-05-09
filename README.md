# dotfiles

Personal development environment configuration.

## Overview

This repository contains my personal dotfiles, currently featuring Neovim, Ghostty, OpenCode AI, Zsh, Powerlevel10k, and Git configurations.

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

## Ghostty Configuration

### Overview

Configuration for [Ghostty](https://ghostty.org), a fast, feature-rich, and cross-platform terminal emulator.

### Installation

1. Symlink the Ghostty configuration:

```sh
ln -s ~/dotfiles/ghostty ~/Library/Application\ Support/com.mitchellh.ghostty
```

### Files

| File | Description |
|------|-------------|
| `config` | Main configuration file (theme, font, keybindings, etc.) |

## Zsh Configuration

### Overview

Configuration for Zsh shell with Oh My Zsh, including plugins and custom aliases.

### Installation

1. Symlink the Zsh configuration files:

```sh
ln -s ~/dotfiles/zsh/.zshrc ~/.zshrc
ln -s ~/dotfiles/zsh/.zsh_aliases ~/.zsh_aliases
ln -s ~/dotfiles/zsh/.zshenv ~/.zshenv
ln -s ~/dotfiles/zsh/.zprofile ~/.zprofile
```

### Files

| File | Description |
|------|-------------|
| `.zshrc` | Main Zsh configuration (Oh My Zsh, plugins, theme, keybindings) |
| `.zsh_aliases` | Custom aliases and utility functions |
| `.zshenv` | Environment variables and PATH exports |
| `.zprofile` | Login shell configuration |

## Powerlevel10k Configuration

### Overview

Configuration for [Powerlevel10k](https://github.com/romkatv/powerlevel10k), a fast and customizable Zsh prompt theme.

### Installation

1. Symlink the Powerlevel10k configuration:

```sh
ln -s ~/dotfiles/p10k/.p10k.zsh ~/.p10k.zsh
```

### Files

| File | Description |
|------|-------------|
| `.p10k.zsh` | Prompt theme configuration (segments, colors, icons) |

## Git Configuration

### Overview

Global Git configuration including user identity and default settings.

### Installation

1. Symlink the Git configuration:

```sh
ln -s ~/dotfiles/git/.gitconfig ~/.gitconfig
```

### Files

| File | Description |
|------|-------------|
| `.gitconfig` | Git user configuration |

## License

[MIT](LICENSE) - Copyright (c) 2026 Noel Earvin Piamonte
