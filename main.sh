export DOTFILES_PATH=${0:a:h}
export PROGRAMS_PATH=$(readlink -f "$DOTFILES_PATH/..")
# $(readlink -f "$(which $0)/..")

# vim mode inside the terminal
set -o vi
set editing-mode vi
set keymap vi
set shiftwidth=4
set clipboard=unnamedplus


#\\\_ COMPLETIONS _///#
 # zstyle :compinstall filename '/Users/fd0/.zshrc'
zstyle ':completion:*' list-colors "${(@s.:.)LS_COLORS}"
autoload -Uz compinit
compinit
autoload -Uz bashcompinit
bashcompinit
# The following lines were added by compinstall
# zstyle :compinstall filename '/Users/marcpartensky/.zshrc'

# autoload -Uz compinit
# compinit

# autocompletion
# source ~/.zsh-plugins/zsh-autocomplete/zsh-autocomplete.plugin.zsh
# zstyle ':autocomplete:*' config off
zstyle ':autocomplete:*' min-input 3


# pip zsh completion start
function _pip_completion {
  local words cword
  read -Ac words
  read -cn cword
  reply=( $( COMP_WORDS="$words[*]" \
             COMP_CWORD=$(( cword-1 )) \
             PIP_AUTO_COMPLETE=1 $words[1] 2>/dev/null ))
}
compctl -K _pip_completion pip3

# Antigen
ANTIGEN_CACHE=false
source ${0:a:h}/antigen.zsh
antigen theme romkatv/powerlevel10k
antigen theme eastwood
antigen theme kardan
antigen theme nicoulaj
# antigen theme candy
# antigen theme robbyrussell
antigen bundle zsh-users/zsh-autosuggestions
antigen bundle zsh-users/zsh-syntax-highlighting
#antigen bundle soimort/translate-shell
antigen apply

bindkey '\t' autosuggest-accept

# ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=#ff00ff,bg=cyan,bold,underline"
# ZSH_THEME="powerlevel10k/powerlevel10k"
# ZSH_THEME="eastwood"

# export GREP_OPTIONS="--color=always"
# export GREP_COLORS="ms=01;31:mc=01;31:sl=:cx=:fn=35:ln=32:bn=32:se=36"

eval "$(pyenv init -)"

source ${0:a:h}/exports.sh
source ${0:a:h}/aliases.sh
source ${0:a:h}/functions.sh

ln -snf ${0:a:h}/.zshenv ~
ln -snf ${0:a:h}/.p10k.zsh ~
source ${0:a:h}/.zshenv
source ${0:a:h}/.p10k.zsh


# When started as 'evim', evim.vim will already have done these settings, bail out.
# if v:progname =~? "evim"
#  finish
# endif

# Get the defaults that most users want.
# source $VIMRUNTIME/defaults.vim

# if has("vms"); then
#  set nobackup
  # do not keep a backup file, use versions instead
# else
#  set backup
  # keep a backup file (restore to previous version)
#  if has('persistent_undo'); then
#    set undofile	# keep an undo file (undo changes after closing)
#  fi
# fi

# if [&t_Co > 2 -o has("gui_running")]; then
  # Switch on highlighting the last used search pattern.
#  set hlsearch
# fi

# Put these in an autocmd group, so that we can delete them easily.
# augroup vimrcEx
#  au!
  # For all text files set 'textwidth' to 78 characters.
#  autocmd FileType text setlocal textwidth=78
# augroup END

# Add optional packages.
# The matchit plugin makes the % command work better, but it is not backwards
# compatible.
# The ! means the package won't be loaded right away but when plugins are
# loaded during initialization.
# if [has('syntax') -a has('eval')]; then
#  packadd! matchit
# fi

# prompt_context() {
#   if [[ "$USER" != "$DEFAULT_USER" || -n "$SSH_CLIENT" ]]; then
#     prompt_segment black default "%(!.%{%F{yellow}%}.)$USER"
#   fi
# }
