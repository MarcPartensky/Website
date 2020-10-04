class Group extends Tree {
    // type of the entities of the group    
    static type = undefined;
    // number of entites created (usefull for making ids)
    static n=0;
    // separator for naming entities
    static separator = ":";

    static random(n, args=[]) {
        const g = new this();
        for (let i=0; i<n; i++) {
            g.set(this.type.name+this.separator+this.n, this.type.random(...args));
            this.n += 1;
        }
        return g;
    }
    show(ctx) {
        for (const v of this.values()) {
            v.show(ctx);
        }
    }
    update(dt) {
        for (const v of this.values()) {
            v.update(dt);
        }
    }
}



// A function that returns a class with a
// predefined type
function Grouper(type) {
    class SubGroup extends Group {} // Just here to bypass a bug
    const g = SubGroup.bind({});
    g.type = type;
    return g;
}