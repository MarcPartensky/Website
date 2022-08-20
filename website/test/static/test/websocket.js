const websocket = new WebSocket('wss://test/websocket')

let message
while (message) {
	message = prompt('message:')
	websocket.send(JSON.stringify({
		'message': message
	}));
}
