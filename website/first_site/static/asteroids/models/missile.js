class Missile extends GameEntity {
    static size = 3;
    static duration = 1000/10; // mili-seconds
    static velocityBoost = 5;
    static random(
        source=undefined,
        target=undefined
    ) {
        return new this(
            new Segment([0, 0], [0, Missile.size]),
            Body.random(1, 2),
            source,
            target
        );
    }
    static make(
        source,
        target=undefined,
        duration=Missile.duration
    ) {
        const body = new Body(source.body[0].slice(0, 2).copy());
        body[0][1].norm += this.velocityBoost;
        return new this(
            new Segment([0, 0], [0, Missile.size]),
            body,
            source,
            target,
            duration
        );
        
    }
    constructor(
        form,
        body,
        source=undefined,
        target=undefined,
        duration=Missile.duration,
    ) {
        super(form, body);
        this.source = source;
        this.target = target;
        this.duration = duration;
        this.time = undefined;
    }
    update(dt) {
        if (!this.time) {
            this.time = Date.now()
        }
        if (!this.isAlive(dt)) {
            this.removing = true;
        }
        this.form.angle = this.body[0][1].angle;
        super.update(dt);
    }
    get left() {
        return Date.now() - this.time;
    }
    isAlive(dt) {
        return this.left*dt<this.duration;
    }
}