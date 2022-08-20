class Block {
  /*
  Create a block using its id, environment and width and height.
  */
  constructor(id, src, environment, w=100, h=100) {
    this.id = id;
    this.image = new Image(w, h);
    this.image.src = src;
    this.environment = environment;
  }
  get altitude() {
    return this.environment[0];
  }
  get temperature() {
    return this.environment[1];
  }
  get humidity() {
    return this.environment[2];
  }
  get frequency() {
    return this.environment[3];
  }
  show(context, x, y, w=1, h=1, t=0) {
    context.drawImage(this.image, x, y, w, h);
  }
}

class AnimatedBlock{
  constructor(id, src, w=100, h=100) {
    this.id = id;
    this.image = new Image(w, h);
    this.image.src = src;
  }
  show(context, x, y, w=1, h=1, t=0) {
    context.drawImage(this.image, x, y, w, h);
  }
}

class PixelBlock {
  constructor(id, grid, colors, environment) {
    this.id = id;
    this.grid = grid;
    this.colors = colors;
    this.environment = environment;
  }
  get width() {
    return this.grid[0].length;
  }
  get height() {
    return this.grid.length;
  }
  get size() {
    return [this.grid.length, this.grid[0].length];
  }
  show(context, x, y, w=1, h=1, t=0, mg=0.1) {
    let wk = w/this.width;
    let hk = h/this.height;
    for (let i=0; i<this.width; i++) {
      for (let j=0; j<this.height; j++) {
        context.fillStyle = this.colors[this.grid[j][i]];
        context.fillRect(x+i*wk, y+j*hk, wk+mg, hk+mg);
      }
    }
  }
}
