class MissileGroup extends Grouper(Missile) {
    removeDeads() {
        const deads = []
        for (const [k,v] of this) {
            if (v.removing) {
                deads.push(k)
            }
        }
        for (const dead of deads) {
            this.delete(dead)
        }
    }
    update(dt) {
        super.update(dt);
        this.removeDeads()
    }
    add(missile) {
        this.set(
            MissileGroup.type.name+MissileGroup.separator+MissileGroup.n,
            missile
        );
        MissileGroup.n += 1;
    }
}