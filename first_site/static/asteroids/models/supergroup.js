class SuperGroup extends Group {
    constructor() {
        super();
        this.set('asteroidGroup', AsteroidGroup.asteroidField(50, {x: 0, y: 0}, {x: 100, y: 100}));
        this.set("meteorGroup", MeteorGroup.meteorShower(100));
        this.set("spaceshipGroup", SpaceshipGroup.readyOnePlayer());

        // this.set('$gameMap', GameMap.fromSize(10,10));
        this.gameMap = GameMap.fromSize(100,100)
        
        //new AsteroidGroup([[1, Asteroid.random()], [2, Asteroid.random()]])

        // this.set('polygon', Polygon.random(5, 2, 100))
        // this.set('point', new Point(5, 0))
    }
    show(ctx) {
        super.show(ctx);
        this.gameMap.show(ctx);
    }
    update(dt) {
        super.update(dt);
        this.limit();
        
        // this.get('point').x += 1;
        // this.get('polygon').rotate(0.1, this.get('point'));
    }

    limit() {
        const entities = this.getAll();
        this.gameMap.limit(entities);
    }
}
