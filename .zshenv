alias v=nvim
alias restart='exec $SHELL'
alias ez='nvim ~/.zshrc'
alias e='nvim ~/.zshenv'
alias mem="du -sh"
alias memfiles="du -sh * | sort -rh;"
alias vimrc='nvim ~/.vimrc'
alias ev='nvim ~/.config/nvim'
alias todo="nvim ~/programs/markdown/todolist/todolist.md"
alias t="todo"

alias alacritty="v ~/.config/alacritty/alacritty.yml"
alias isep="cd /Volumes/$/isep"
alias desk="desktop"
alias ports="lsof -Pn -i4"
alias ports2="netstat -ap tcp"
alias network="watch -n 1 \"netstat -p tcp\""
alias cat=ccat

### Games ###
alias tetris=bastet
alias spaceinvader=ninvaders
alias tshark="/Applications/Wireshark.app/Contents/MacOS/tshark"

# Git shortcuts
alias gi="git init"
alias ga="echo 'git add -A'; git add -A"
alias gr="git remote"
alias grv="git remote -v"
alias gs="git status"
alias grmc="git rm -r --cached ."
function gc { echo "git commit -m \"$@\""; eval "git commit -m \"$@\"" }
function gp {
    if [ "$#" -eq 0 ]; then
        echo "git push"
        eval "git push"
    else
        echo "git push \"$@\""
        eval "git push \"$@\""
    fi
}
function gn { ga; gc $@ }
function gt { ga; gc $@; git push }
function gfp {
	git remote add origin $@
	git branch -M master
	git push -u origin master
}

# Navigation shortcuts
alias home='cd ~'
alias desktop="cd ~/desktop"
alias documents="cd ~/documents"
alias images="cd ~/images"
alias downloads="cd ~/downloads"

# Programming shortcuts
alias programs='cd ~/Programs/'
alias website='cd ~/Programs/Website'
alias web='cd ~/Programs/Web'
alias javascript='cd ~/Programs/Web/Javascript'
alias canvas='cd ~/Programs/Web/Javascript/Canvas'
alias html='cd ~/Programs/Web/Html'
alias css="cd ~/Programs/Web/Css"
alias markdown="cd ~/Programs/Markdown"
alias wadjet='cd ~/Unity Games/Asteroids'
alias gitprojects="cd ~/git-projects"
alias brain="cd ~/programs/BrainPerformer"

# Quick temporary aliases
alias asteroids="cd ~/Programs/Web/Javascript/Canvas/Asteroids"

function p { cd ~/Programs/$@ }
function pj { cd ~/git-projects/$@ }
export programs=~/programs

# Python shortcuts
alias pip=pip3
alias py=python
alias activate="source env/bin/activate"
alias py20='cd ~/Programs/Python/Repository-2020'
alias pygames='cd ~/Programs/Python/Repository-Games'
alias pyml='cd ~/Programs/Python/Machine-Learning'
alias pyhome='cd ~/Programs/Python'
alias pypackages='cd /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/'
alias pypi='cd ~/Programs/Python/Pypi'

# Python programs
alias webpfix='py /Users/marcpartensky/Programs/Python/Repository-2020/webpfix.py'
alias glou="py /Users/marcpartensky/git-projects/Glou"
alias noscreenshots='python /Users/marcpartensky/Programs/Python/Repository-2020/no-screenshots.py'
alias video2gif='python /Users/marcpartensky/Programs/Python/Repository-2020/video2gif.py'
alias hyperplanning="python /Users/marcpartensky/programs/python/repository-2020/isep-hyperplanning.py"
alias portail="python /Users/marcpartensky/programs/python/repository-2020/isep-portal.py"

# Messenger
alias vivelescookies="chrome https://www.facebook.com/messages/t/1830795903602344"
alias alexandre="chrome https://www.facebook.com/messages/t/alexandre.partensky"
alias maman="chrome https://www.facebook.com/messages/t/pew.pradithja.1"
alias pierre="chrome https://www.facebook.com/messages/t/pierre.barthet.5"
alias bigot="chrome https://www.facebook.com/messages/t/alexandre.bgt.12"
alias valentin="chrome https://www.facebook.com/messages/t/valentin.colin.73"
alias samy="chrome https://www.facebook.com/messages/t/samy.haffoudhi"
alias paul="chrome https://www.facebook.com/messages/t/100009925413499"
alias arnaud="chrome https://www.facebook.com/messages/t/100013962188251"
alias etienne="chrome https://www.facebook.com/messages/t/etienne.faviere"
alias baptiste="chrome https://www.facebook.com/messages/t/100009848792300"
alias lovinsky="chrome https://www.facebook.com/messages/t/Skyns82"
alias maxime="chrome https://www.facebook.com/messages/t/100011382659168"
alias jp="chrome https://www.facebook.com/messages/t/jeanpascal.vostatek"
alias maximilien="chrome https://www.facebook.com/messages/t/maximilien.delagastine"
alias sacha="chrome https://www.facebook.com/messages/t/sacha.montassiet.1"
alias thibault="chrome https://www.facebook.com/messages/t/thibaut.moi"
alias philippe="chrome https://www.facebook.com/messages/t/100005499708371"
alias medhi="chrome https://www.facebook.com/messages/t/mehdi.haffoudhi.9"
alias hugues="chrome https://www.facebook.com/messages/t/hugues.rubin"
alias kevin="chrome https://www.facebook.com/messages/t/pandasus.pandasus.1"

# Applications
alias chrome="open -a 'Google Chrome' $1"
alias unity="open -a 'Unity'"
alias daisy="open -a 'DaisyDisk'"
alias terminal="open -a 'iTerm'"
alias postman="open -a 'Postman'"
alias keybr="chrome https://www.keybr.com/"
alias touch-typing="open -a 'Google Chrome' 'https://www.typingclub.com/sportal/program-3.game'"
alias change-extension="for file in *.$1; do mv '$file' '${file%.txt}.$2'; done"
function finder { open . }
function search { open -a 'Google Chrome' "https://www.google.com/search?q=$*" }
function youtube { open -a 'Google Chrome' "https://www.youtube.com/results?search_query=$1" }
alias yt=youtube
function messenger { open -a 'Google Chrome' "https://www.facebook.com/messages"; }
function messenger-terminal { exec "fb-messenger-cli"; }

alias youtube='cd /Volumes/\$/Youtube'

filename=""
function copy {
	filename=$1
	echo $filename is copied
	cat $1 | pbcopy
}

alias filename='echo $filename'

function paste {
	echo $filename is pasted
	pbpaste > $filename
}

# This is why being lazyness in programming even exists
function cheat { curl cheat.sh/"$@"; }

function compressgif {
    ffmpeg -i $1 -vf scale=320:-1 -r 10 -f image2pipe -vcodec ppm - | convert -delay 5 -loop 0 - $2
}
