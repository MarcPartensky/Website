class Life {
    static value = 1;
    static max = 1;
    constructor(value=Life.value, max=Life.max) {
        this.value = value;
        this.max = max;
        // It doesn't matter where the lifebar is
        // because it only matters when showing it.
        this.bar = new LifeBar();
    }
    isAlive() {
        return this.value > 0;
    }
    regen() {
        this.value = this.max;
    }
    show(ctx, position) {
        this.bar.show(ctx, position, this.value/this.max);
    }
}

class LifeBar extends Rectangle {
    static areaColor = "lightgreen";
    static borderColor = "white";
    static margin = 2;
    static position = [0,0];
    static size = [3, 0.5];
    static lineWidth = 0.1;
    // defining new default arguments
    constructor(
        position=LifeBar.position,
        size=LifeBar.size,
        color=undefined,
        lineWidth=LifeBar.lineWidth,
        fill=undefined,
    ) {
        super(position, size, color, lineWidth, fill);
    }
    // the order of the operations is very important
    show(ctx, position, ratio, margin=LifeBar.margin) {
        this.center = position.sub(new Vector(0, -margin));
        const w = this.w;
        this.w *= ratio;
        this.color = LifeBar.areaColor;
        this.fill = true;
        super.show(ctx)
        this.w = w;
        this.color = LifeBar.borderColor;
        this.fill = false;
        super.show(ctx);
    }
}