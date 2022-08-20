/*
Basically a list of points. Unlike a figure, a form does have an area.
*/
class Form extends Figure {
  static width = 3;
  static height = 2;

  static color = "#ffffff";
  static areaColor = this.color;
  static borderColor = Color.darken(this.areaColor);
  static fill = true;
  static random(w, h, areaColor=Form.areaColor, borderColor=Form.borderColor) {
    var f = Figure.random(w, h);
    f.areaColor = areaColor;
    f.borderColor = borderColor;
  }
  constructor(vectors, areaColor=Form.areaColor, borderColor=Form.borderColor) {
    super(vectors);
    this.areaColor = areaColor;
    this.borderColor = borderColor;
  }
}
