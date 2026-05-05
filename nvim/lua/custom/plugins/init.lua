return {
  'sindrets/diffview.nvim',
  keys = {
    { '<leader>gd', '<cmd>DiffviewOpen<CR>', desc = 'Open Diffview' },
    { '<leader>gq', '<cmd>DiffviewClose<CR>', desc = 'Close Diffview' },
    { '<leader>gr', '<cmd>DiffviewRefresh<CR>', desc = 'Refresh Diffview' },
  },
  config = function()
    local actions = require("diffview.actions")
    require("diffview").setup({
      use_icons = false,
      view = {
        default = {
          layout = "diff2_vertical",
        },
      },
      file_panel = {
        listing_style = "list",
        win_config = {
          position = "right",
        },
      },
      keymaps = {
        file_panel = {
          { "n", "j", function()
            actions.next_entry()
            actions.select_entry()
          end, { desc = "Next file and show diff" } },
          { "n", "k", function()
            actions.prev_entry()
            actions.select_entry()
          end, { desc = "Prev file and show diff" } },
          { "n", "<down>", function()
            actions.next_entry()
            actions.select_entry()
          end, { desc = "Next file and show diff" } },
          { "n", "<up>", function()
            actions.prev_entry()
            actions.select_entry()
          end, { desc = "Prev file and show diff" } },
        },
      },
    })
  end,
}
