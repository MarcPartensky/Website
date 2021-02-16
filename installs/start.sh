#!/usr/bin/env zsh

# It is inspired from https://gist.github.com/w3cj/76cd9fb9f346e153b6f0dc46fd025620

# xcode-select --install /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
#

case `uname` in
  Darwin)
    # commands for OS X go here
		/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
		brew update
		brew install git
		brew install alacritty
		# brew cask install iterm2
		brew install neovim
		brew install pyenv
		brew install node
		brew install fortune
		brew install cowsay
		brew install ccat
		brew install highlight
		# brew install cmatrix tmatrix
		brew install lolcat
		brew install figlet
		brew install toilet
		brew install watch
		brew install jq fzf peco #emoji completion
		brew install emojify

		# brew install vcprompt
		# brew cask install spectacle
		# brew cask install firefox
		# install nvm/node
		brew cask install rectangle
		brew cask install alfred
  ;;
  Linux)
    # commands for Linux go here
  ;;
  FreeBSD)
    # commands for FreeBSD go here
  ;;
esac


# curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
# nvm install stable
# npm install -g lite-server eslint
# brew cask install visual-studio-code
# brew cask install hyperswitch

# dynamic history search
pip install percol

if [ -d "~/.config" ]; then
    makedir ~/.config
fi

if [ -d "~/.config/nvim" ]; then
    git clone https://github.com/MarcPartensky/nvim.git ~./config
fi

