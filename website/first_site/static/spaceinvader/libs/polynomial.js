import Vector from './vector.js';

export default class Polynomial extends Vector {
  static fromRoots(roots) {
    let p = this.one;
    for (const root of roots) {
      p.imul(new this(root, 1))
    }
    return p;
  }
  /*
  Create a polynomial using the unpacked list of components.
  */
  constructor(...components) {
    super(...components);
  }
  /*
  Evaluate the polynomial at a given value.
  */
  call(x) {
    let v = 0;
    for (let i=0; i<this.length; i++) {
      v += x*this[i]**i;
    }
    return v;
  }
  str() {
    let ws = [];
    let w = "";
    let c, j;
    for (let i=0; i<this.length; i++) {
      j = this.length-1-i;
      c = this[j];
      if (c!=0) {
        if (j==0) {
          w = String(c);
        } else if (j==1) {
          if (c==1) {
            w = "X";
          } else {
            w = String(c)+"X";
          }
        } else {
          if (c==1) {
            w = "X^"+String(j);
          } else {
            w = String(c)+"X^"+String(j);
          }
        }
        ws.push(w);
      }
    }
    let s = ws.join("+");
    if (s=="") {
      s = "0";
    }
    return s;
  }
  /*
  Delete the zeros at the end of the polynomial.
  */
  correct() {
    while (this[this.length-1]==0) {
      delete this[this.length-1];
    }
  }
  /*
  Return the degree of the polynomial.
  */
  get degree() {
    return this.length;
  }
  /*
  Multiply the polynomial with another polynomial.
  */
  mul(other) {
    let n = this.degree;
    let p = other.degree;
    let m = Math.max(n, p);
    this.iadapt(m);
    other.iadapt(m);
    let polynomial = new Polynomial();
    for (let k=0; k<m; k++) {
      let c = 0;
      for (let i=0; i<k; i++) {
        c += this[i] * other[k-i];
      }
      polynomial.push(c);
    }
    polynomial.correct();
    return polynomial;
  }
  factorize() {

  }
}
