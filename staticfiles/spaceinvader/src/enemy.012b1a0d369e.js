class Enemy extends Entity {
    shoot() {
        const position = this.position.copy()
        return new Missile(
            new Segment(position.add(new Vector(0, .05)), position.add(new Vector(0, .1)), 1, 'orange'),
            new Body(new Motion(
                position.add(new Vector(0, .1)),
                new Vector(0, 0.2)
            ))
        )
    }
}
