class Player extends Entity {
    constructor(...args) {
        super(...args)
        this.life = 1
    }
    applyBorder(x, y, w, h) {
        this.position[0] = Math.max(x, this.position[0])
        this.position[0] = Math.min(w, this.position[0])
        this.position[1] = Math.max(y, this.position[1])
        this.position[1] = Math.min(h, this.position[1])
    }
    shoot() {
        const position = this.position.copy()
        return new Missile(
            new Segment(position.add(new Vector(0, -.05)), position.add(new Vector(0,-.1)), 1, 'yellow'),
            new Body(new Motion(
                position.add(new Vector(0, -.1)),
                new Vector(0, -0.2)
            ))
        )
    }
    show(context) {
        super.show(context)
        this.showLife(context)
    }
    showLife(context) {
        let rectangle = Rectangle.of(
            this.x-0.025, this.y+0.05,
            0.05, 0.0005, 0.02
        )
        rectangle.show(context)
        rectangle = Rectangle.of(
            this.x-0.025, this.y+0.05,
            this.life*0.05, 0.0005,
            0.01, 'green'
        )
        rectangle.show(context)
    }
}
