# Source viewer

A vim plugin for displaying source code from logs when log line contains pattern <filename.xyz#3>.

## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/randspy/source_viewer ~/.vim/bundle/source_viewer`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'https://github.com/randspy/source_viewer'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/randspy/source_viewer'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/randspy/source_viewer'` to .vimrc
  - Run `:PlugInstall`


Create environment variable for your source code root location.

    export SOURCE_VAR=/../path/../..
    
Copy BufOnly.vim (http://www.vim.org/scripts/script.php?script_id=1071) plugin into 
    
    ../.vim/plugin/
    
Copy into .vimrc

    set runtimepath^=~/.vim/bundle/source_viewer

To add shortcut (Ctrl + m) copy into .vimrc 

    map <C-m> :Sc<CR>
    
    
    
    

