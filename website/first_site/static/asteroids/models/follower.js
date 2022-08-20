// Using strategy pattern for spaceships
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
