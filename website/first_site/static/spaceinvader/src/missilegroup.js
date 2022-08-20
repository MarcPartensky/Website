class MissileGroup extends Group {
    constructor(...args) {
        super(...args)
        this.counter = 0
    }
    append(missile) {
        this.counter += 1
        this.set(
            this.counter,
            missile
        )
    }
    extend(missiles) {
        for (const missile of missiles) {
            this.append(missile)
        }
    }
    applyBorder(xb, yb, wb, hb) {
        const toDestroy = []
        for (const [key, missile] of this) {
            if (missile.x < xb || missile.x > wb)
                toDestroy.push(key)
            else if (missile.y < yb || missile.y > hb)
                toDestroy.push(key)
        }
        for (const key of toDestroy) {
            this.delete(key)
        }
    }
}
