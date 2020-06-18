// GameClient   => Game => SuperGroup => ...
//                      => GameMap
//              => Context

// GameServer   => Game => SuperGroup => ...
//                      => GameMap

class Game {
    // Making a getter is memory friendly
    // and it doesn't matter that we can't
    // change the result.
    static get gameMap() {
        return GameMap.fromSize(100,100);
    }
    static random() {
        return new this(
            SuperGroup.random()
        );
    }
    constructor(
        group = new SuperGroup(), // this super group is empty
        gameMap = Game.gameMap
    ) {
        this.group = group;
        this.gameMap = gameMap;
    }
    update(dt) {
        this.group.update(dt);
        this.limit();
    }
    show(ctx) {
        this.gameMap.show(ctx);
        this.group.show(ctx);
    }
    limit() {
        const entities = this.group.getAll();
        this.gameMap.limit(entities);
    }
}