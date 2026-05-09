# dotfiles

Personal development environment configuration.

## Overview

This repository contains my personal dotfiles, currently featuring Neovim, Ghostty, OpenCode AI, Zsh, Powerlevel10k, and Git configurations.

## Prerequisites

Before symlinking the configurations, install the following tools in order.

### 1. Clone this repository

```sh
git clone https://github.com/earvinpiamonte/dotfiles.git ~/dotfiles
```

### 2. [Homebrew](https://brew.sh)

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 3. [Git](https://git-scm.com)

macOS ships with Git, but you can upgrade to the latest version via Homebrew:

```sh
brew install git
```

### 4. [Fonts](https://formulae.brew.sh/cask/font-jetbrains-mono-nerd-font)

Ghostty and Neovim are configured to use **JetBrainsMono Nerd Font**.

```sh
brew install --cask font-jetbrains-mono-nerd-font
```

### 5. [Oh My Zsh](https://ohmyz.sh)

```sh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### 6. [Powerlevel10k](https://github.com/romkatv/powerlevel10k)

```sh
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

### 7. [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)

```sh
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

### 8. [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)

```sh
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

### 9. [zoxide](https://github.com/ajeetdsouza/zoxide)

```sh
brew install zoxide
```

### 10. [fzf](https://github.com/junegunn/fzf)

```sh
brew install fzf
```

### 11. [bat](https://github.com/sharkdp/bat)

```sh
brew install bat
```

### 12. [nvm](https://github.com/nvm-sh/nvm)

```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
```

### 13. [ffmpeg](https://ffmpeg.org) (optional)

```sh
brew install ffmpeg
```

### 14. [Neovim](https://neovim.io)

Requires Neovim >= 0.10.

```sh
brew install neovim
```

### 15. [Ghostty](https://ghostty.org)

```sh
brew install --cask ghostty
```

### 16. [OpenCode](https://opencode.ai)

```sh
curl -fsSL https://opencode.ai/install | bash
```

## Neovim Configuration

### Features

Based on [kickstart.nvim](https://github.com/nvim-lua/kickstart.nvim) with the following custom additions:

| Plugin | Description |
|--------|-------------|
| [diffview.nvim](https://github.com/sindrets/diffview.nvim) | Git diff viewer |
| [neoscroll.nvim](https://github.com/karb94/neoscroll.nvim) | Smooth scrolling |
| [render-markdown.nvim](https://github.com/MeanderingProgrammer/render-markdown.nvim) | Enhanced Markdown rendering with images and mermaid diagrams |
| [smear-cursor.nvim](https://github.com/sphamba/smear-cursor.nvim) | Smooth cursor animation |

### Symlink

```sh
ln -s ~/dotfiles/nvim ~/.config/nvim
```

Start Neovim and plugins will install automatically:

```sh
nvim
```

## OpenCode Configuration

### Overview

Configuration for [OpenCode](https://opencode.ai), an AI-powered coding assistant.

### Symlink

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

### Symlink

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

### Symlink

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

### Symlink

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

### Symlink

```sh
ln -s ~/dotfiles/git/.gitconfig ~/.gitconfig
```

### Files

| File | Description |
|------|-------------|
| `.gitconfig` | Git user configuration |

## Final Step

After symlinking all configurations, reload your shell to apply changes:

```sh
exec zsh
```

Or restart your terminal emulator.

## License

[MIT](LICENSE) - Copyright (c) 2026 Noel Earvin Piamonte
