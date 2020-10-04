class Segment extends Figure {
  static lineWidth = 3; // pixels
  static color = "#ffffff";
  static random(lineWidth=super.width, color=super.color) {
    return new Segment(
      Point.random(),
      Point.random(),
      lineWidth,
      color)
  }
  constructor(p1, p2,
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
  get angle() {
    return this.vector.angle;
  }
  set angle(a) {
    this.rotate(a-this.angle);
  }
  get length() {
    return this.p1.sub(this.p2).norm
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
}
