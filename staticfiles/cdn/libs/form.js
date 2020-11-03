import Figure from './figure.js';

/*
Unlike a figure, a form does have an area.
This class is more of an interface than
a true class or we can also see it as an
abstract class. (reference to PHP, C#, C++, ...)
*/
export default class Form extends Figure {
  static fill = false;
  static random(...args) {
    throw "Static function random is not implemented."
  }
  // get center() {
  //   throw "The get center method is not implemented for "+this+".";
  // }
  // set center(vector) {
  //   throw "The set center method is not implemented for "+this+".";
  // }
  get area() {
    throw "The get area method is not implemented for "+this+".";
  }
  set area(area) {
    throw "The set area method is not implemented for "+this+".";
  }
  translate(v) {
    throw "The translate method is not implemented for "+this+".";
  }
  rotate(r, vector=undefined) {
    throw "The rotate method is not implemented for "+this+".";
  }
}
