var canvas = document.querySelector("canvas");

canvas.width=window.innerWidth;
canvas.height=window.innerHeight;

var c=canvas.getContext('2d');

var cross= function(l1,l2) { //y=a1*x+b1 and y=a2*x+b2
  x=(l2.b-l1.b)/(l1.a-l2.a);
  y=(l1.a*x+l1.b);
  return [x,y];
}


function Point(x,y,radius=5,color="white") {
  this.x=x;
  this.y=y;
  this.color=color;
  this.radius=radius;
  this.draw = function() {
    c.beginPath();
    c.arc(this.x,this.y,this.radius,0,Math.PI*2,false);
    c.strokeStyle=this.color;
    c.stroke();
    c.fill();
  }
  this.contact=function(x,y) {
    return Math.sqrt((this.x-x)**2+(this.y-y)**2)<=this.radius*2;
  }
}

function Line(p1,p2,color="white") {
  this.p1=p1;
  this.p2=p2;
  this.color=color;
  this.update = function() { //y=ax+b => b=y-ax
    this.a=(this.p2.y-p1.y)/(this.p2.x-this.p1.x);
    this.b=this.p1.y-this.a*this.p1.x;
  }
  this.draw = function() {
    x1=0;
    y1=this.b;
    x2=canvas.width;
    y2=canvas.width*this.a+this.b;
    c.beginPath();
    c.moveTo(x1,y1);
    c.lineTo(x2,y2);
    c.strokeStyle=this.color;
    c.stroke();
  }
}

function Segment(p1,p2,color="white") { //y=ax+b => b=y-ax
  this.x=[min(p1.x,p2.x),max(p1.x,p2.x)]
  this.y=[min(p1.y,p2.y),max(p1.y,p2.y)]
  this.a=(p2.y-p1.y)/(p1.x-p2.x);
  this.b=p1.y-this.a*p1.x;
  this.color=color;
  this.draw = function() {
    x1=0;
    y1=this.b1;
    x2=canvas.width;
    y2=canvas.width*this.a+this.b;
    c.beginPath();
    c.moveTo(x1,y1);
    c.lineTo(x2,y2);
    c.strokeStyle=this.color;
    c.stroke();
  }
}

function Vector(x,y,color="white") {
  this.x=x;
  this.y=y;
  this.norm=Math.sqrt(this.x**2+this.y**2);
  if      (this.x>0) {this.angle=Math.atan(this.y/this.x);}
  else if (this.x<0) {this.angle=Math.atan(this.y/this.x)+Math.PI;}
  else               {this.angle=0;}

  this.apply=function(p){
    p.x=p.x+this.x;
    p.y=p.y+this.y;
  }
  this.project=function(p) {

  }
  this.crossProduct=function(v) {
    return v.x*this.x+v.y*this.y;
  }
  this.draw=function() {

  }
}


var mouse={
  x:undefined,
  y:undefined,
  focus:undefined
}


window.addEventListener("mousemove",
  function(event) {
    mouse.x=event.x;
    mouse.y=event.y;
  }
)



c.onclick = function() {
  mouse.focus=undefined;
  for(var i=0; i<points.length; i++){
    if(points[i].contact(mouse.x,mouse.y)) {mouse.focus=i;}
  }
  console.log('Click just happened');
};



var p1=new Point(0,0);
var p2=new Point(0,1);
var p3=new Point(1,0);
var p4=new Point(1,1);

var points=[p1,p2,p3,p4];

var reverse=new Vector(0,-1);
var center=new Vector(canvas.width/2,canvas.height/2);



//alert(l1.a);
//alert(l2.a);

center.apply(p1);
center.apply(p2);
center.apply(p3);
center.apply(p4);

var l1=new Line(p1,p4);
var l2=new Line(p2,p3);




function Main(){
  //mouse.click=false;
  c.clearRect(0,0,canvas.width,canvas.height);
  p1.draw();
  p2.draw();
  p3.draw();
  p4.draw();
  p2.x=mouse.x;
  p2.y=mouse.y;
  l1.update();
  l2.update();
  l1.draw();
  l2.draw();
  if(mouse.click){alert("user clicked");}
  requestAnimationFrame(Main);
}

Main();
