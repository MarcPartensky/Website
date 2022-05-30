var canvas  = document.querySelector('canvas');
var context = canvas.getContext('2d');

// var width = 10;
// var height = 10;

// context.translate(canvas.width/2, canvas.height/2);
// context.scale(canvas.width/width, canvas.height/height);
// scaling in javascript is useless because the canvas is already rasterized


class Vector extends Array {
  static distance(v1, v2) {
    v = v1.sub(v2);
    return v.norm;
  }
  static random(width, height) {
    var x = Math.floor(width * Math.random());
    var y = Math.floor(height * Math.random());
    return new Vector([x, y]);
  }
  constructor(components, color="white") {
    this.components = components;
    this.color = color;
  }
  get x() {
    return this.components[0];
  }
  set x(v) {
    this.components[0] = v;
  }
  get y() {
    return this.components[1];
  }
  set y(v) {
    this.components[1] = v;
  }
  get z() {
    return this.components[2];
  }
  set z(v) {
    this.components[2] = v;
  }
  get norm() {
    return Math.sum(this.components.map(x => x*x));
  }
  show(context) {
    // Not showable for now.
  }
  neg() {
    const components = [];
    this.components.forEach(component => {
      components.push(-component);
    });
    return new Vector(components);
  }
  add(vector) {
    length = Math.max(this.components.length, vector.components.length);
    const components = [];
    for (let i=0; i<length; i++) {
      components.push(this.components[i]+vector.components[i]);
    }
    return new Vector(components);
  }
  sub(vector) {
    return this.add(vector.neg())
  }
  rmul(scalar) {
    const components = [];
    this.components.forEach(component => {
      components.push(scalar * component);
    });
    return new Vector(components);
  }
}


class Point extends Vector {
  static random(width, height) {
    var x = Math.floor(width * Math.random());
    var y = Math.floor(height * Math.random());
    return new Point([x, y]);
  }
  show(context) {
    context.putImageData(monImageData, this.x, this.y);
  }
}


class Segment {
  /**
  * Create a segment with the points p1 and p2.
  */
  constructor (p1, p2, color="white") {
    this.p1 = p1;
    this.p2 = p2;
    this.color = color;
  }
  /**
  * Show the segment on the context.
  */
  show(context) {
    context.strokeStyle = this.color;
    context.beginPath();
    context.moveTo(this.p1.x, this.p1.y);
    context.lineTo(this.p2.x, this.p2.y);
    context.closePath();
    context.stroke();
  }
}


class Rect {
  static random(w, h, color="white", fill=false) {
    var x = Math.floor(w * Math.random());
    var y = Math.floor(h * Math.random());
    var width = Math.floor(w * Math.random());
    var height = Math.floor(h * Math.random());
    return new Rect(x, y, width, height, color, fill);
  }
  /**
  * Create a rect using xmin, ymin, xmax, ymax
  * and optional color.
  */
  constructor(x, y, width, height, color="white", fill=false) {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    this.color = color;
    this.fill = fill;
  }
  /**
  * Show the rect on the context.
  */
  show(context) {
    context.strokeWidth = "1px";
    if (this.fill) {
      context.fillStyle = this.color;
      context.fillRect(this.x, this.y, this.width, this.height);
    } else {
      context.strokeStyle = this.color;
      context.strokeRect(this.x, this.y, this.width, this.height);
    }
  }

  getCenter() {
    var x = this.x + this.width/2;
    var y = this.y + this.height/2;
    return [x, y];
  }

  setCenter(vector) {
    this.x = vector.x - this.width/2;
    this.y = vector.y - this.height/2;
  }
}


class Squa extends Rect {
  constructor(x, y, size) {
    this.x = x;
    this.y = y;
    this.size = size;
  }
  get width() {
    return this.size;
  }
  get height() {
    return this.size;
  }
}


class Polygone {
  /**
  * Create a polygone using the list of points
  * and optional color and fill arguments.
  */
  constructor(points, color="white", fill=false) {
    this.points = points;
    this.color = color;
    this.fill = fill;
  }
  /**
  * Show the polygone on the context.
  */
  show(context) {
    if (this.points.length > 1) {
      context.beginPath();
      var start = this.points[0];
      context.moveTo(start.x, start.y);
      for (var point of this.points) {
        context.lineTo(point.x, point.y);
      }
      context.closePath();
      if (this.fill) {
        context.fillStyle = this.color;
        context.fill();
      } else {
        context.strokeStyle = this.color;
        context.stroke();
      }
    }
  }
  /**
  * Show all the points.
  */
  showPoints(context) {
    this.points.forEach(function(point) {
      point.show(context)
    });
  }
}

class Rectangle extends Polygone {
  constructor() {

  }
}

class Sprite extends Rect {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }
}


var mouse= {x:undefined, y:undefined}
window.addEventListener("resize",
  function() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
)
window.addEventListener("mousemove",
  function(event) {
    mouse.x = event.x;
    mouse.y = event.y;
  }
)

var p1 = Point.random(canvas.width, canvas.height);
var p2 = Point.random(canvas.width, canvas.height);
var p3 = Point.random(canvas.width, canvas.height);
alert(Point.distance(p1, p2));
var s = new Segment(p1, p2);
var r = Rect.random(canvas.width, canvas.height, color="yellow");
var pl = new Polygone([p1, p2, p3], color="red", fill=false);


function colorize() {
  var colors = ["white", "black", "blue", "red", "green", "yellow"];
  for (var y=0; y<canvas.height; y++) {
    for (var x=0; x<canvas.width; x++) {
      context.fillStyle = colors[Math.floor(Math.random()*colors.length)];
      context.fillRect(x,y,1,1);
    }
  }
}


function animate() {
  requestAnimationFrame(animate);
  context.clearRect(0, 0, canvas.width, canvas.height);
  s.show(context);
  r.setCenter(mouse);
  r.show(context);
  pl.show(context);
}

animate();
