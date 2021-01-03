#!/usr/bin/env zsh

# This file aims to load all dependencies on a new fresh osx environment.
# It is inspired from https://gist.github.com/w3cj/76cd9fb9f346e153b6f0dc46fd025620

xcode-select --install /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew update
brew cask install iterm2
brew install neovim
# update iterm2 settings -> colors, keep directory open new shell, keyboard shortcuts
# set brew bash as default shell
brew install fortune
brew install cowsay
brew install ccat
brew install highlight
brew install cmatrix
brew install lolcat
brew install figlet
brew install toilet
brew install watch
brew install jq fzf peco #emoji completion
brew install emojify

brew install git
# brew install vcprompt
# update bash_profile
# brew cask install spectacle
brew cask install rectangle
brew cask install alfred
# set CMD+space to launch alfred
# brew cask install firefox
# install nvm/node
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
nvm install stable
npm install -g lite-server eslint
brew cask install visual-studio-code
brew cask install hyperswitch

# dynamic history search
pip install percol

if [ -d "~/.config" ]; then
    makedir ~/.config
fi

if [ -d "~/.config/nvim" ]; then
    git clone https://github.com/MarcPartensky/nvim.git ~./config
fi

