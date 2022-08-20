import Tensor from "./tensor.js";
import Motion from "./motion.js";
import Vector from "./vector.js";

export default class Body extends Tensor {
  static n = 1;
  static w = 2;
  static h = 2;
  static random(n=Body.n, w=Body.w, h=Body.h) {
    let motions = new Tensor(n);
    for (let i=0; i<n; i++) {
      motions[i] = Motion.random(w, h);
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
    for (let i=0; i<this.length; i++) {
      this[i].update(dt);
    }
    // this.updateFriction(0.1)
    // this.map(motion => motion.update(dt));
  }
  updateFriction(friction=0.1) {
    for (const motion of this) {
      motion.updateFriction(friction);
    }
  }
  follow(vector) {
    let norm = vector.sub(this.position).norm/10;
    // norm = sigmoid(norm);
    // norm = Math.min(Math.max(0, norm),1);
    let angle = vector.sub(this.position).angle;
    // this[0][2].angle = angle;
    this[0][2] = Vector.polar(norm, angle);
    // this.motion.acceleration = Vector.polar(norm, angle);
  }
  limit(vmin, vmax) {
    this.motion[0].limit(vmin, vmax);
  }
}
