class Follower { 
    orientate(body, form) {
        //tourne le Follower vers sa vitesse
        form.angle = body.velocity.angle;
    }
    
    follow(body, position, velocityNorm) {
        //change l'acceleration du Follower en fonction de la position donnée
        const velocityFollower = position.sub(body.p);
        velocityFollower.norm = velocityNorm;
        body.velocity = velocityFollower;
    }
}

class SpaceshipGroup extends Group {

    static readyOnePlayer(){
        const s = Spaceship.random()
        return new this([["spaceship:0",s]]);
    }

    constructor(g){
        super(g);
    }
}

class Spaceship extends Entity {
    static color="#ef6c00";//du orange
    static initFuel=1000;
    static dashVelocityNorm=2;
    static velocityNorm=1;

    static random() {
        const body = Body.random(1, 3, 2);
        const form = new Polygon([[4,0],[-2,2],[-1,0],[-2,-2]]);//triangle regardant vers la droite
        form.center = Vector.zero(2);
        const follower = new Follower();
        return new this(form, body, follower);
    }

    constructor(form, body, follower) {
        super(form, body);
        form.fill=true;
        form.color=Spaceship.color;
        this.follower = follower;
        this.fuel=Spaceship.initFuel;
        this.isDashing=false;
    }

    startDash(){
        //Commence un dash s'il reste du fuel
        this.isDashing=this.fuel>0;

    }
    
    endDash(){
        //Termine un dash et remet la vitesse à la normale
        this.isDashing=false;
        this.velocity.norm=Spaceship.velocityNorm;
    }

    
    update(dt) {
        this.body.updateFriction(0.1);
        if (this.isDashing){
            if (this.fuel>=dt){
                this.fuel+=-dt;
                this.velocity.norm=Spaceship.dashVelocityNorm;
            }else{
                this.isDashing=false;
                this.velocity.norm=Spaceship.velocityNorm;
            }
        }
        this.follower.orientate(this.body, this.form);
        super.update(dt);
                //this.follower.follow(this.body, position);
        //this.follower.follow(this.body, new Vector(10,0));
        
    }
    follow(position) {
        this.body.follow(position);
        // this.follower.follow(this.body, position, 4);
    }
    show(ctx) {
        super.show(ctx);
        this.body.motion.show(ctx);
    }
}
