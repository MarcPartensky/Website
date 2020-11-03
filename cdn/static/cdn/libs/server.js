export default class Server extends Connexion {
    constructor() {
        

    }
}

const express = require('express'),
    app = express(),
    server = require('http').createServer(app),
    io = require('socket.io').listen(server),
    ent = require('ent'), // Permet de bloquer les caractères HTML (sécurité équivalente à htmlentities en PHP)
    os = require('os');

server.maxConnections = 2;

app.use(express.static('public'));
app.get('/', function (req, res) {
  res.sendFile(__dirname + "/index.html");
});


io.sockets.on('connection', function (socket, pseudo) {
    // Dès qu'on nous donne un pseudo, on le stocke en variable de session et on informe les autres personnes
    socket.on('nouveau_client', function(pseudo) {
        
    }
}
