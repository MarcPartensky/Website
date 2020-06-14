class Line extends Figure {
  static color = "#ffffff";
  static lineWidth = 1;
  constructor(point, vector, color=Line.color, lineWidth=Line.lineWidth) {
    this.point = point;
    this.vector = vector;
    this.color = color;
    this.lineWidth = lineWidth;
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
    context.closePath();
    context.close();
  }
  contains(point) {
    return point.sub(this.point)
  }
  project(point) {
    const v = this.vector.rot(Math.PI/2);
  }
}
