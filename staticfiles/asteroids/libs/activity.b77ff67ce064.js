class Activity {
    constructor(components) {
        this.components = components;
    }
    show(context) {
        for(const component of this.components) {
            component.show(context);
        }
    }
    update(dt) {
        for(const component of this.components) {
            component.update(dt);
        }
    }
}
