export default class Animation {
    static on = false;
    static state = 0;
    constructor(object, on=Animation.on, state=Animation.state) {
        this.object = object;
        this.on = on;
        this.state = state;
    }
    trigger() {
        this.on = true;
        this.start();
    }
    start() {

    }
    next() {

    }
    end() {

    }
    update(dt) {
        throw 'The update method of an animation must be implemented.'
    }
}


export class ColorChanger extends Animation {
    constructor(entity, state, colors) {
        super(entity, state);
        this.colors = colors;
    }
    get color() {
        const [c1, c2] = this.colors;
        const v1 = Color.toVector(c1);
        const v2 = Color.toVector(c2);
        const v = v1.rmul(1-this.state).add(v2.rmul(this.state));
        return Color.fromVector(v);
    }
    update(dt) {
        if (this.on) {
            if (this.state<1) {
                this.next()
            } else {
                this.end();
            }
        }
    }
    next() {
        this.state += dt;
        this.object.form.color = this.color;
    }
    end() {
        this.state = 0;
        this.on = false;
    }
}