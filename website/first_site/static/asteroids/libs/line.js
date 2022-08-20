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
  show(context) {
    context.lineWidth = this.lineWidth;
    context.strokeStyle = this.color;
    context.beginPath();
    context.closePath();
    context.close();
  }
  contains(point) {
    return point.sub(this.point);
  }
  get normal() {
    return this.vector.rot(Math.PI/2);
  }
  distance(point) {
    return Math.abs(point.sub(this.point).dot(this.normal));
  }
  height(point) {
    return point.sub(this.point).dot(this.normal);
  }
  project(point) {
    return this.vector.rmul(point.sub(this.point).dot(this.vector)/this.vector.norm**2).add(this.point);
  }
  cross(line) {
    const v1 = this.vector;
    const v2 = line.vector;
    const p1 = this.point;
    const p2 = line.point;
    const p1_ = this.vector.call(this);
    const p2_ = line.vector.call(line.point);
    (p.x-p1.x)*v1.y = v1.x*(p.y-p1.y)
    (p.x-p2.x)*v2.y = v2.x*(p.y-p2.y)
    l2-l1
    p1.x*v1.y-p2.x*v2.y = v1.x*p1.y-v2.x*p2.y
  }
}
