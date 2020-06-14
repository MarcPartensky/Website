class Game extends Manager {
    update() {
        super.update();
        // follow one spaceship
        const player = this.group.get('spaceshipGroup').get('spaceship:0');
        this.context.plane.position = player.position;
        player.follow(this.context.fromScreen(this.mouse))
    }
}