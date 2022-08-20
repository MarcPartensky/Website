const roomName = document.location.pathname.split('/').pop()

if (window.location.protocol == "https:") {
	var ws_scheme = "wss://"
} else {
	var ws_scheme = "ws://"
}

const socket = new WebSocket(
		ws_scheme
		+ window.location.host
		+ '/ws/code/'
		+ roomName
		+ '/'
)

socket.onmessage = function(e) {
	const data = JSON.parse(e.data)
	editor.setValue(data.message)
}.bind(code)

socket.onclose = function(e) {
	console.error('Code socket closed unexpectedly')
}

editor.focus()
// code.onkeyup = function(e) {
// 	if (e.keyCode === 13) {  // enter, return
// 		document.querySelector('#chat-message-submit').click()
// 	}
// }

editor.on('keyup', function(e) {
	console.log('changing editor')
	socket.send(JSON.stringify({
			'message': editor.getValue()
	}))
}.bind(socket))
