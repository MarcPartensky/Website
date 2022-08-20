// Cool explosion when the missiles hit something.

class Explosion extends ColorChanger {
    constructor() {
        
    }
    end() {
        super.end();
        this.object.removing = true;
    }
}