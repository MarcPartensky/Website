class Segment extends BasePolygon {
  static lineWidth = 3; // pixels
  static color = "#ffffff";
  static random(lineWidth=super.width, color=super.color) {
    return new Segment(
      Point.random(),
      Point.random(),
      lineWidth,
      color)
  }
  constructor(p1=Point.zero2, p2=Point.zero2,
    lineWidth=Segment.lineWidth,
    color=Segment.color
  ) {
    super();
    this.points = new Matrix(Point.from(p1), Point.from(p2));
    this.lineWidth = lineWidth;
    this.color = color;
  }
  get p1() {
    return this.points[0];
  }
  set p1(value) {
    this.points[0] = value;
  }
  get p2() {
    return this.points[1];
  }
  set p2(value) {
    this.points[1] = value;
  }
  translate(vector) {
    for (const p of this.points) {
      p.translate(vector);
    }
  }
  rotate(angle, vector=undefined) {
    vector = vector || this.center;
    for (const p of this.points) {
      p.rotate(angle, vector);
    }
  }
  get center() {
    return Vector.average(...this.points);
  }
  set center(v) {
    this.translate(v.sub(this.center));
  }
  get vector() {
    return this.p2.sub(this.p1);
  }
  set vector(v) {
    this.p2 = v.sub(this.p1);
  }
  get normal() {
    return this.vector.rot(Math.PI/2);
  }
  set normal(vector) {
    this.vector = vector.rot(-Math.PI/2);
  }
  get angle() {
    return this.vector.angle;
  }
  set angle(a) {
    this.rotate(a-this.angle);
  }
  get length() {
    return this.p1.sub(this.p2).norm
  }
  get line() {
    return new Line(this.p1, this.vector);
  }
  show(context) {
    context.context.lineWidth = this.lineWidth;
    context.strokeStyle = this.color;
    context.beginPath();
    context.moveTo(...this.p1);
    context.lineTo(...this.p2);
    context.closePath();
    context.stroke();
  }
  get base() {
    const [a, b] = this.vector.unit();
    const [c, d] = this.normal.unit();
    return new Matrix([a,b],[c,d]);
  }
  toBase(vector) {
    return new Vector(
      vector.dot(this.vector)/this.vector.norm,
      vector.dot(this.normal)/this.normal.norm
    );
  }
  contains(point, precision=1e-10) {
    const d = Point.distance(this.p1, point)+Point.distance(this.p2, point);
    return d-this.length <= precision;
  }
  crossLine(line) {
    const point = this.line.cross(line);
    if (this.contains(point)) {
      return point;
    }
    return undefined;
  }
  crossSegment(segment) {
    const point = this.line.cross(segment.line);
    if (this.contains(point)) {
      if (segment.contains(point)) {
        return point;
      }
    }
    return undefined;
  }
  cross(figure) {
    if (this.figure instanceof Segment) {
      return this.crossSegment(segment);
    } else if (this.figure instanceof Line) {
      return this.crossLine(figure);
    } else if (this.figure instanceof Polygon) {
      return figure.crossSegment(segment);
    } else {
      throw `Collisions between ${this.constructor.name} and ${figure.constructor.name} are not dealt with`;
    }
  }
  
 }
