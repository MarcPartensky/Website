class AsteroidForm extends Polygon {
    static color = "#3f87a6";
    static w=2;
    static fill=true;
    static maxPoints = 8;
    static minPoints = 3;
    static size = 1;
    static random(color=AsteroidForm.color, fill=Asteroid.fill) {
        const n = Math.floor((AsteroidForm.maxPoints-AsteroidForm.minPoints)*Math.random())+AsteroidForm.minPoints;
        console.log('polygon.random')
        const p = Polygon.random(n);
        // const p = new Polygon(
        //     new Matrix(
        //         new Vector(0, 1),
        //         new Vector(1, 0),
        //         new Vector(-1, 0)
        //     )
        // )
        // console.log('polygon:', p)
        return new this(p.matrix, color, p.width, fill);
    }
}

class Asteroid extends Entity {
    static color = "#3f87a6";
    static w = 5;
    static riskOfSelfDestruction  = 0.000005;
    static rotation = 0.1;
    static random() {
        const form = AsteroidForm.random()
        form.fill = true;
        const body = Body.random(1, 1, 2);
        return new this(form, body)
    }
    update(dt) {
        super.update(dt);
        // console.log(dt*Asteroid.rotation)
        // console.log(this.form)
        this.form.rotate(dt*Asteroid.rotation)
        // console.log(this.form)
        if (Math.random() * dt <= Asteroid.riskOfSelfDestruction) {
            console.log("Explosion imminente !!!!");
            this.selfDestruction();
        }
    }
    selfDestruction() {
            //détruit l'Asteroid
        return this.removing=true;
    }

}