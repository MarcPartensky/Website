class Game {
    constructor(ticks) {
        this.ticks = ticks
        this.interval = undefined
    }
    update() {

    }
    start() {
        this.interval = setInterval(this.update.bind(this), this.ticks)
    }
}
