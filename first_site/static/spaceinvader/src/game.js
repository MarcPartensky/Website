class Game extends GameClient {
    static dt = 0.01
    constructor(ticks, context, levels=[], dt=Game.dt) {
        super(ticks, context)
        this.levels = levels
        this.levelIndex = 0
        this.level = new this.levels[this.levelIndex]
        this.dt = dt
        this.over = false
    }
    show() {
        super.show()
        this.level.show(this.context)
    }
    onKeyDown(evt) {
        super.onKeyDown(evt)
        switch(evt.key) {
            case 'a':
                break;
        }
    }
    update() {
        super.update()
        if (!this.level.over) {
            this.level.update(this.dt)
        } else if (this.level.isLost()) {
            this.level = new this.levels[this.levelIndex]
        } else if (this.levelIndex < this.levels.length-1){
            this.levelIndex += 1
            this.level = new this.levels[this.levelIndex]
        } else if (!this.over) {
            this.over = true
            alert('You won!')
        }
    }
  onKeyDown(evt) {
    if (evt.keyCode==39) // Arrow Right for moving right
            this.level.group.get('player').velocity[0] = 0.5;
    if (evt.keyCode==37) // Arrow Left for moving left
            this.level.group.get('player').velocity[0] = -0.5;
    if (evt.keyCode==40) // Arrow Up for moving up
            this.level.group.get('player').velocity[1] = 0.5;
    if (evt.keyCode==38) // Arrow Down for moving down
            this.level.group.get('player').velocity[1] = -0.5;
    if (evt.keyCode==18) {// Alt for pause
        if (this.dt) {
            this.dt = 0;
        } else {
            this.dt = Game.dt;
        }
    }
    if (evt.keyCode==32)
      this.level.group.get('playerMissileGroup').append(
          this.level.group.get('player').shoot()
      )
     }
  onKeyUp(evt) {
    if (evt.keyCode==39) // Arrow Right for moving right
        this.level.group.get('player').velocity[0] = 0;
    if (evt.keyCode==37) // Arrow Left for moving left
        this.level.group.get('player').velocity[0] = 0;
    if (evt.keyCode==40) // Arrow Up for moving up
        this.level.group.get('player').velocity[1] = 0;
    if (evt.keyCode==38) // Arrow Down for moving down
        this.level.group.get('player').velocity[1] = 0;
  }
}
