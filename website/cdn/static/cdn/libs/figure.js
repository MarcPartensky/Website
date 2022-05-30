/**
 * A figure is basically a base class
 * for any visual object.
 */
export default class Figure {
  static lineWidth = 1;
  static color = "#ffffff";
  static conversion = true;
  static random(...args) {
    throw "Static function random is not implemented."
  }
}
