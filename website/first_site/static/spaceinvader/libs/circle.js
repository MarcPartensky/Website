class Circle extends Form {
  constructor(
    center,
    radius, 
    lineWidth=Form.lineWidth, 
    color=Form.color,
    fill=Form.fill
  ) {
    super();
    this.center = center
    this.radius = radius;
    this.lineWidth = lineWidth;
    this.color = color;
    this.fill = fill;
  }
  get x() {
    return this.center[0];
  }
  set x(value) {
    this.center[0] = value;
  }
  get y() {
    return this.center[1];
  }
  set y(value) {
    this.center[1] = value;
  }
  get r() {
    return this.radius;
  }
  set r(value) {
    this.radius = value;
  }
  show(context) {
    context.lineWidth = this.lineWidth;
    if (this.fill) {
      context.fillStyle = this.color;
    } else {
      context.strokeStyle = this.color;
    }
    context.beginPath();
    context.arc(...this.center, this.radius, 0, 2*Math.PI);
    if (this.fill) {
      context.fill();
    } else {
      context.stroke();
    }
    context.closePath();
  }
  contains(position) {
    return this.center.sub(position).norm < this.radius;
  }
  crossCircle(circle) {
    return this.center.sub(circle.center).norm < this.radius+other.radius;
  }
}
