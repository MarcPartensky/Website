class Point extends Vector {
  static radius = 1;
  static color = "#ffffff";
  static conversion = false;
  static average(...points) {
    return new Point(...Vector.average(...points));
  }
  static random(n=2) {
    return new Point(...Vector.random(n));
  }
  constructor(...components) {
    super(...components);
    this.radius = Point.radius;
    this.color = Point.color;
    this.conversion = Point.conversion;
  }
  map(f) {
    return new Point(...super.map(f));
  }
  get r() {
    return this.radius;
  }
  set r(value) {
    this.radius = value;
  }
  show(context) {
    context.beginPath();
    context.fillStyle = this.color;
    context.arc(this.x, this.y, this.radius, 0, 2*Math.PI, this.conversion);
    context.fill();
    context.closePath();
  }
}
