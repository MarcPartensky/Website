var canvas = document.querySelector("canvas");

canvas.width=window.innerWidth;
canvas.height=window.innerHeight;

var c=canvas.getContext('2d');

//alert("made it there");
//console.log("should do something here");

/*

c.fillStyle="rgba(0,255,0,0.5)";
c.fillRect(100,100,100,100);
c.fillStyle="rgba(0,255,255,0.5)";
c.fillRect(200,100,100,100);

console.log(canvas);

//Line
c.beginPath();
c.moveTo(50,300);
c.lineTo(300,100);
c.lineTo(400,300);
c.strokeStyle="blue";
c.stroke();


//window.alert("test");
//Arc / Circle

c.beginPath();
c.art(300,300,30,0,Math.PI*2,false)
c.strokeStyle="blue";
c.stroke();


//Math.random

//a=canvas.width/7
//b=canvas.height/6

//c.beginPath();
//c.fillStyle="rgba(0,255,255,0.5)";

for (var i=0; i<1000; i++){
  var x = Math.random()*window.innerWidth;
  var y = Math.random()*window.innerHeight;
  c.beginPath();
  c.arc(x,y,30,0,Math.PI*2,false);
  c.strokeStyle='blue';
  c.stroke();
}

for (var y = 0; y < 6; y++) {
  for (var x = 0; x < 7; x++) {

      c.fillRect(x*a,y*b,a,b);
  }
}
*/


//alert("made it there");

var mouse= {
  x:undefined,
  y:undefined
}

window.addEventListener("resize",
  function() {
    canvas.width=window.innerWidth;
    canvas.height=window.innerHeight;
  }
)

window.addEventListener("mousemove",
  function(event) {
    mouse.x=event.x;
    mouse.y=event.y;
  }
)

function Circle(x,y,dx,dy,radius,color) {
  this.x=x;
  this.y=y;
  this.dx=dx;
  this.dy=dy;
  this.radius=radius
  this.color=color;
  this.state=0;


  this.draw = function() {
    c.beginPath();
    c.arc(this.x,this.y,this.radius,0,Math.PI*2,false);
    c.strokeStyle=this.color;
    c.stroke();
    c.fill();
  }

  this.update = function() {
    if (this.x+this.radius>innerWidth || this.x-this.radius<0) {
      this.dx*=-1;
    }

    if (this.y+this.radius>innerHeight || this.y-this.radius<0) {
      this.dy*=-1;
    }

    this.state+=1;

    //this.dr=Math.cos(this.state/100*2*Math.PI);
    //this.radius+=this.dr;

    this.x+=this.dx;
    this.y+=this.dy;
  }

  this.act=function() {
    if (Math.sqrt((mouse.x-this.x)**2+(mouse.y-this.y)**2)<100) {
      this.radius+=1;
    } else if (this.radius>5) {
      this.radius-=1;
    }
  }

}



function animate() {
  requestAnimationFrame(animate);
  //c.clearRect(0,0,innerWidth,innerHeight);

  for (var i=0; i<circleArray.length; i++) {
    circleArray[i].act();
    circleArray[i].update();
    circleArray[i].draw();

  }


}


var circleArray=[]
var colorArray=["blue","white","red","green","yellow"]

for (var i=0; i<100; i++) {
  var radius = Math.random()*50;
  var radius=20;
  var x = Math.random()*(innerWidth-radius*2)+radius;
  var y = Math.random()*(innerHeight-radius*2)+radius;
  var dx = (Math.random()-0.5)*2*10;
  var dy = (Math.random()-0.5)*2*10;
  var color=colorArray[Math.floor(Math.random()*colorArray.length)];

  var circle = new Circle(x,y,dx,dy,radius,color);
  circleArray.push(circle)
}



animate()

//alert("testing");
