class GameClient extends GameBase {
  static movement = {up: false, down: false, right: false, left: false, zoomin: false, zoomout: false};
  static zoomDelta = 0.1;
  static scrollZoomFactor = 0.5;
  static backgroundColor = "#000000";
    constructor(
        ticks,
        canvas,
        eventListeners=[],
        movement=GameClient.movement, 
        backgroundColor=GameClient.backgroundColor
    ) {
        super(ticks)
        this.canvas = canvas
        this.eventListeners = eventListeners 
        this.backgroundColor = backgroundColor
        this.mouse = new Vector(0, 0)
        this.movement = movement
        this.context = new ContextAdapter(this.canvas.getContext('2d')) 
    }
    get ticks() {
        return this._ticks
    }
    set ticks(number) {
        this._ticks = number 
        clearInterval(this.interval)
        this.interval = setInterval(this.update.bind(this), number)
    }
    start() {
        this.deactivate()
        this.addEventListeners()
        this.resize()
        this.interval = setInterval(this.update.bind(this), this.ticks)
    }
    addEventListeners() {
        this.eventListeners= [
            window.addEventListener("keydown", this.onKeyDown.bind(this)),
            window.addEventListener("keyup", this.onKeyUp.bind(this)),
            this.canvas.addEventListener("mousemove", this.onMouseMotion.bind(this)),
            this.canvas.addEventListener("scroll", this.onScroll.bind(this)),
            this.canvas.addEventListener("mousewheel", this.onScroll.bind(this)),
            this.canvas.addEventListener("resize", this.resize.bind(this))
        ]
    }
    removeEventListeners() {
        for (const eventListener of this.eventListeners) {
            removeEventListener(eventListener)
        }
        this.eventListeners = [];
    }
    stop() {
        clearInterval(this.interval)
    }
    restart() {
        this.interval = setInterval(this.update.bind(this), this.ticks)
    }
    destroy() {
        this.stop()
        this.removeEventListeners()
    }

    clear() {
        this.context.fillStyle = this.backgroundColor
        this.context.clear()
    }
    update() {
        super.update()
        this.context.plane.location.update();
        this.context.plane.units.update();
        this.move();
        this.show()
    }
    show() {
        this.clear()
    }
  deactivate() {
    // prevent default behaviours of space and arrow keys
    window.addEventListener("keydown", function(e) {
      if([32, 37, 38, 39, 40].indexOf(e.keyCode) > -1) {
          e.preventDefault();
      }
    }, false)
  }
  resize() {
    this.canvas.width = this.context.width = window.innerWidth;
    this.canvas.height = this.context.height = window.innerHeight;
  }
  onKeyDown(evt) {
    console.log(evt.keyCode)
    switch(evt.keyCode) {
        case 39: // Arrow Right for moving right
            this.movement.right = true;
        case 37: // Arrow Left for moving left
            this.movement.left = true;
        case 40: // Arrow Up for moving up
            this.movement.up = true;
        case 38: // Arrow Down for moving down
            this.movement.down = true;
        case 16: // Left and Right shift for zooming in and out
            if (evt.location == 1) {
                this.movement.zoomout = true;
            } else {
                this.movement.zoomin = true;
            }
        case 18: // Alt for pause
            if (this.game.dt) {
                this.game.dt = 0;
            } else {
                this.game.dt = Game.dt;
            }
        }
  }
  onKeyUp(evt) {
    switch(evt.keyCode) {
      case 39: // Arrow Right
        this.movement.right = false;
      case 37: // Arrow Left
        this.movement.left = false;
      case 40: // Arrow Up
        this.movement.up = false;
      case 38: // Arrow Down
        this.movement.down = false;
      case 16:
        if (evt.location == 1) {
          this.movement.zoomout = false;
        } else {
          this.movement.zoomin = false;
        }
      }
  }
  onScroll(evt) {
    if (evt.wheelDeltaY>0) {
        this.context.plane.units[0].irmul(1+GameClient.scrollZoomFactor*GameClient.zoomDelta);
    } else {
        this.context.plane.units[0].irmul(1-GameClient.scrollZoomFactor*GameClient.zoomDelta);
    }
  }
  onMouseMotion(evt) {
    this.mouse = new Vector(evt.x, evt.y);
  }

  move() {
    if (this.movement.up) {
      this.context.plane.y += this.context.plane.speed/this.context.plane.ux;
    }
    if (this.movement.down) {
      this.context.plane.y -= this.context.plane.speed/this.context.plane.uy;
    }
    if (this.movement.left) {
      this.context.plane.x -= this.context.plane.speed/this.context.plane.ux;
    }
    if (this.movement.right) {
      this.context.plane.x += this.context.plane.speed/this.context.plane.uy;
    }
    if (this.movement.zoomin) {
      this.context.plane.units[0].irmul(1+GameClient.zoomDelta);
    }
    if (this.movement.zoomout) {
      this.context.plane.units[0].irmul(1-GameClient.zoomDelta);
    }
  }

}
