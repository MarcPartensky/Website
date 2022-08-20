class Body extends Tensor {
  static length = 1;
  static format = [2,2];
  static random(length=this.length, format=this.format) {
    let motions = Array(length);
    for (let i=0; i<length; i++) {
      motions[i] = Motion.random(...format);
    }
    return this.from(motions);
  }
  get motion() {
    return this[0];
  }
  set motion(value) {
    this[0] = value;
  }
  get moment() {
    return this[1];
  }
  set moment(value) {
    this[1] = value;
  }
  get x() {
    return this.motion.x;
  }
  set x(v) {
    this.motion.x = v;
  }
  get y() {
    return this.motion.y;
  }
  set y(v) {
    this.motion.y = v;
  }
  get z() {
    return this.motion.z;
  }
  set z(v) {
    this.motion.z = v;
  }
  get vx() {
    return this.motion.vx;
  }
  set vx(v) {
    this.motion.vx = v;
  }
  get vy() {
    return this.motion.vy;
  }
  set vy(v) {
    this.motion.vy = v;
  }
  get vz() {
    return this.motion.vz;
  }
  set vz(v) {
    this.motion.vz = v;
  }
  get ax() {
    return this.motion.ax;
  }
  set ax(v) {
    this.motion.ax = v;
  }
  get ay() {
    return this.motion.ay;
  }
  set ay(v) {
    this.motion.ay = v;
  }
  get az() {
    return this.motion.az;
  }
  set az(v) {
    this.motion.az = v;
  }
  get position() {
    return this.motion.position;
  }
  set position(v) {
    this.motion.position = v;
  }
  get velocity() {
    return this.motion.velocity;
  }
  set velocity(v) {
    this.motion.velocity = v;
  }
  get acceleration() {
    return this.motion.acceleration;
  }
  set acceleration(v) {
    this.motion.acceleration;
  }
  update(dt) {
    this.map(motion => motion.update(dt));
  }
  updateFriction(friction) {
    for (const motion of this) {
      motion.updateFriction(0.1);
    }
  }
  follow(vector) {
    let norm = vector.sub(this.position).norm;
    // norm = sigmoid(norm);
    norm = Math.min(Math.max(0, norm),1);
    let angle = vector.sub(this.position).angle;
    this.motion.velocity = Vector.polar(norm, angle);
  }
  limit(vmin, vmax) {
    this.motion[0].limit(vmin, vmax);
  }
}
