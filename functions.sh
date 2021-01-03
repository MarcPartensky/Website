mkcdir()  {
    mkdir -p -- "$1" &&
      cd -P -- "$1"
}
alias mcd="mkcdir"
alias go="mkcdir"

alias startmamp='cd /Applications/MAMP/bin && ./start.sh'
alias stopmamp='cd /Applications/MAMP/bin && ./stop.sh'

function div {
  local _d=${3:-2}
  local _n=0000000000
  _n=${_n:0:$_d}
  local _r=$(($1$_n/$2))
  _r=${_r:0:-$_d}.${_r: -$_d}
  return $_r
}

# Ffmpeg
function speed-up {
	local n=$(python3 -c "print(1/$3)" 2>&1)
	ffmpeg -i $1 -filterv "setpts=$n*PTS" $2
}

filename=""
function copy {
	filename=$1
	echo $filename is copied
	cat $1 | pbcopy
}

function paste {
	echo $filename is pasted
	pbpaste > $filename
}

function search { open -a 'Google Chrome' "http://www.google.com/search?q=$1" }
alias chrome="open -a 'Google Chrome' $1";

alias daisy="open -a 'DaisyDisk'"

function youtube { open -a 'Google Chrome' "https://www.youtube.com/results?search_query=$1" }

function messenger { open -a 'Google Chrome' "https://www.facebook.com/messages"; }

function messenger-terminal { exec "fb-messenger-cli"; }

alias postman="open -a 'Postman'"

function spam {
	exec "messenger_terminal";
	exec "/search $1";
	exec "0";
	for i in {1...$3}
	do
		exec $2;
	done
}

function troll {
	sleep $1;
	for i in {1..$2}
	do
		osascript -e 'display notification "you are useless"'
		say "you are useless"
	done
}

alias touch-typing="open -a 'Google Chrome' 'https://www.typingclub.com/sportal/program-3.game'"

function speedtest {
	curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python -
}

function finder {
	open .
}

function dl-music {
	youtube-dl -ciw -x --audio-format "mp3" --audio-quality 0 -f bestaudio --embed-thumbnail -o '%(title)s.%(ext)s' --rm-cache-dir  $*
}

alias ytdl="youtube-dl -ciw -x --audio-format 'mp3' --audio-quality 0 -f bestaudio --embed-thumbnail -o '%(title)s.%(ext)s' --rm-cache-dir"

export YTOPTS="-ciw -x --audio-format 'mp3' --audio-quality 0 -f bestaudio --embed-thumbnail -o '%(title    )s.%(ext)s' --rm-cache-dir"

function weather {
	curl wttr.in
}
:
