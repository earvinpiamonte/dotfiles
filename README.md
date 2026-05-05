# Dotfiles

Personal development environment configuration.

## Overview

This repository contains my personal dotfiles, currently featuring a Neovim configuration based on [kickstart.nvim](https://github.com/nvim-lua/kickstart.nvim).

## Neovim Configuration

### Features

- **Plugin Manager**: [lazy.nvim](https://github.com/folke/lazy.nvim)
- **Fuzzy Finding**: [Telescope](https://github.com/nvim-telescope/telescope.nvim) with fzf-native
- **LSP**: [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) with [Mason](https://github.com/mason-org/mason.nvim) for automatic tool installation
- **Autocompletion**: [blink.cmp](https://github.com/saghen/blink.cmp) with [LuaSnip](https://github.com/L3MON4D3/LuaSnip)
- **Formatting**: [conform.nvim](https://github.com/stevearc/conform.nvim)
- **Syntax Highlighting**: [nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter)
- **File Explorer**: [neo-tree](https://github.com/nvim-neo-tree/neo-tree.nvim)
- **Git Integration**: [gitsigns.nvim](https://github.com/lewis6991/gitsigns.nvim), [diffview.nvim](https://github.com/sindrets/diffview.nvim)
- **Colorscheme**: [kanagawa.nvim](https://github.com/rebelot/kanagawa.nvim) (wave theme, transparent)
- **Status Line**: [mini.statusline](https://github.com/nvim-mini/mini.nvim)
- **Markdown**: [render-markdown.nvim](https://github.com/MeanderingProgrammer/render-markdown.nvim) with image support
- **Keybinds**: [which-key.nvim](https://github.com/folke/which-key.nvim)

### Custom Plugins

| Plugin | Description |
|--------|-------------|
| `diffview.nvim` | Git diff viewer with custom keymaps (`<leader>gd`, `<leader>gq`, `<leader>gr`) |
| `neoscroll.nvim` | Smooth scrolling |
| `render-markdown.nvim` | Enhanced Markdown rendering with images and mermaid diagrams |
| `smear-cursor.nvim` | Smooth cursor animation |

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

## License

[MIT](LICENSE) - Copyright (c) 2026 Noel Earvin Piamonte
