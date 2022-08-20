class Line extends Figure {
  static color = "#ffffff";
  static lineWidth = 1;
  constructor(p, v, color=Line.color, lineWidth=Line.lineWidth) {
    super(p, v);
    this.color = color;
    this.lineWidth = lineWidth;
  }
  get point() {
    return this[0];
  }
  set point(value) {
    this[0] = value;
  }
  get vector() {
    return this[1];
  }
  set vector(value) {
    this[1] = value;
  }
  /*
  Reset the point to the closest point of the line to the origin.
  */
  correct() {


  }
  get angle() {
    return this[1].angle;
  }
  set angle(value) {
    this[1].angle = value;
  }
  show(context) {
    context.lineWidth = this.lineWidth;
    context.strokeStyle = this.color;
    context.beginPath();
    context.
    context.close();
  }
  contains(point) {
    return point.sub(this.point).

  }
  project(point) {
    const v = this.vector.rot(Math.PI/2);




  }
}
