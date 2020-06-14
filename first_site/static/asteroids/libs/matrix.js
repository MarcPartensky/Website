class Matrix extends Tensor {
  /*
  * A matrix can be built from a 2d array, a list of vectors
  */
  static get order() {return 2}; /* Fancy way of declaring a static constant. */
  static w = 1;
  static h = 1;
  static format = [this.w, this.h];
  static zero(...format) {
    let v = Tensor.zero(...format)
    v = v.map(x => Matrix.from(x))
    return v;
  }

  static random(w=this.w, h=this.h) {
    return super.random(w,h).map(t => Vector.from(t));
  }
  static toVectors(...vectors) {
    return this.from(vectors.map(v => Vector.from(v)))
  }
  static from(vectors) {
    return super.from(vectors.map(v => Vector.from(v)));
  }
  constructor(...vectors) {
    super(...vectors)
    for (let i=0; i<this.length; i++) {
      if (this[i]!=undefined) {
        this[i] = Vector.from(this[i]);
      }
    }
  }
  get width() {
    return this.length;
  }
  get height() {
    return this[0].length;
  }
  get format() {
    return [this.width, this.height];
  }
  str() {
    let m = this.slice();
    for (let x=0; x<this.width; x++) {
      m[x] = m[x].join(" ");
    }
    return m.join("\n");
  }
  slice() {
    return new Matrix(...super.slice());
  }
  dot(matrix) {
    let d = this.width;
    let h = this.height;
    let w = matrix.width;
    let m = Matrix.fromFormat(w, h);
    for (let x=0; x<w; x++) {
      for (let y=0; y<h; y++) {
        m[x][y] = this[x][y]*matrix[x][y];
      }
    }
    return m;
  }
  idot(matrix) {
    this.set(this.dot(matrix));
  }
  mul(matrix) {
    let d = this.width;
    let h = this.height;
    let w = matrix.width;
    let m = Matrix.fromFormat(w, h);
    for (let x=0; x<w; x++) {
      for (let y=0; y<h; y++) {
        m[x][y] = 0;
        for (let z=0; z<d; z++) {
          m[x][y] += this[z][y]*matrix[x][z];
        }
      }
    }
    return m;
  }
  imul(matrix) {
    return this.set(this.mul(matrix));
  }
  vmul(vector) {
    let w = this.width;
    let h = this.height;
    let a = Array(h);
    for (let y=0; y<h; y++) {
      a[y] = 0;
      for (let x=0; x<w; x++) {
        a[y] += this[x][y] * vector[x];
      }
    }
    return new Vector(...a);
  }
}

class SquareMatrix extends Matrix {
  static length = 1;
  static random(length=Matrix.length) {
    let m = new SquareMatrix(...Matrix.fromFormat(length, length));
    for (let x=0; x<length; x++) {
      for (let y=0; y<length; y++) {
        m[x][y] = Math.random();
      }
    }
    return m;
  }
  constructor(...vectors) {
    if (Math.max(...vectors.map(v => v.length)) != Math.min(...vectors.map(v => v.length))) {
      throw new Error("The vectors must have the same length.");
    }
    super(...vectors);
  }
  get det2() {
    const n = this.length;
    let v = 0;
    for (let i=0; i<n; i++) {
      let p1 = 1;
      let p2 = 1;
      for (let j=0; j<n; j++) {
        console.log()
        p1 *= this[(i+j)%n][j];
        p2 *= this[(i-j+n)%n][j];
      }
      v += (p1-p2);
    }
    return v;
  }
  get det() {
    let v = 0;
    for (p of permutation([...range(this.length)])) {
     // v +=
    }
    return v;
  }
}
/*
node
.load tensor.js
.load matrix.js
m = new SquareMatrix([1, 2], [3, 4]);

*/
