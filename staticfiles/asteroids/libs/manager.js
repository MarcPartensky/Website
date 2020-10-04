class Manager {
  static zoomDelta = 0.1;
  static scrollZoomFactor = 0.5;
  static entities = [];
  static dt = 0.1;
  static movement = {up: false, down: false, right: false, left: false, zoomin: false, zoomout: false};
  static backgroundColor = "#000000";

  addEventListeners() {
    // using window as a global
    window.addEventListener("keydown", this.onKeyDown.bind(this));
    window.addEventListener("keyup", this.onKeyUp.bind(this));
    window.addEventListener("mousemove", this.onMouseMotion.bind(this));
    window.addEventListener("scroll", this.onScroll.bind(this));
    window.addEventListener("mousewheel", this.onScroll.bind(this));
    window.addEventListener("resize", this.resize.bind(this));
  }
  deactivate() {
    // prevent default actions from space and arrow keys
    window.addEventListener("keydown", function(e) {
      if([32, 37, 38, 39, 40].indexOf(e.keyCode) > -1) {
          e.preventDefault();
      }
    }, false);
  }
  constructor(
    canvas,
    game,
    dt=Manager.dt,
    movement=Manager.movement,
    backgroundColor=Manager.backgroundColor
  ) {
    this.canvas = canvas;
    this.context = new ContextAdapter(this.canvas.getContext("2d"));
    this.game = game;
    this.dt = dt;
    this.movement = movement;
    this.backgroundColor = backgroundColor;
    this.mouse = new Vector(0, 0);
  }
  clear() {
    this.context.fillStyle = this.backgroundColor;
    this.context.clear();
  }
  show() {
    this.clear();
    this.game.show(this.context);
  }
  update() {
    this.context.plane.location.update();
    this.context.plane.units.update();
    this.move();
    this.game.update(this.dt);
  }
  resize() {
    this.canvas.width = this.context.width = window.innerWidth;
    this.canvas.height = this.context.height = window.innerHeight;
  }
  onKeyDown(evt) {
    switch(evt.keyCode){
      case 39: // Arrow Right for moving right
        this.movement.right = true;
        break;
      case 37: // Arrow Left for moving left
        this.movement.left = true;
        break;
      case 40: // Arrow Up for moving up
        this.movement.up = true;
        break;
      case 38: // Arrow Down for moving down
        this.movement.down = true;
        break;
      case 16: // Left and Right shift for zooming in and out
        if (evt.location == 1) {
          this.movement.zoomout = true;
        } else {
          this.movement.zoomin = true;
        }
        break;
      case 18: // Alt for pause
        if (this.dt) {
          this.dt = 0;
        } else {
          this.dt = Manager.dt;
        }
      }
  }
  onKeyUp(evt) {
    switch(evt.keyCode) {
      case 39: // Arrow Right
        this.movement.right = false;
        break;
      case 37: // Arrow Left
        this.movement.left = false;
        break;
      case 40: // Arrow Up
        this.movement.up = false;
        break;
      case 38: // Arrow Down
        this.movement.down = false;
        break;
      case 16:
        if (evt.location == 1) {
          this.movement.zoomout = false;
        } else {
          this.movement.zoomin = false;
        }
        break;
      }
  }
  onScroll(evt) {
    if (evt.wheelDeltaY>0) {
        this.context.plane.units[0].irmul(1+Manager.scrollZoomFactor*Manager.zoomDelta);
    } else {
        this.context.plane.units[0].irmul(1-Manager.scrollZoomFactor*Manager.zoomDelta);
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
      this.context.plane.units[0].irmul(1+Manager.zoomDelta);
    }
    if (this.movement.zoomout) {
      this.context.plane.units[0].irmul(1-Manager.zoomDelta);
    }
  }
  loop() {
    this.update();
    this.show();
    requestAnimationFrame(this.loop.bind(this));
  }
  start() {
    // this.resize(); // resize has its own event listener to call it
    this.addEventListeners();
    // this.deactivate(); // no need to deactivate anything after all
  }
  main() {
    this.start();
    this.loop();
  }
}

