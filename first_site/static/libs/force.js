class Force {
    static random(n) {
        return new this(Vector.random(n), Point.random(n))
    }
    constructor(vector, point) {
        this.vector = vector;
        this.point = point;
    }
    call(point) {
        return new this(this.vector, point);
    }
    next() {
        return this.vector.next();
    }
    get x() {
        return this.vector[0];
    }
    set x(value) {
        this.vector[0] = value;
    }
    get y() {
        return this.vector[1];
    }
    set y(value) {  
        this.vector[1] = value;
    }
    get z() {
        return this.vector[2];
    }
    set z(value) {
        this.vector[2] = value;
    }
    neg() {
        return new Force(this.vector.neg(), this.point);
    }
    add(force) {
        return new Force(this.vector.add(force.vector), this.point);
    }
    sub(force) {
        return this.add(force.neg());
    }
}