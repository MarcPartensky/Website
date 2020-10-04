class ContextAdapter {
  constructor(context, plane=new Plane()) {
    this.context = context;
    this.plane = plane;
    this.textSeparator = "px ";
  }
  toScreen(v) {
    return this.plane.toScreen(v).add(this.center);
  }
  fromScreen(v) {
    return this.plane.fromScreen(v.sub(this.center));;
  }
  get width() {
    return this.context.width;
  }
  set width(value) {
    this.context.width = value;
  }
  get height() {
    return this.context.height;
  }
  set height(value) {
    this.context.height = value;
  }
  get center() {
    return new Vector(this.context.width/2, this.context.height/2);
  }
  set strokeStyle(value) {
    this.context.strokeStyle = value;
  }
  get strokeStyle() {
    return this.context.strokeStyle;
  }
  set fillStyle(value) {
    this.context.fillStyle = value;
  }
  get fillStyle() {
    return this.context.fillStyle;
  }
  set strokeWidth(value) {
    this.context.strokeWidth = value;
  }
  get strokeWidth() {
    return this.context.strokeWidth;
  }
  set lineWidth(value) {
    this.context.lineWidth = value * Math.max(...this.plane.units.position);
  }
  get lineWidth() {
    return this.context.lineWidth / Math.max(...this.plane.units.position);
  }
  beginPath() {
    this.context.beginPath();
  }
  closePath() {
    this.context.closePath();
  }
  stroke() {
    this.context.stroke();
  }
  fill() {
    this.context.fill();
  }
  translate(x, y) {
    let v = this.plane.units.position.tdot(new Vector(x,y));
    this.plane.position = v;
  }
  clear() {
    this.context.clearRect(0, 0, this.context.width, this.context.height);
  }
  strokeRect(x, y, w, h) {
    [x, y] = this.toScreen(new Vector(x,y));
    [w, h] = this.plane.units.position.tdot(new Vector(w,h));
    this.context.strokeRect(x, y, w, h);
  }
  fillRect(x, y, w, h, mg=0) {
    [x, y] = this.toScreen(new Vector(x,y));
    [w, h] = this.plane.units.position.tdot(new Vector(w,h));
    this.context.fillRect(x, y, w+mg, h+mg);
  }
  clearRect(x, y, w, h) {
    [x, y] = this.toScreen(new Vector(x,y));
    [w, h] = this.plane.units.position.tdot(new Vector(w,h));
    this.context.clearRect(x, y, w, h);
  }
  fillText(text, x, y) {
    [x, y] = this.toScreen(new Vector(x,y));
    this.context.fillText(text, x, y, 1000);
  }
  drawImage(img, x, y, w=undefined, h=undefined) {
    if (w && h) {
      [x, y] = this.toScreen(new Vector(x,y));
      [w, h] = this.plane.units.position.tdot(new Vector(w,h));
      this.context.drawImage(img, x, y, w, h);
    } else {
      [x, y] = this.toScreen(new Vector(x,y));
      this.context.drawImage(img, x, y);
    }
  }
  arc(x, y, r, a, b, conversion=true) {
    [x, y] = this.toScreen(new Vector(x,y));
    if (conversion) {
      r *= Math.max(...this.plane.units.position);
    }
    this.context.arc(x, y, r, a, b);
  }
  moveTo(x, y) {
    [x, y] = this.toScreen(new Vector(x,y));
    this.context.moveTo(x, y);
  }
  lineTo(x, y) {
    [x, y] = this.toScreen(new Vector(x,y));
    this.context.lineTo(x, y);
  }
  get font() {
    return this.context.font;
  }
  set font(value) {
    this.context.font = value;
  }
  get textSize() {
    return Number(this.context.font.split(this.textSeparator)[0])/Math.max(...this.plane.units.position);
  }
  get textFont() {
    return this.context.font.split(this.textSeparator)[1];
  }
  set textSize(value) {
    value *= Math.max(...this.plane.units.position);
    this.context.font = String(value) + this.textSeparator + this.textFont;
  }
  set textFont(value) {
    this.context.font = String(this.textSize) + this.textSeparator + value;
  }
}
