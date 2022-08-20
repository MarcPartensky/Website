class Segment extends Figure {
  static lineWidth = 1;
  static color = "#ffffff";
  static random(lineWidth=super.width, color=super.color) {
    p1 = Point.random();
    p2 = Point.random();
    return new Segment(p1, p2, lineWidth, color)
  }
  constructor(p1, p2, lineWidth, color) {
    super(p1, p2);
    this.points = [p1, p2];
    this.lineWidth = lineWidth || super.lineWidth;
    this.color = color || super.color;
  }
  get p1() {
    return this[0];
  }
  set p1(value) {
    this[0] = value;
  }
  get p2() {
    return this[1];
  }
  set p2(value) {
    this[1] = value;
  }
  show(context) {
    context.lineWidth = this.lineWidth;
    context.strokeStyle = this.color;
    context.beginPath();
    context.moveTo(...this.p1);
    context.lineTo(...this.p2);
    context.close();
  }
}
