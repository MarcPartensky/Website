class GameBase {
    static ticks = 1000
    constructor(ticks=GameBase.ticks) {
        this._ticks = ticks
        this.interval = undefined
    }
    update() {

    }
    start() {
        this.interval = setInterval(this.update.bind(this), this.ticks)
    }
    main() {
        this.start()
    }
}
