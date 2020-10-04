

class Circle {
  constructor(position,velocity,acceleration,radius,color) {
    this.position=position;
    this.velocity=velocity;
    this.acceleration=acceleration;
    this.radius=radius;
    this.color=color;
  }
  move(time) {
    this.velocity[0]+=this.acceleration[0]*time;
    this.velocity[1]+=this.acceleration[1]*time;
    this.position[0]+=this.velocity[0]*time;
    this.position[1]+=this.velocity[1]*time;
  }
  update(time){
    this.move(time);
  }
  show(c){
    c.beginPath();
    c.arc(this.position[0],this.position[1],this.radius,0,Math.PI*2,false);
    c.strokeStyle=this.color;
    c.stroke();
    c.fill();
  }
}



class Game {
  constructor(number=10){
    this.canvas = document.querySelector("canvas");
    this.canvas.width=window.innerWidth;
    this.canvas.height=window.innerHeight;
    this.screen=this.canvas.getContext('2d');
    this.colors=["blue","white","red","green","yellow"];
    this.borders=[this.canvas.width,this.canvas.height]
    this.time=1;
    this.circles=[];

    for(var i=0;i<number;i++){
      var radius=50; //Math.random()*(innerWidth-radius*2)+radius;
      var position=[Math.random()*(this.canvas.width-radius*2)+radius,Math.random()*(this.canvas.height-radius*2)+radius];
      var velocity=[(Math.random()-0.5)*2,(Math.random()-0.5)*2];
      var acceleration=[(Math.random()-0.5)*2,(Math.random()-0.5)*2];

      var color=this.colors[Math.floor(Math.random()*this.colors.length)];
      this.circles.push(new Circle(position,velocity,acceleration,radius,color));
    }
  }

  loop(){
    this.update();
    this.show();
    requestAnimationFrame(this.loop);
    alert("test")
  }

  update(){
    for(var i=0;i<this.circles.length;i++){
      this.circles[i].update(this.time);
      this.affectBorders(this.circles[i]);
    }
  }

  affectBorders(circle){
    if (circle.position[0]+circle.radius>this.borders[0]){
      circle.velocity[0]*=-1;
      circle.position[0]=this.borders[0]-circle.radius;
    }
    if (circle.position[0]-circle.radius<0) {
      circle.velocity[0]*=-1;
      circle.position[0]=circle.radius;
    }
    if (circle.position[1]+circle.radius>this.borders[1]){
      circle.velocity[1]*=-1;
      circle.position[1]=this.borders[1]-circle.radius;
    }
    if (circle.position[1]-circle.radius<0) {
      circle.velocity[1]*=-1;
      circle.position[1]=circle.radius;
    }
  }

  show(){
    this.screen.clearRect(0,0,this.canvas.width,this.canvas.height);
    for(var i=0;i<this.circles.length;i++){
      this.circles[i].show(this.screen);
    }
    //this.canvas.fill
  }

  check(){
    this.on=true;
  }
}



var game=new Game(100);
//game.loop()

function Main(){
  game.update();
  game.show();
  requestAnimationFrame(Main);
}

Main();
