class Rectangle {
  static color = "#ffffff";
  static lineWidth = 1;
  static of(x, y, w, h, ...args) {
    return this([x,y], [w,h], ...args);
  }
  static from(a, ...args) {
    return new this(a.slice(0,2), a.slice(2), ...args)
  }
  static random() {
    return new this(Vector.random(), Vector.random());
  }
  
  constructor(position, size, color=Rectangle.color, lineWidth=Rectangle.lineWidth) {
    this.position = new Vector(...position);
    this.size = new Vector(...size);
    this.color = color;
    this.lineWidth = lineWidth;
  }
  get position() {
    return this[0];
  }
  set position(vector) {
    this[0] = vector;
  }
  get size() {
    return this[1];
  }
  set size(vector) {
    this[1] = vector;
  }
  get x() {
    return this[0][0]
  }
  set x(value) {
    this[0][0] = value;
  }
  get y() {
    return this[0][1];
  }
  set y(value) {
    this[0][1] = value;
  }
  get w() {
    return this[1][0];
  }
  set w(value) {
    this[1][0] = value;
  }
  get h() {
    return this[1][1];
  }
  set h(value) {
    this[1][1] = value;
  }
  get components() {
    return [this.x, this.y, this.w, this.h];
  }
  set components(value) {
    [this.x, this.y, this.w, this.h] = value;
  }
  get points() {
    let p1 = new Point(this.x, this.y);
    let p2 = new Point(this.x+this.w, this.y);
    let p3 = new Point(this.x+this.w, this.y+this.h);
    let p4 = new Point(this.x, this.y+this.h);
    return [p1, p2, p3, p4];
  }
  set points(value) {
    this.x = Math.min(value.map((p) => p.x));
    this.y = Math.min(value.map((p) => p.y));
    this.w = Math.max(value.map((p) => p.x))-this.x;
    this.h = Math.max(value.map((p) => p.y))-this.y;
  }
  get area() {
    return this.w*this.h;
  }
  show(ctx) {
    const p = new Polygon(this.points);
    p.show(ctx);
  }
}
