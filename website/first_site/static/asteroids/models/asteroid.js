class AsteroidForm extends Polygon {
    static color = "#3f87a6";
    static w = 2;
    static fill = true;
    static maxPoints = 8;
    static minPoints = 3;
    static size = 1;
    static random(color=AsteroidForm.color, fill=Asteroid.fill) {
        const n = Math.floor((AsteroidForm.maxPoints-AsteroidForm.minPoints)*Math.random())+AsteroidForm.minPoints;
        const p = Polygon.random(n, 2, 10);
        return new this(p.matrix, color, p.width, fill);
    }
}

class Asteroid extends Entity {
    static color = "#3f87a6";
    static w = 5;
    static riskOfSelfDestruction  = 0.00005;
    static rotation = 0.1;
    static movement = 0.1;
    static random() {
        const form = AsteroidForm.random()
        form.fill = true;
        const body = new Body(
            Motion.random(2, 2).rsub(1/2).rmul(2), // values between 0 and 1
            Motion.random(2, 1).rsub(1/2).rmul(2)
        );
        body[0][1].irmul(Asteroid.rotation); // reducing velocity
        body[1][1].irmul(Asteroid.movement); // reducing angular velocity
        return new this(form, body)
    }
    update(dt) {
        super.update(dt);
        this.form.angle = this.body[1][0][0]; // setting form angle
        // the form position is already dealt with
        if (Math.random() <= dt * Asteroid.riskOfSelfDestruction) {
            console.log("Explosion imminente !!!!");
            this.selfDestruction();
        }
    }
    selfDestruction() {
        //silly way of destroying an asteroid
        return this.removing=true;
    }
}