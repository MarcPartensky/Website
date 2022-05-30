/*
* Abstraction of an array for better writting.
*/
class Group extends Array {
    constructor(...elements) {
        super(...elements);
    }
    copy() {
        return new Group(...this);
    }
    empty() {
        this.length = 0;
    }
    set(other) {
        Object.assign(this, other);
    }
    imap(f) {
        this.set(this.map(f));
    }
}

class Tree extends Group {
    constructor(...trees) {
        super(...trees);
    }
    copy() {
        return new Tree(...this);
    }
    irmap(f) {
        if (this[0] instanceof Tree) {
            for (const tree of this) {
                tree.irmap(f);
            }
        } else {
            this.imap(f);
        }
    }
    rmap(f) {
        const t = this.copy();
        t.irmap(f);
        return t;
    }
}
