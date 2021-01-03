# vim mode inside the terminal
# set -o vi
# set editing-mode vi
# set keymap vi
# set shiftwidth=4
# set clipboard=unnamed

#\\\_ COMPLETIONS _///#
# zstyle :compinstall filename '/Users/fd0/.zshrc'
# zstyle ':completion:*' list-colors "${(@s.:.)LS_COLORS}"
# autoload -Uz compinit
# compinit
# autoload -Uz bashcompinit
# bashcompinit

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

#Esclave
alias esclave="cd ~/discordbot/esclave"
alias esclave-aws="ssh -i 'discordbotofmarcpartensky.pem' ubuntu@ec2-15-236-33-61.eu-west-3.compute.amazonaws.com"


mcd() {
    mkdir -p -- "$1" &&
      cd -P -- "$1"
}

# Mamp
alias startmamp='cd /Applications/MAMP/bin && ./start.sh'
alias stopmamp='cd /Applications/MAMP/bin && ./stop.sh'


alias json-beautifer="chrome https://jsonformatter.curiousconcept.com/"
alias github="chrome https://github.com/MarcPartensky/"

source ~/antigen.zsh
# antigen theme romkatv/powerlevel10k
antigen bundle zsh-users/zsh-autosuggestions
#antigen bundle soimort/translate-shell
antigen apply

ZSH_THEME="powerlevel10k/powerlevel10k"
# The following lines were added by compinstall
# zstyle :compinstall filename '/Users/marcpartensky/.zshrc'

# autoload -Uz compinit
# compinit

source ./aliases.sh
source ./functions.sh
source ./exports.sh

# End of lines added by compinstall

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

# Shouldn't have to do that but doing it anyway

# prompt_context() {
#   if [[ "$USER" != "$DEFAULT_USER" || -n "$SSH_CLIENT" ]]; then
#     prompt_segment black default "%(!.%{%F{yellow}%}.)$USER"
#   fi
# }
