class GameClient extends Manager {
    static movement = {up: false, down: false, right: false, left: false, zoomin: false, zoomout: false};
    static backgroundColor = "#000000";

    constructor(
        canvas,
        game,
        socket,
    ) {
        super(canvas, game)
        this.socket = socket;
    }
    on() {
        this.socket.on("id", function(id) {
            this.id = id;
            console.log("id", this.id);
        }.bind(this));
        this.socket.on("game", function(game) {
            this.game = game;
            console.log("game sent", game);
        }.bind(this));
        this.socket.on("map", function(stream) {
            this.game.map = JSON.parse(stream, Game.reviver);
            console.log("map");
        }.bind(this));
        this.socket.on("test", function(message) {
            console.log(message);
        }.bind(this));
        this.socket.on("playerGroup", function(stream) {
            this.game.map.group.playerGroup = JSON.parse(stream, Game.reviver);
        }.bind(this));
        this.socket.on("superGroup", function(stream) {
            this.game.map.group = JSON.parse(stream, Game.reviver);
        }.bind(this));
        this.socket.on("cache", function (cache) {
            console.log("cache detected")
            cache = JSON.parse(cache, Game.reviver);
            this.game.map.group.handleCache(cache);
        }.bind(this));
    }
    get player() {
        const player = this.game.group.get('spaceshipGroup').get('spaceship:0');
        return player;
    }
    show() {
        super.show();
        const player = this.player;
        if (player) {
            this.context.plane.position = player.position;
        }
    }
    update() {
        const player = this.player;
        player.follow(this.context.fromScreen(this.mouse))
        super.update()
    }
    onKeyDown(e) {
        super.onKeyDown(e);
        if (e.code=='Space') {
            this.game.group.get('missileGroup').add(this.player.shoot());
        }
    }
    //     let player = this.game.map.group.playerGroup.map.get(this.id);
    //     if (player) {
    //         if (!player.alive) {
    //             console.log("you are dead");
    //             this.socket.emit("player-respawn");
    //         }
    //     }
        
    //     if ('id' in this) {
    //         this.game.map.group.collideClient(this.id);
    //     }
    //     if (this.game.map.group.cache.size>0) { // could overrun the server
    //         this.socket.emit(
    //             "cache",
    //             JSON.stringify(this.game.map.group.cache, Game.replacer)
    //         );
    //         this.game.map.group.cache.clear();
    //     }
    //     this.socket.emit("control-mousemove", this.context.fromScreen(this.mouse));
    // }    
}