class Rectangle extends BasePolygon {
  static color = "#ffffff";
  static lineWidth = 1;
  static of(x, y, w, h, ...args) {
    return this(x,y, w,h, ...args);
  }
  static from(a, ...args) {
    return new this(a.slice(0,2), a.slice(2), ...args)
  }
  static random() {
    return new this(Vector.random(), Vector.random());
  }
  
  constructor(
    position,
    size,
    color=Rectangle.color,
    lineWidth=Rectangle.lineWidth,
    fill=Rectangle.fill,
  ) {
    super(color, lineWidth, fill);
    this.position = new Vector(...position);
    this.size = new Vector(...size);
  }
  translate(vector) {
    this.position.iadd(vector);
  }
  get x() {
    return this.position[0]
  }
  set x(value) {
    this.position[0] = value;
  }
  get y() {
    return this.position[1];
  }
  set y(value) {
    this.position[1] = value;
  }
  get w() {
    return this.size[0];
  }
  set w(value) {
    this.size[0] = value;
  }
  get h() {
    return this.size[1];
  }
  set h(value) {
    this.size[1] = value;
  }
  get components() {
    return [...this.position, ...this.size];
  }
  set components(value) {
    this.position = value.slice(0, 2);
    this.size = value.slice(2, 4);
  }
  get points() {
    return [
      new Point(this.x, this.y),
      new Point(this.x+this.w, this.y),
      new Point(this.x+this.w, this.y+this.h),
      new Point(this.x, this.y+this.h)
    ];
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
    if (this.lineWidth) {
        ctx.lineWidth = this.lineWidth;
    }
    if (this.fill) {
      ctx.fillStyle = this.color;
      ctx.fillRect(...this.components);
    } else {
      ctx.strokeStyle = this.color;
      ctx.strokeRect(...this.components);
    }
  }
}
