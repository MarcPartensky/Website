/*
A tensor is either an array of tensors or an array of numbers.
Every operation done on tensors is executed recursively.
It makes it easier to use but maybe slower to compute with.
*/
class Tensor extends Array {
  /*
  Every tensor has a norm, order, format and size. Here are stored default values.
  */
  static norm = 2;
  // static norm = 2;
  static order = 1;
  static format = [1];

  static empty(...format) {
    format = format || this.format;
    let t = this.from(Array(format[0]));
    if (format.length>1) {
      for (let i = 0; i < format[0]; i++) {
        t[i] = this.empty(...format.slice(1, format.length));
      }
    }
    return t;
  }
  /**
   * Create a tensor filled with zero with given format.
   * @param  {...Number} format 
   */
  static zero(...format) {
    format = format || this.format;
    let t = new Tensor(format[0]);
    if (format.length > 1) {
      for (let i = 0; i < format[0]; i++) {
        t[i] = Tensor.zero(...format.slice(1));
      }
    } else {
      for (let i = 0; i < format[0]; i++) {
        t[i] = 0;
      }
    }
    return t;
  }
  /*
  Create a new tensor with the same format of the given one but filled with zeros.
  */
  static zeroLike(tensor) {
    return this.zero(...tensor.format);
  }
  static fill(value, ...format) {
    let t = this.zero(...format);
    return t.fill(value);
  }
  static fillLike(value, tensor) {
    return this.fill(value, ...tensor.format);
  }
  static random(...format) {
    format = format || this.format;
    let t = new Tensor(format[0]);
    if (format.length==0) {return t};
    for (let i = 0; i < format[0]; i++) {
      if (format.length==1) {
        t[i] = Math.random();
      } else {
        t[i] = Tensor.random(...format.slice(1));
      }
    }
    return this.from(t);
  }
  /*
  Does the sum of all tensors.
  */
  static sum(...tensors) {
    return tensors.reduce((x, y) => x.add(y));
  }
  /**
   * Does the average of all tensors.
   * @param  {...Tensor} Tensor 
   */
  static average(...tensors) {
    return Tensor.sum(...tensors).rdiv(tensors.length);
  }
  /**
   * Multiply all the tensors together.
   * @param  {...Tensor} tensors 
   */
  static prod(...tensors) {
    return tensors.reduce((x, y) => x.mul(y));
  }
  /**
   * Copy a tensor.
   * @param {Tensor} tensor 
   */
  static copy(tensor) {
    return tensor.slice(0);
  }
  /**
   * Determine the distance between multiple tensors.
   * @param  {...Tensor} tensors 
   */
  static distance(...tensors) {
    if (tensors.length==2) {
      return tensors[0].sub(tensors[1]).norm;
    }
    let d = 0;
    let t = undefined;
    for (const ti of tensors) {
      if (t) {
        d += Tensor.distance(t, ti);
      }
      t = ti;
    }
    return d;
  }
  /*
  Convert an array of arrays into a tensor of tensors using
  a recursive approach.
  */
  static convert(v, type=this) {
    if (v instanceof Array) {
      if (v[0] instanceof Array) {
        return v.map(t => this.convert(t, type=type));
      } else {
        return type.from(v);
      }
    } else {
      return type.from(v);
    }
  }
  /*
  The constructor takes an array of arrays as input and makes
  it a tensor of tensors.
  */
  // constructor(...array) {
  //   if (array.length==1) {
  //     super(1);
  //     this[0] = array[0];
  //   } else {
  //     // super(...Tensor.convert(array));
  //     super(...array);
  //   }
  // }
  /*
  Return the order of the tensor.
  */
  get order() {
    if (this[0] instanceof Tensor) {
      return this[0].order + 1;
    } else {
      return 1;
    }
  }
  /*
  Return the format of the tensor.
  */
  get format() {
    if (this[0] instanceof Tensor) {
      return [this.length].concat(this[0].format);
    } else {
      return [this.length];
    }
  }
  /*
  Return the size of the tensor which is the product of the format.
  */
  get size() {
    return this.format.reduce(Math.imul);
  }
  /*
  Return the norm of the tensor.
  */
  get norm() {
    if (this[0] instanceof Tensor) {
      return this.map(t => t.norm ** Tensor.norm).reduce((a, b) => a + b)**(1/Tensor.norm);
    } else {
      return this.map(t => t ** Tensor.norm).reduce((a, b) => a + b)**(1/Tensor.norm);;
    }
  }
  /*
  Set the value of the tensor to the given tensor.
  */
  set(t) {
    for (let i=0; i<Math.max(t.length, this.length); i++) {
      this[i] = t[i];
    }
  }
  /*
  Set the value of the tensor to the given tensor recursively.
  */
  rset(t) {
    if (t[0] instanceof Array) {
      for (let i = 0; i < this.length; i++) {
        this[i].rset(t[i]);
      }
    } else {
      for (let i = 0; i < this.length; i++) {
        this[i] = t[i];
      }
    }
  }
  // isort(f) {
  //   this.set(this.sort(f));
  // }
  /*
  Adapt the tensor length to the given one, by adding zero-tensors or deleting terms.
  */
  adapt(n) {
    let t = Tensor.copy(this);
    if (n > this.length) {
      for (let i=0; i<n-this.length; i++) {
        t.push(Tensor.zero(...t[0].format));
      }
    } else {
      for (let i=0; i<this.length-n; i++) {
        delete t[t.length-1];
      }
    }
    return t;
  }
  iadapt(n) {
    this.set(this.adapt(n));
  }
  imap(f) {
    for (let i=0; i<this.length; i++) {
      this[i] = f(this[i]);
    }
  }
  /*
  Map that is applied to the lowest elements only.
  */
  rmap(f) {
    if (this[0] instanceof Tensor) {
      return this.map(t => t.rmap(f));
    } else {
      return this.map(f);
    }
  }
  irmap(f) {
    if (this[0] instanceof Tensor) {
      for (let i=0; i<this.length; i++) {
        this[i].irmap(f);
      }
    } else {
      this.imap(f);
    }
  }
  neg() {
    return this.rmap(t => -t);
  }
  ineg() {
    this.irmap(t => -t);
  }
  inv() {
    return this.rmap(t => 1 / t);
  }
  iinv() {
    this.irmap(t => 1 / t);
  }
  floor() {
    return this.rmap(Math.floor);
  }
  ifloor() {
    this.irmap(Math.floor);
  }
  rmul(k) {
    return this.rmap(t => k * t);
  }
  irmul(k) {
    this.irmap(t => k * t);
  }
  rdiv(k) {
    return this.rmap(t => t/k);
  }
  irdiv(k) {
    this.irmap(t => t/k);
  }
  pow(k) {
    return this.rmap(x => x ** k)
  }
  ipow(k) {
    this.irmap(x => x ** k);
  }
  round(k) {
    return this.rmap(x => Math.round(x*10**k)/10**k);
  }
  iround(k) {
    this.irmap(x => Math.round(x*10**k)/10**k);
  }
  fill(k) {
    return this.rmap(t => k);
  }
  ifill(k) {
    this.set(this.fill(k));
  }
  // component wise operations
  map2(tensor, f) {
    let m = Math.max(this.length, tensor.length);
    let v = this.copy();
    if (this[0] instanceof Tensor) {
      for (let i=0; i<m; i++) {
        v[i] = v.map2(tensor[i], f);
      }
    } else {
      for (let i = 0; i < m; i++) {
        v[i] = f(this[i], tensor[i]);
      }
    }
    return v;
  }
  imap2(tensor, f) {
    let m = Math.max(this.length, tensor.length);
    if (this[0] instanceof Tensor) {
      for (let i=0; i<m; i++) {
        this[i].imap2(tensor[i], f);
      }
    } else {
      for (let i = 0; i < m; i++) {
        this[i] = f(this[i], tensor[i]);
      }
    }
  }
  mul(tensor) {
    return this.map2(tensor, (x,y) => x*y);
  }
  imul(tensor) {
    this.imap2(tensor, (x,y) => x*y);
  }
  add(tensor) {
    return this.map2(tensor, (x,y) => x+y);
  }
  iadd(tensor) {
    this.imap2(tensor, (x,y) => x+y);
  }
  radd(k) {
    return this.rmap(t => t+k);
  }
  iradd(k) {
    this.irmap(t => t+k);
  }
  rsub(k) {
    return this.rmap(t => t-k);
  }
  irsub(k) {
    this.irmap(t => t-k);
  }
  sub(tensor) {
    return this.map2(tensor, (x,y) => x-y);
  }
  isub(tensor) {
    this.imap2(tensor, (x,y) => x-y);
  }
  dot(tensor) {
    return Math.sum(this.mul(tensor))
  }
  copy() {
    return this.slice(0);
  }
  /*
  Reshape the tensor to another given format.
  */
  reshape(...format) {
    throw "Most difficult function to implement.";
  }
  flatten() {
    if (this.order == 1) {
      return Tensor.from(this);
    } else {
      let t = new Tensor();
      for (const ti of this) {
        t = t.concat(ti.flatten());
      }
      return t;
    }
  }
}
