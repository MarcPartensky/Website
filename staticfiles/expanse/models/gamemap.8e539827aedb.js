class GameMap extends Array {
  /*
  * Extending array for syntax simplicity.
  */
  /*
  * Create an empty map using its width and height.
  */
  constructor(width, height) {
    super(width);
    for (let x=0; x<width; x++) {
      this[x] = Array(height);
    }
    this.frequency = 1/20;
    this.seed = {x:1000*Math.random(), y:1000*Math.random()};
    this.couples = [["#26266E", 0], ["#0000ff", 0.45], ["#4d00ff", 0.46],
                    ["#ffffff", 0.5],["#f5f500", 0.55], ["#00ff00",0.6],
                    ["#218E37", 0.70], ["#979E98", 0.80], ["#f5f5f5", 0.85],
                    ["#ffffff",1]];
  }
  get width() {
    return this.length;
  }
  get height() {
    return this[0].length;
  }
  /*
  * Generate the map using perlin noise generation.
  */
  generate() {
    for (let x=0; x<this.width; x++) {
      for (let y=0; y<this.height; y++) {
        this[x][y] = this.create(x, y);
      }
    }
  }
  /*
  * Create a case at a given position.
  */
  create(x, y) {    // let k = 255;
    // let a = parseInt(k*(noise.perlin2(f*x, f*y)+1)/2);
    // let v = new Vector(a, a, a);
    // let c = Color.fromVector(v);
    let t = (noise.perlin2(this.frequency*x+this.seed.x, this.frequency*y+this.seed.y)+1)/2;
    let c = Color.interpolate(this.couples, t);
    return new Case(c);
  }
  /*
  * Show the map.
  */
  show(context) {
    for (let x=0; x<this.width; x++) {
      for (let y=0; y<this.height; y++) {
        this[x][y].show(context, x, y);
      }
    }
  }
}
