class Level {
    show(context) {
        this.group.show(context)
        this.border.show(context)
        this.line.show(context)
    }
    update(dt) {
        this.group.update(dt)
        this.applyBorder()
        this.group.get('enemyMissileGroup').extend(
            this.group.get('enemyGroup').shoot()
        )
        this.checkCollisions()
        this.checkGameOver()
    }
    checkGameOver() {
        if (this.isWon())
            this.over = true
        else if (this.isLost())
            this.over = true
    }
    isWon() {
        return this.group.get('enemyGroup').size == 0
    }
    isLost() {
        return this.group.get('player').life <= 0
    }
    applyBorder() {
        this.group.get('player').applyBorder(0, .7, 1, 1)
        this.group.get('enemyGroup').applyBorder(0, 0, 1, 1)
        this.group.get('enemyMissileGroup').applyBorder(0, 0, 1, 1)
        this.group.get('playerMissileGroup').applyBorder(0, 0, 1, 1)
    }
    checkCollisions() {
        this.checkCollisionsBetweenEnemysAndPlayerMissiles()
        this.checkCollisionsBetweenPlayerAndEnemyMissiles()
    }
    checkCollisionsBetweenEnemysAndPlayerMissiles() {
        const missileKeysToDestroy = []
        const enemyKeysToDestroy = []
        for (const [missileKey, missile] of this.group.get('playerMissileGroup')) {
            for (const [enemyKey, enemy] of this.group.get('enemyGroup')) {
                if (enemy.form.contains(missile.form.p1)) {
                    missileKeysToDestroy.push(missileKey)
                    enemyKeysToDestroy.push(enemyKey)
                } else if (enemy.form.contains(missile.form.p2)) {
                    missileKeysToDestroy.push(missileKey)
                    enemyKeysToDestroy.push(enemyKey)
                }
            }
        }
        for (const missileKey of missileKeysToDestroy) {
            this.group.get('playerMissileGroup').delete(missileKey)
        }
        for (const enemyKey of enemyKeysToDestroy) {
            this.group.get('enemyGroup').delete(enemyKey)
        }
    }
    checkCollisionsBetweenPlayerAndEnemyMissiles() {
        const missileKeysToDestroy = []
        const player = this.group.get('player')
        for (const [missileKey, missile] of this.group.get('enemyMissileGroup')) {
            if (player.form.contains(missile.form.p1)) {
                missileKeysToDestroy.push(missileKey)
                player.life -= missile.damage
            } else if (player.form.contains(missile.form.p2)) {
                missileKeysToDestroy.push(missileKey)
                player.life -= missile.damage
            }
        }
        for (const missileKey of missileKeysToDestroy) {
            this.group.get('enemyMissileGroup').delete(missileKey)
        }
    }
}
