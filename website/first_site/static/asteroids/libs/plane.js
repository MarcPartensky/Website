class Plane {
  static location = Motion.zero(3, 2)
  static units = Motion.zero(3, 2);
  static speed = 10;
  constructor(location=Plane.location, units=Plane.units, speed=Plane.speed) {
    this.location = location;
    this.units = units;
    this.speed = speed;
  }
  get position() {
    return this.location.position;
  }
  set position(value) {
    this.location.position = value;
  }
  get velocity() {
    return this.location.velocity;
  }
  set velocity(value) {
    this.location.velocity = value;
  }
  get acceleration() {
    return this.location.acceleration;
  }
  set acceleration(value) {
    this.location.acceleration = value;
  }
  get x() {
    return this.location[0][0];
  }
  set x(value) {
    this.location[0][0] = value;
  }
  get y() {
    return this.location[0][1];
  }
  set y(value) {
    this.location[0][1] = value;
  }
  get vx() {
    return this.location[1][0];
  }
  set vx(value) {
    this.location[1][0] = value;
  }
  get vy() {
    return this.location[1][1];
  }
  set vy(value) {
    this.location[1][1] = value;
  }
  get ax() {
    return this.location[2][0];
  }
  set ax(value) {
    this.location[2][0] = value;
  }
  get ay() {
    return this.location[2][1];
  }
  set ay(value) {
    this.location[2][1] = value;
  }
  get ux() {
    return this.units[0][0];
  }
  set ux(value) {
    this.units[0][0] = value;
  }
  get uy() {
    return this.units[0][1];
  }
  set uy(value) {
    this.units[0][1] = value;
  }
  get uvx() {
    return this.units[1][0];
  }
  set uvx(value) {
    this.units[1][0] = value;
  }
  get uvy() {
    return this.units[1][1];
  }
  set uvy(value) {
    this.units[1][1] = value;
  }
  get uax() {
    return this.units[2][0];
  }
  set uax(value) {
    this.units[2][0] = value;
  }
  get uay() {
    return this.units[2][1];
  }
  set uay(value) {
    this.units[2][1] = value;
  }
  toScreen(position) {
    return position.sub(this.location.position).tdot(this.units.position);
  }
  fromScreen(position) {
    return position.tdot(this.units.position.map(x => 1/x)).add(this.location.position);
  }
  zoom(value) {
    this.units[0].irmul(value);
  }
}
