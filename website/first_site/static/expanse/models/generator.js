class TerrainColorGenerator {
  constructor(seed=100000*Math.random(), frequency=1/100, precision=100) {
    this.seed = seed;
    this.frequency = frequency;
    this.precision = precision;
    this.couples = [["#26266E", 0], ["#0000ff", 0.45], ["#4d00ff", 0.5],
                    ["#ffff00", 0.5], ["#f5f500",0.55], ["#E6A83B",0.56],
                    ["#218E37", 0.60], ["#279B15", 0.80],
                    ["#979E98", 0.81], ["#f5f5f5", 0.9], ["#ffffff",1]];
  }
  showRaw(context, xmin, ymin, xmax, ymax) {
    for (let x=xmin; x<xmax; x++) {
      for (let y=ymin; y<ymax; y++) {
          this.showRect(context,x,y,1,1);
      }
    }
  }
  showNet(context, xmin, ymin, xmax, ymax) {
    for (let x=0; x<this.precision; x++) {
      for (let y=0; y<this.precision; y++) {
          this.showRect(context,
            Color.linear(x, 0, this.precision, xmin, xmax),
            Color.linear(y, 0, this.precision, ymin, ymax),
            (xmax-xmin)/this.precision,
            (ymax-ymin)/this.precision,
            1,
          );
      }
    }
  }
  showRect(context, x, y, w, h) {
    context.fillStyle =  Color.interpolate(this.couples,
      (noise.perlin2(this.frequency*x+this.seed, this.frequency*y+this.seed)+1)/2
    );
    context.fillRect(x, y, w, h, 1);
  }
  showCase(context, x, y, w, h) {
    // let case = Case.generate();
    // case.show(x, y, 1, 1);
  }
  getEnvironment(x, y, n=3, k=1) {
    let a = Array(n);
    for (let i=0; i<n; i++) {
      a[i] = (noise.perlin2(x*this.frequency*k**i+this.seed, y*this.frequency*k**i+this.seed)+1)/2
    }
    return a;
  }
}


class TerrainGenerator extends Terrain {
  constructor() {

  }
}
