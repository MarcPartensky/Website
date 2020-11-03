import BasePolygon from './basepolygon.js';
import Point from './point.js';
import Vector from './vector.js';

export default class Square extends BasePolygon {
  static random(...args) {
    return new this(
      Math.random(-1, 1),
      Math.random(-1, 1),
      Math.random(0, 1),
      ...args
    );
  }
  constructor(
    x, y, s,
    color=BasePolygon.color,
    lineWidth=BasePolygon.lineWidth,
    fill=BasePolygon.fill
  ) {
    super(color, lineWidth, fill);
    this.x = x;
    this.y = y;
    this.s = s;
  }
  get size() {return this.s;}
  set size(v) {this.s = v;}
  get side() {return this.s;}
  set side(v) {this.s = v;}
  get w() {return s;}
  set w(v) {this.s = v;}
  get h() {return this.s;}
  set h(v) {this.s = v;}
  get area() {return this.s**2;}
  get center() {
    return new Vector(this.x+this.s/2, this.y+this.s/2);
  }
  set center(vector) {
    this.x = vector.x - this.s/2;
    this.y = vector.y - this.s/2;
  }
  get points() {
    return [
      new Point(this.x, this.y),
      new Point(this.x+this.s, this.y),
      new Point(this.x+this.s, this.y+this.s),
      new Point(this.x, this.y+this.s)
    ];
  }
  set points(pts) {
    this.x = Math.min(value.map(pts => pts.x));
    this.y = Math.min(value.map(pts => pts.y));
    // naive mapping because the information is redundant
    this.s = Math.max(value.map(pts => pts.x))-this.x;
  }
  get components() {
    return [this.x, this.y, this.z];
  }
  set components(cps) {
    this.x = cps[0];
    this.y = cps[1];
    this.s = cps[2];
  }
  show(ctx) {
    if (this.lineWidth) {
        ctx.lineWidth = this.lineWidth;
    }
    if (this.fill) {
      ctx.fillStyle = this.color;
      ctx.fillRect(this.x, this.y, this.s, this.s);
    } else {
      ctx.strokeStyle = this.color;
      ctx.strokeRect(this.x, this.y, this.s, this.s);
    }
  }
  contains(p) {
    return this.x <= p[0] <= this.x+this.s &&
          this.y <=  p[1] <= this.y+this.s;
    
  }
}