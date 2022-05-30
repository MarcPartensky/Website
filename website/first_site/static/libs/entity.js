class Entity {
    static random(form_args, body_args) {
        const form = Polygon.random(form_args);
        const body = Body.random(body_args);
        return new this(form, body);
    }
    constructor(form, body) {
        this.form = form;
        this.body = body;
    }
    get position() {
        return this.body.position;
    }
    set position(position) {
        this.body.position = position;
    }
    get angle() {
        return this.body.angle;
    }
    set angle(angle) {
        this.body.angle = angle;
    }
    update(dt) {
        this.body.update(dt);
        this.form.angle = this.body.angle;
        this.form.center = this.body.position;
    }
    show(ctx) {
        this.form.show(ctx);
    }
}