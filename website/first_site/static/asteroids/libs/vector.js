// import Tensor from 'tensor.js'

class Vector extends Tensor {
  static length = 2;
  // Mathematically a vector doesn't have a dimension
  // only a length we abuse of this term to qualify
  // the length, same goes for size.
  static get dim() {return this.length;}
  static set dim(v) {this.length = v;}
  static get size() {return this.length;}
  static set size(v) {this.length = v;}
  static color = "#ffffff";
  static norm = 2; // euclidan norm
  static lineWidth = 2; // in pixels
  static zero(...format) {
    return this.from(Tensor.zero(...format));
  }
  static one(n) {
    return this.fill(1, length);
  }
  static distance(v1, v2) {
    return (v1.sub(v2)).norm;
  }
  static copy = this.from; // Abusive
  static empty(n=0) {
    return this.from(Array(n));
  }
  static get zero2() {
    return new this(0, 0);
  }
  static get zero3() {
    return new this(0, 0, 0);
  }
  static random(dim = this.dim, min=-1, max=1) {
    let v = new this(dim);
    for (let i = 0; i < dim; i++) {
      v[i] = (Math.random()*(max-min))+min;
    }
    return v;
  }
  static randoms(n, dim = this.dim) {
    let vs = [];
    for (let i = 0; i < n; i++) {
      vs.push(this.random(dim));
    }
    return vs;
  }
  static polar(norm, angle) {
    return new this(
      norm * Math.cos(angle), 
      norm * Math.sin(angle)
    );
  }
  static fill(value, dim = this.dim) {
    let v = new this(dim);
    for (let i = 0; i < dim; i++) {
      v[i] = value;
    }
    return v;
  }
  static adapt(dim, ...vectors) {
    // let dim = Math.max(...vectors.map(v => v.dim));
    for (let i = 0; i < vectors.length; i++) {
      vectors[i].push(...Array(dim - vectors[i].dim).fill(0));
    }
  }
  get x() {
    return this[0];
  }
  set x(value) {
    this[0] = value;
  }
  get y() {
    return this[1];
  }
  set y(value) {
    this[1] = value;
  }
  get z() {
    return this[2];
  }
  set z(value) {
    this[2] = value;
  }
  get sum() {
    return this.reduce((x, y) => x+y);
  }
  get norm() {
    return (this.map(x => x ** Vector.norm).reduce((x, y) => x + y))**(1/Vector.norm);
  }
  set norm(value) {
    this.irmul(value/this.norm);
  }
  // The angle of a vector can only make sense
  // when applied on 2d vectors.
  // This is an abusive way to generalize for
  // simple usage.
  get angle() {
    return Math.atan2(this.y,this.x);
  }
  set angle(value) {
    const n = this.norm;
    this.x = n*Math.cos(value);
    this.y = n*Math.sin(value);
  }
  get components() {
    return Array.from(this);
  }
  set components(values) {
    this.set(values);
  }
  get dim() {
    return this.length;
  }
  set dim(value) {
    this.length = value;
  }
  get inv() {
    return this.map(x => 1 / x);
  }
  get unit() {
    let m = Math.max(...this);
    return this.map(x => x / m);
  }
  tdot(other) {
    const v = new Vector(this.length);
    for (let i=0; i<this.length; i++) {
      v[i] = this[i]*other[i];
    }
    return v;
  }
  dot(other) {
    let r = 0;
    for (const [r1, r2] of zip(this, other)) {
      r += r1*r2;
    }
    return r;
  }
  project(other) {
    return other.rmul(this.dot(other)/other.norm)
  }
  iproject(other) {
    this.set(this.project(other));
  }
  towards(vector) {
    return Vector.polar(this.norm, vector.sub(this).angle);
  }
  itowards(vector) {
    this.angle = vector.sub(this).angle;
  }
  translate(vector) {
    this.iadd(vector);
  }
  rotate(angle, vector=undefined) {
    vector = vector || Vector.zero(Vector.length);
    this.isub(vector)
    this.angle += angle;
    this.iadd(vector);
  }
  irot(angle, vector=undefined) {
    this.rotate(angle, vector);
  }
  rot(angle, vector=undefined) {
    vector = vector || Vector.zero(Vector.length);
    const v = this.sub(vector)
    v.angle += angle;
    v.iadd(vector);
    return v;
  }
  equals(vector) {
    for (let i = 0; i < Math.max(vector.dim, this.dim); i++) {
      if (this[i] != vector[i]) {
        return false;
      }
    }
    return true;
  }
  colinear(vector, error = 10 ** -10) {
    return this.mul(vector).norm < error;
  }
  fill(value) {
    return Vector.from(super.fill(value));
  }
  ifill(value) {
    for (let i = 0; i < this.dim; i++) {
      this[i] = value;
    }
  }
  map(f) {
    return Vector.from(super.map(f));
  }
  imap(f) {
    for (let i = 0; i < this.dim; i++) {
      this[i] = f(this[i]);
    }
  }
  slice(a, b) {
    return Vector.from(super.slice(a, b));
  }
  map2(vector, f) {
    let m = Math.max(this.dim, vector.dim);
    let v = Vector.empty(m);
    for (let i = 0; i < m; i++) {
      v[i] = (f(this[i], vector[i]));
    }
    return v;
  }
  imap2(vector, f) {
    let m = Math.max(this.dim, vector.dim);
    for (let i = 0; i < m; i++) {
      this[i] = (f(this[i], vector[i]));
    }
  }
  adapt(n) {
    let v = Vector.copy(this);
    if (n>this.length) {
      for (let i=0; i<n-this.length; i++) {
        v.push(0);
      }
    } else {
      for (let i=0; i<this.length-n; i++) {
        delete v[v.length-1];
      }
    }
    return v;
  }
  // prod(vector) {
  //   // Vectorial product
  //   throw "Not implemented error";
  // }
  div(k) {
    return this.rmul(1 / k);
  }
  idiv(k) {
    this.imul(1 / k);
  }
  ifloor() {
    this.imap(Math.floor);
  }
  floor() {
    return this.map(Math.floor);
  }
  limit(vmin, vmax) {
    let m = Math.max(this.length, vmin.length, vmax.length);
    for (let i=0; i<m; i++) {
      this[i] = Math.max(this[i], vmin[i]);
      this[i] = Math.min(this[i], vmax[i]);
    }
  }
  call(point) {
    return Point.from(this.vector.add(point));
  }
  /** 
   * Shows an arrow.
  */
  show(
    ctx,
    position=Vector.zero(this.dim),
    color=Vector.color,
    lineWidth=Vector.lineWidth,
    factor=10,
    angle=Math.PI/6
  ) {
    ctx.beginPath();
    ctx.context.lineWidth = lineWidth;
    ctx.strokeStyle = color;
    ctx.moveTo(...position);
    const p = this.add(position)
    ctx.lineTo(...p);
    const v = this.rdiv(-factor);
    v.rotate(angle)
    ctx.lineTo(...v.add(p));
    v.rotate(-2*angle)
    ctx.moveTo(...p)
    ctx.lineTo(...v.add(p));
    ctx.stroke();
    ctx.closePath();
  }
  closest(vectors) {
    let a = Infinity;
    let b, v;
    for (const vi of vectors) {
      b = this.sub(vi).norm;
      if (a > b) {
        v = vi;
        a = b;
      }
    }
    return v;
  }
  closestIndex(vectors) {
    let a = Infinity;
    let b;
    let i = 0,
      j = 0;
    for (const vi of vectors) {
      b = this.sub(vi).norm;
      if (a > b) {
        a = b;
        j = i;
      }
      i++;
    }
    return j;
  }
  farthest(vectors) {
    let a = 0;
    let b, v;
    for (const vi of vectors) {
      b = this.sub(vi).norm;
      if (a < b) {
        v = vi;
        a = b;
      }
    }
    return v;
  }
  farthestIndex(vectors) {
    let a = Infinity;
    let b;
    let i = 0,
      j = 0;
    for (const vi of vectors) {
      b = this.sub(vi).norm;
      if (a < b) {
        a = b;
        j = i;
      }
      i++;
    }
    return j;
  }
  get directionCosines() {
    for (let i=0; i<this.length; i++) {

    }
  }
}


class Vector2 extends Vector {
  // force the dimension to be 2
  static get dim() {return 2;}
  static polar(norm, angle) {
    return new this(
      norm * Math.cos(angle), 
      norm * Math.sin(angle)
    );
  }
  constructor(x, y) {
    super(x, y);
  }
  get angle() {
    return Math.atan2(this[1],this[0]);
  }
  set angle(value) {
    this[0] = this.norm*Math.cos(value);
    this[1] = this.norm*Math.sin(value);
  }
}

class Vector3 extends Vector {
  // force the dimension to be 3
  static get dim() {return 3;}
  constructor(x, y, z) {
    super(x, y, z);
  }
  cross(vector) {
    return new Vector(
      this[2]*vector[3]-this[3]*vector[2],
      this[3]*vector[1]-this[1]*vector[3],
      this[1]*vector[2]-this[2]*vector[1]
    );
  }
  rotate(angle, vector) {

  }
}
