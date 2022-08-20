/*

*/
class Figure extends Matrix {
  static lineWidth = 1;
  static borderColor = "#ffffff";
  static conversion = true;
  constructor(vectors) {
    super(...vectors);
  }
}
