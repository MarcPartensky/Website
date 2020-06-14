class MeteorGroup extends Group {
    
    static meteorShower(n) {
        let wtf = [];
        for (let pas = 0; pas < n; pas++) {
            wtf.push(["meteor:"+pas, Meteor.random()]);
        }
        return new this(wtf);
    }
}



class Meteor extends GameEntity {
    static color = "#c50000";

    //m = new Motion(new Vector(1, 2))

    static fromVelocity(velocity) {
        // m = new Matrix()
        let form = new Polygon(
            new Matrix(
                new Vector( 1,  1),
                new Vector(-1,  1),
                new Vector(-1, -1),
                new Vector( 1, -1)
            )
        )
        // console.log(form)
        // [[1, 1],[-1, 1],[-1,-1],[1,-1]];
        // console.log(form)
        form.fill = true;
        let body = Body.random(2, 2, 2);
        // console.log(body)
        form.color = Meteor.color;
        body.velocity = velocity;
        return new this(form, body)
    }
    static random() {
        return this.fromVelocity(Vector.random());
    }


}