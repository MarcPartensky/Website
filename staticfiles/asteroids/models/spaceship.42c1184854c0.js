// Using strategy pattern is used
class Spaceship extends Entity {
    static color = "#ef6c00";//du orange
    static initFuel = 1000;
    static extraDashVelocityNorm = 2;
    static afterDashVelocityNorm = 1;
    static dashing = false;
    static dashDuration = 2;

    static random() {
        const body = Body.random(1, 3, 2);
        const form = new Polygon([[4,0],[-2,2],[-1,0],[-2,-2]]);//triangle regardant vers la droite
        form.color = Spaceship.color;
        form.fill = true;
        form.center = Vector.zero(2);
        return new this(form, body);
    }

    constructor(
        form,
        body,
        life = new Life(),
        shooter = undefined,
        follower = new Follower(),
        fuel = Spaceship.initFuel,
        dashing = Spaceship.dashing, // dashing should have its own class using strategy pattern (dasher.js)
        dashDuration = Spaceship.dashDuration
    ) {
        super(form, body);
        this.life = life
        this.shooter = shooter || new Shooter(this, [Missile]);
        this.follower = follower;
        this.dashing = dashing;
        this.dashTime = 0;
        this.dashDuration = dashDuration;
        this.fuel = fuel; // We'd be better of only using time instead of fuel
    }
    canDash() {
        return Date.now() - this.dashTime > this.dashDuration;
    }

    startDash(){
        //Commence un dash s'il reste du fuel
        this.dashing = this.fuel>0;
        this.dashTime = Date.now();
        this.velocity.norm = this.velocity.norm + this.extraDashVelocityNorm;
    }
    endDash(){
        //Termine un dash et remet la vitesse à la normale
        this.dashing = false;
        this.velocity.norm = Spaceship.afterDashVelocityNorm;
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
    shoot() {
        return this.shooter.shoot();
    }
    follow(position) {
        this.body.follow(position);
        // this.follower.follow(this.body, position, 4);
    }
    show(ctx) {
        super.show(ctx);
        this.life.show(ctx, this.position);
        this.body.motion.show(ctx);
    }
}