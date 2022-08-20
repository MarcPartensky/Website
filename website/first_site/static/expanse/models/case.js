class Case {
  constructor(color) {
    this.color = color;
    // this.texture = texture;
  }
  show(context, x, y) {
    context.fillStyle = this.color;
    context.fillRect(x, y, 1, 1);
  }
}

class Case2 {
  constructor(texture) {
    this.texture = texture;
  }
  show(context, x, y, w, h) {
    context.drawImage(this.texture, x, y, w, h);
  }
}
