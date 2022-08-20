class Triangle extends Polygon {
  // number of points is always 3
  static get length() {return 3;}
  static get w() {return 3;}
  static get width() {return 3;}
  static random(
    s=1,
    color=this.color,
    lineWidth=this.lineWidth,
    fill=this.fill
  ) {
    return new this(
      Matrix.random(this.w, this.h).rmul(s),
      color, lineWidth, fill);
  }
  constructor(matrix, ...args) {
    super(matrix, ...args)
  }
  get area() {
    const [a,b,c] = this.segments.map(s => s.length);
    console.log(a, b, c);
    return 1/4*Math.sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c));
  }
  contains(p) {
    const [p0, p1, p2] = this.matrix;
    const dX = p.x-p2.x;
    const dY = p.y-p2.y;
    const dX21 = p2.x-p1.x;
    const dY12 = p1.y-p2.y;
    const D = dY12*(p0.x-p2.x) + dX21*(p0.y-p2.y);
    const s = dY12*dX + dX21*dY;
    const t = (p2.y-p0.y)*dX + (p0.x-p2.x)*dY;
    if (D<0) return s<=0 && t<=0 && s+t>=D;
    return s>=0 && t>=0 && s+t<=D;
  }
}
