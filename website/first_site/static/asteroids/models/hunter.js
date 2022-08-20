// Using strategy pattern for spaceships
class Hunter {
    constructor(spaceship, target=undefined) {
        this.spaceship = spaceship;
        this.target = target;
    }
    hunt() {
        this.spaceship.follow(this.target.center);
    }
}