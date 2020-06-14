class AsteroidGroup extends Group {
    static n = 50;
    static asteroidField(numberAst=AsteroidGroup.n, centerPosition, dimension) {
        let listDelist=[];
        let id, ast;
        for (let pas = 0; pas < numberAst; pas++) {
            ast = Asteroid.random();
            ast.x = centerPosition.x + (Math.random() * dimension.x)/2;
            ast.y = centerPosition.y + (Math.random() * dimension.y)/2;
            id = "asteroid:"+pas;
            listDelist.push([id,ast])
        }
        return new this(listDelist);
    }
    constructor(g) {
        super(g);
        this.spread(100);
    }
    spread(n) {
        for (const v of this.values()) {
            v.position.angle = 2*Math.PI * Math.random();
            v.position.norm = n*Math.random();
        }
    }
    removeDeads() {
        const deads = []
        for (const [k,v] of this) {
            if (v.removing) {
                deads.push(k)
            }
        }
        for (const dead of deads) {
            this.delete(dead)
        }
    }
    update(dt) {
        super.update(dt);
        this.removeDeads()
    }
    selfDestruction() {
        this.clear();
    //Détruit tous les asteroids du groupe
    }

    
}
