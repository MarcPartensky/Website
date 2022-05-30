class Force extends Vector {

}

class Moment extends VectorField {
    constructor(force) {
        this.force = force;
        this.f = (v => v.cross(force));
    }
    call(vector) {
        return this.f(vector);
    }
}