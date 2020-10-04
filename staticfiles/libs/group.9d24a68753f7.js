class Group extends Tree {
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