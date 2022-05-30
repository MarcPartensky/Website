class Group extends Tree {
    // type of the entities of the group    
    static type = undefined;
    // number of entites created (usefull for making ids)
    static n=0;
    // separator for naming entities
    static separator = ":";

    static of(items) {
        const group = new this(items);
        group.type = this.type;
        return group;
    }

    static random(n, args=[]) {
        const g = new this();
        for (let i=0; i<n; i++) {
            g.set(this.type.name.toLowerCase()+this.separator+this.n, this.type.random(...args));
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
    take(key) {
        return this.get(this.constructor.type.name.toLowerCase()+this.constructor.separator+key);
    }
    add(key, value) {
        this.set(this.constructor.type.name.toLowerCase()+this.constructor.separator+key, value);
    }
    remove(key) {
        this.delete(this.constructor.type.name.toLowerCase()+this.constructor.separator+key);
    }
    getBodies() {
        const bodies = [];
        for (const [k,v] of this) {
            if (v instanceof Group) {
                bodies.push([k, v.getBodies()]);
            } else {
                bodies.push([k, v.body]);
            }
        }
        return bodies;
    }
    setBodies(bodies) {
        for (const [k,v] of bodies) {
            if (v[0] instanceof String) {
                this.get(k).setBodies(v);
            } else {
                this.get(k).body.rset(v);
            }
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
