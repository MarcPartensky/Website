//import Vector from './vector.js';

class Point extends Vector {
  static radius = 1;
  static color = "#ffffff";
  static conversion = false;
  static average(...points) {
    return new Point(...Vector.average(...points));
  }
  static random(n=2) {
    return Point.from(Vector.random(n));
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
  show(
    context,
    color=Point.color,
    radius=Point.radius,
    conversion=Point.conversion
  ) {
    context.beginPath();
    context.fillStyle = color;
    context.arc(this.x, this.y, radius, 0, 2*Math.PI, conversion);
    context.fill();
    context.closePath();
  }
}
