class Entity {
    static random(form_args=[], body_args=[]) {
        const form = Polygon.random(...form_args);
        const body = Body.random(...body_args);
        return new this(form, body);
    }
    constructor(form, body) {
        this.form = form;
        this.body = body;
    }
    update(dt) {
        this.body.update(dt);
        // if (this.body.length==1) {
        //     console.log(this.form, this.body)
        //     this.form.angle = this.body[0][1].angle;
        // }
        // else if (this.body.length==2) {
        //     this.form.angle = this.body.angle;
        // }
        // console.log(this.form, this.body)
        this.form.center = this.body.position;
    }
    show(ctx) {
        this.form.show(ctx);
        // this.hitBox.show(ctx);
        // this.hitBubble.show(ctx);
    }
    get motion() {
        return this.body[0];
    }
    set motion(v) {
        this.body[0].set(v);
    }
    get angularMotion() {
        return this.body[1];
    }
    set angularMotion(v) {
        this.body[1].set(v);
    }
    get x() {
        return this.body[0][0][0];
    }
    set x(v) {
        this.body[0][0][0] = v;
    }
    get y() {
        return this.body[0][0][1];
    }
    set y(v) {
        this.body[0][0][1] = v;
    }
    get z() {
        return this.body[0][0][2];
    }
    set z(v) {
        this.body[0][0][2] = v;
    }
    get vx() {
        return this.body[0][1][0];
    }
    set vx(v) {
        this.body[0][1][0].set(v);
    }
    get ax() {
        return this.body[0][1][2];
    }
    set ax(v) {
        this.body[0][1][2].set(v);
    }
    get position() {
        return this.body[0][0];
    }
    set position(v) {
        this.body[0][0].set(v);
    }
    get p() {
        return this.body[0][0];
    }
    set p(v) {
        this.body[0][0].set(v);
    }
    get velocity() {
        return this.body[0][1];
    }
    set velocity(v) {
        this.body[0][1].set(v);
    }
    get velocity() {
        return this.body[0][1];
    }
    set velocity(v) {
        this.body[0][1].set(v);
    }
    get angle() {
        return this.body.angle;
    }
    set angle(angle) {
        this.body.angle = angle;
    }
    get hitBox() {
        return this.form.hitBox;
    }
    get hitBubble() {
        return this.form.hitBubble;
    }
}
