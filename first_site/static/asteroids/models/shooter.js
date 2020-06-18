// Using strategy pattern for spaceships
class Shooter {
    constructor(entity, types, selection=0) {
        this.entity = entity; // reference loop btw
        this.types = types;
        this.selection = selection;
        this.shooted = 0; // optional
        this.last_shooting = 0; // against shoot spam
    }
    get type() {
        return this.types[this.selection];
    }
    set type(v) {
        this.types[this.selection] = v;
    }
    shoot() {
        this.last_shooting = Date.now();
        this.shooted += 1;
        return this.type.make(this.entity);
    }
}