ping = 0;


class Player_ {
    constructor(id) {
            this.id  =  id;
    }
    
    join() {
                //ajoute le vaisseau de this dans le jeu
    }
    
    left() {
                //retire le vaisseau du joueur
    }
}



class socketClient {
        //se trouve côté server. Une instance de socketClient par onglet du jeu
    constructor(socket,gameServer) {
        this.socket = socket;
        this.player  = new Player(this.socket.id);//fabrication d'une instance Player pour notre client
        this.gameServer = gameServer;
    }

    connect() {
        //lancée quand l'objet se connecte au serveur
        this.player.join();
        this.registerPlayerEvent(this.player)

    }

    

    disconnect() { 
                //quand l'objet se déconnecte au serveur
        this.player.left();
    }
    
    initSocketAPI() {
        //permet de recevoir les commandes envoyée par le joueur
        if (this.player === undefined || this.player === null) {
            console.log("on essai de iniSocketAPI alors que le joueur est pas co :/");
        }
        // const player = this.player;
        this.socket.on("message", function (message) {
            console.log(message);
            this.socket.emit("message", message);
        });
    }

    registerPlayerEvent(player) {
        //permet d'annnoncer à tous les joueurs des updates
        const socket = this.socket;
        // const player = this.player;
        const myGameServer = this.gameServer;
        player.update.on("coordinatesUpdate", function (data) {
            //console.log("coordinatesUpdate event", data);
            myGameServer.sendAll("coordinatesUpdate", { uuid: player.id, coordinates: data.coordinates });
        });

        player.update.on("directionUpdate", function (data) {
            //console.log("directionUpdate event", data);
            myGameServer.sendAll("directionUpdate", { uuid: player.id, direction: data.direction });
        });

        player.update.on("unsummonPlayer", function (data) {
            myGameServer.sendAll("unsummonPlayer", { uuid: data.uuid });
        });

        player.update.on("summonPlayer", function (data) {
            myGameServer.sendAll("summonPlayer", { name: data.name, uuid: data.uuid, coordinates: data.coordinates });
        });


    }
    
    
    initInformPlayers() {
        //Permet d'informer le client quel est son vaisseau et informe touts les autres joueurs en ligne
        //qu'un nouveau joueur est connecté

        this.socket.emit("I choose you !", { your_uuid: this.player.id });
        
        for (let player of this.map.listPlayers) {
            console.log(`${player.id}`);
            if (player.id !== this.socket.id) {
                this.socket.emit("summonPlayer", { name: player.name, uuid: player.id, coordinates: player.coordinates })//todo
            }

        }
    }
    
    

}


class GameServer {
    constructor(game, io, dt=0.01) {
        this.game = game;
        this.dt = dt;
        this.socketList = {};
        this.io =  io;
    }

    setUp() {
        //A lancer lors du démarrage du server
        this.initUpdate();
        this.acceptConnection();
    }

    sendAll(event, message) {//todo utiliser les boradcasts https://socket.io/docs/#Broadcasting-messages
        for (let so_id in this.socketList) {//todo faire un truc async
            this.socketList[so_id].socket.emit(event, message);
        }

    }
    
    
    acceptConnection() {
        //demande au seveur d'accepter les connexions des clients
        this.io.sockets.on("connection", function (socket) {
            const id = socket.id;
            this.socketList[id] = new socketClient(socket, this);
            this.socketList[id].connection();
            socket.on("disconnect", function () {
                this.socketList[id].disconnect();
                delete this.socketList[id];
            });
        }.bind(this));
    }

    initUpdate() {
        //A lancer au lancement du serveur, permet d'informer les clients des dernières news
        this.game.on("Event Update News !!",  function (data)  {
            console.log("event caught by GameServer !!");
            this.sendAll("Update de la mort", { param1: "ciao les losers", param2: "toujours pour décrire l'update" });
        });
    }
    
    on() {
        this.io.sockets.on("connection", function (socket) {
            const id = socket.id;
            this.socketList[id] = new socketClient();
            this.socketList[id].connection();
            socket.on("disconnect", function () {
                this.socketList[id].disconnect();
                delete this.socketList[id];
            });
            let player = new Player(name);
            this.game.map.group.playerGroup.map.set(id, player);
            socket.emit("id", id);
            socket.on("player-spawn", function() {
                this.game.map.group.playerGroup.map.get(id).spawn();
                this.io.sockets.emit(
                    "map", 
                    JSON.stringify(this.game.map, Game.replacer)
                );
                console.log("map was emitted");
                console.log("player spawned")
            }.bind(this));
            socket.on("player-respawn", function() {
                this.game.map.group.playerGroup.map.get(id).spawn();
                console.log("player respawned")
            }.bind(this));
            socket.on("control-mousemove", function(position) {
                const direction = Vector.from(position);
                direction.limit(this.game.map.vmin, this.game.map.vmax);
                this.game.map.group.playerGroup.map.get(id).direction = direction;
            }.bind(this));
            socket.on("control-split", function(position) {
                player = this.game.map.group.playerGroup.map.get(id)
                player.split(Vector.from(position || player.direction));
            }.bind(this));
            socket.on('cache', function(cache) {
                cache = JSON.parse(cache, Game.reviver);
                this.game.map.group.handleCache(cache);
            }.bind(this));
            socket.on("message", function(message) {
                console.log(message);
            });
            socket.on('ping1', function() {
                ping+=1;
                socket.emit('pong');
            });
        }.bind(this));
    }
    update(io, ss) {
        this.game.update();
        this.game.map.group.collide();
        if (this.game.map.group.cache.size > 0) {
            io.sockets.emit(
                "cache",
                JSON.stringify(this.game.map.group.cache, Game.replacer)
            );
            this.game.map.group.cache.clear();
        }
        io.sockets.emit(
            "playerGroup", 
            JSON.stringify(this.game.map.group.playerGroup, Game.replacer)
        );
    }
    loop(io, ss) {
        this.update(io, ss);
    }
    start(io, ss) {
        console.log("starting the game");
        this.on(io);
    }
    main(io, ss) {
        this.start(io, ss);
        setInterval(this.loop.bind(this), this.dt*1000, io, ss);
    }
}