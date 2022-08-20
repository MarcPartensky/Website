class SpaceshipGroup extends Grouper(Spaceship) {
    static type = Spaceship;
    static readyOnePlayer(){
        const s = Spaceship.random()
        return new this([["spaceship:0",s]]);
    }
    addSpaceship(idSpaceship, spaceshipObject) {
       //Ajoute le spaceship spaceshipObject dans le groupe this avec l'id idSpaceship
        this.push([[`spaceship:${idSpaceship}`,spaceshipObject]])
    }
}