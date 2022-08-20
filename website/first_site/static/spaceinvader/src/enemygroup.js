class EnemyGroup extends Group {
    applyBorder(xb, yb, wb, hb) {
        const positions = Array.from(game.level.group.get('enemyGroup').values()).map(enemy=>enemy.position)
        const xmin = Math.min(...positions.map(v=>v.x))
        const ymin = Math.min(...positions.map(v=>v.y))
        const xmax = Math.max(...positions.map(v=>v.x))
        const ymax = Math.max(...positions.map(v=>v.y))
        if (xmax > wb || xmin < xb) {
            for (const enemy of this.values()) {
                enemy.velocity.x = -enemy.velocity.x
            }
        }
        if (ymax > yb || ymin < yb) {
            for (const enemy of this.values()) {
                enemy.velocity.y = -enemy.velocity.y 
            }
        }
    }
    shoot() {
        const missiles = []
        for (const enemy of this.values()) {
            if (Math.random() < 0.01) {
                missiles.push(enemy.shoot())
            }
        }
        return missiles
    }
}
