class Player extends Body {
  constructor(motion=new Motion(new Vector()), block, size=new Vector(1, 1)) {
    super(...motion);
    // this.image = new Image(...image_size);
    // this.image.src = src;
    this.block = block;
    this.size = size;
  }
  get w() {
    return this.size[0];
  }
  get h() {
    return this.size[1];
  }
  show(context) {
    // context.drawImage(this.image, this.x, this.y);
    block.show(context, this.x, this.y, this.w, this.h);
  }
}

var skin = new PixelBlock("skin", [
  [0, 0, 0, 1, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 3, 2, 0, 0, 0],
  [7, 7, 0, 2, 2, 0, 0, 0],
  [0, 4, 4, 4, 4, 4, 4, 0],
  [0, 0, 0, 4, 4, 0, 2, 0],
  [0, 0, 0, 5, 5, 0, 1, 0],
  [0, 0, 6, 6, 6, 0, 0, 0],
],[NaN, "#000000", "#brown", "#012345", "#00ff00", "#cc9966","#ffbb99", "#999999"], new Vector(1, -1, 1));


// "imgs/character.png"
// var p1 = new Player(new Motion(new Vector(0, 0)), skin);
