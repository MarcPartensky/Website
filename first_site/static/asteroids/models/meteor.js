class Meteor extends GameEntity {
    static color = "#c50000";

    //m = new Motion(new Vector(1, 2))
    static fromVelocity(velocity) {
        let form = new Square(-1, -1, 2);
        form.fill = true;
        let body = Body.random(2, 2, 2);
        form.color = Meteor.color;
        body.velocity = velocity;
        return new this(form, body)
    }
    static random() {
        return this.fromVelocity(Vector.random());
    }


}