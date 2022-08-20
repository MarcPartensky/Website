class Circle extends Form {
  constructor(
    vector, 
    radius, 
    lineWidth=Form.lineWidth, 
    borderColor=Form.borderColor, 
    areaColor=Form.areaColor, 
    fill=Form.fill
  ) {
    super(vector);
    this.radius = radius;
    this.lineWidth = lineWidth;
    this.areaColor = areaColor;
    this.borderColor = borderColor;
    this.fill = fill;
  }
  get center() {
    return this[0];
  }
  set center(value) {
    this[0] = value;
  }
  get x() {
    return this[0][0];
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
  get r() {
    return this.radius;
  }
  set r(value) {
    this.radius = value;
  }
  get color() {
    if (this.fill) {
      return this.areaColor;
    } else {
      return this.borderColor;
    }
  }
  set color(value) {
    if (this.fill) {
      this.areaColor = value;
    } else {
      this.borderColor = value;
    }
  }
  show(context) {
    context.lineWidth = this.lineWidth;
    if (this.fill) {
      context.fillStyle = this.color;
    } else {
      context.strokeStyle = this.color;
    }
    context.beginPath();
    context.arc(...this[0], this.radius, 0, 2*Math.PI);
    if (this.fill) {
      context.fill();
    } else {
      context.stroke();
    }
    context.closePath();
  }
  contains(position) {
    return this[0].sub(position).norm < this.radius;
  }
  collide(other) {
    return this[0].sub(other[0]).norm < this.radius+other.radius;
  }
}
