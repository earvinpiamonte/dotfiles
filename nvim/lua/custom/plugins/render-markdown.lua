return {
  'MeanderingProgrammer/render-markdown.nvim',
  event = 'VeryLazy',
  ft = { 'markdown', 'norg', 'rmd', 'org', 'codecompanion' },
  dependencies = {
    'nvim-treesitter/nvim-treesitter',
    'echasnovski/mini.icons',
    {
      '3rd/image.nvim',
      opts = {
        backend = 'kitty',
        integrations = { markdown = { enabled = true, only_render_image_at_cursor = true } },
        max_width = 100,
        max_height = 12,
        max_height_window_percentage = nil,
        window_overlap_clear_enabled = true,
        editor_only_render_when_focused = true,
        tmux_passthrough = true,
      },
    },
  },
  ---@module 'render-markdown'
  ---@type render.md.UserConfig
  opts = {
    render_modes = { 'n', 'c', 't', 'i' },
    bullet = { enabled = true },
    checkbox = { enabled = true },
    code = { sign = false },
    heading = {
      sign = false,
      position = 'inline',
      icons = { '󰲡 ', '󰲣 ', '󰲥 ', '󰲧 ', '󰲩 ', '󰲫 ' },
    },
    paragraph = { left_margin = 0, min_width = 0 },
    pipe_table = { enabled = true },
    quote = {
      enabled = true,
      repeat_linebreak = true,
    },
    image = {
      enabled = true,
      only_render_image_at_cursor = true,
      max_file_size = 10, -- MB
    },
    mermaid = {
      enabled = true,
    },
  },
}
