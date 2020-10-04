/*
A motion is a matrix and also a list of vectors.
*/
class Motion extends Matrix {
  static width = 3;
  static height = 2;
  static get length() {return Motion.width};
  static set length(n) {Motion.width = n};
  static get dimension() {return Motion.height};
  static set dimension(n) {Motion.height = n};

  static random(w,h) {
    return new Motion(...Matrix.random(w,h));
  }
  static zero(length=Motion.length) {
    return new Motion(...Matrix.zero(length));
  }
  // constructor(...vectors) {
  //   console.log("motion_constructor:", vectors);
  //   super(...vectors);
  //   console.log(this);
  //   // this.imap(t => new Vector(...t));
  //   for (let i=0; i<this.length; i++) {
  //     this[i] = new Vector(...this[i]);
  //   }
  // }
  get position() {
    return new Vector(...this[0]);
  }
  set position(value) {
    this[0] = value;
  }
  get velocity() {
    return new Vector(...this[1]);
  }
  set velocity(value) {
    this[1] = value;
  }
  get acceleration() {
    return new Vector(...this[2]);
  }
  set acceleration(value) {
    this[2] = v;
  }
  get x() {
    return this[0][0];
  }
  set x(v) {
    this[0][0] = v;
  }
  get y() {
    return this[0][1];
  }
  set y(v) {
    this[0][1] = v;
  }
  get z() {
    return this[0][2];
  }
  set z(v) {
    this[0][2] = v;
  }

  get vx() {
    return this[1][0];
  }
  set vx(v) {
    this[1][0] = v;
  }
  get vy() {
    return this[1][1];
  }
  set vy(v) {
    this[1][1] = v;
  }
  get vz() {
    return this[1][2];
  }
  set vz(v) {
    this[1][2] = v;
  }

  get ax() {
    return this[2][0];
  }
  set ax(v) {
    this[2][0] = v;
  }
  get ay() {
    return this[2][1];
  }
  set ay(v) {
    this[2][1] = v;
  }
  get az() {
    return this[2][2];
  }
  set az(v) {
    this[2][2] = v;
  }
  update(dt=1) {
    for (let x=this.width-2; x>=0; x--) {
      this[x].iadd(this[x+1].rmul(dt));
    }
  }
  updateFriction(friction=0.1) {
    this[1].irmul(1-friction);
  }
}
