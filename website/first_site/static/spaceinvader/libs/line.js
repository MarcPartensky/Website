import Figure from './figure.js';
import Point from './point.js';

export default class Line extends Figure {
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
    this.vector.iunit();

  }
  show(context) {
    context.lineWidth = this.lineWidth;
    context.strokeStyle = this.color;
    context.beginPath();
    context.closePath();
    context.close();
  }
  get other() {
    return this.vector.call(this.point);
  }
  set other(point) {
    this.point = this.vector.sub(point)
  }
  get slope() {
    const [x1, y1] = this.point;
    const [x2, y2] = this.other;
    return (y2-y1)/(x2-x1);
  }
  get a() {
    return this.slope;
  }
  get intercept() {
    const [x, y] = this.point;
    return y-this.a*x;
  }
  get b() {
    return this.intercept;
  }
  get cartesianComplete() {
    throw "Not implemented yet.";
  }
  get cartesianReduced() {
    return [this.a, this.b];
  }
  get normal() {
    return this.vector.rot(Math.PI/2);
  }
  contains(point) {
    return point.sub(this.point);
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
  crossLine(line, precision=1e-10) { // Done the Wikipedia way
    const v1 = this.vector;
    const v2 = line.vector;
    const [x1, y1] = this.point;
    const [x3, y3] = line.point;
    const [x2, y2] = this.vector.call(this);
    const [x4, y4] = line.vector.call(line.point);
    const d = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4);
    if (abs(d)<precision) { // 2 lines parallels
      return undefined;
    }
    const t = (x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)/d;
    const u = (x1-x2)*(y1-y3)-(y1-y2)*(x1-x3)/d;
    return new Point(x1+t*(x2-x1),y1+t*(y2-y1))
  }
  crossSegment(segment) {
    return segment.crossLine(Line);
  }
  cross(figure) {
    if (figure instanceof Line) {
      return this.crossLine(figure);
    } else if (figure instanceof Segment) {
      return this.crossSegment(figure);
    } else if (figure instanceof Polygon) {
      figure.crossSegment(this);
    } else {
      throw `Collisions between ${this.constructor.name} and ${figure.constructor.name} are not dealt with`;
    }
  }
  crossEquations(line, precision=1e-10) { // Done the Wikipedia way
    const a = this.slope;
    const b = line.slope;
    const c = this.intercept;
    const d = line.intercept;
    if (abs(a-b)<precision) { // 2 lines parallels
      return undefined; 
    }
    return new Point((d-c)*(a-b), a*(d-c)/(a-b)+c);
  }
}
