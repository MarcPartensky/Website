class Life {
    constructor(value, max) {
        this.value = value;
        this.max = max;
    }
    isAlive() {
        return this.value > 0;
    }
    regen() {
        this.value = this.max;
    }
}