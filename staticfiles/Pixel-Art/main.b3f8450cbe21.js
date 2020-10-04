class Board {
  static createGrid(width, height, value) {
    let grid = [];
    for (let y=0; y<height; y++) {
      let line = [];
      for (let x=0; x<width; x++) {
        line.push(value);
      }
      grid.push(line);
    }
    return grid;
  }
  constructor(width=8, height=8, color="#eeeeee", mg=1) {
    this.width = width;
    this.height = height;
    this.grid = Board.createGrid(width, height, color);
    this.mg = mg;
  }
  show(context) {
    let W = context.width/this.width;
    let H = context.height/this.height;
    let S = Math.min(W, H);
    for (let y=0; y<this.height; y++) {
      for (let x=0; x<this.width; x++){
        let X = x*S;
        let Y = y*S;
        context.fillStyle = this.grid[y][x];
        context.fillRect(X, Y, S+this.mg, S+this.mg);
      }
    }
  }
  setPixel(x, y, color) {
    this.grid[y][x] = color;
    console.log("board.setPixel:color", this.grid[y][x]);
  }
  get code() {
    return this.grid.map(t => t.join()).join();
  }
}

class Brush {
  constructor(x, y, color="#222222", size=1, mg=1) {
    this.x = x;
    this.y = y;
    this.color = color;
    this.size = size;
    this.down = false;
    this.mg = 1;
  }
  update() {
    brush.color = document.getElementById("color").value;
    console.log("brush.update:color", brush.color)
  }
  show(context, width, height) {
    let W = context.width/width;
    let H = context.height/height;
    let S = Math.min(W, H);
    let K = Math.min(width, height);
    // context.strokeStyle = color;
    // context.beginPath();
    // context.arc(this.x*S, this.y*S, this.size*S/2, 0, 2*Math.PI);
    // context.stroke();
    context.fillStyle = this.color;
    context.fillRect(this.x*S, this.y*S, S+this.mg, S+this.mg);
  }
}

function draw() {
    let rect = canvas.getBoundingClientRect();
    let W = board.width/rect.width;
    let H = board.height/rect.height;
    let S = Math.min(W, H);
    let x = Math.min(parseInt(brush.x * S), board.width-1);
    let y = Math.min(parseInt(brush.y * S), board.height-1);
    board.setPixel(x, y, brush.color);
}

function show() {
  board.show(context);
  brush.show(context, board.width, board.height);
}

function resize() {
    value = Math.min(window.innerWidth*0.9, window.innerHeight*0.9)
    console.log(value)
    context.width = canvas.width = context.height = canvas.height = value;
    show()
}

let canvas = document.getElementById("canvas");
let context = canvas.getContext("2d");

let board = new Board(8,8);
let brush = new Brush();

canvas.addEventListener("mousemove",
  function(event) {
    let rect = canvas.getBoundingClientRect();
    brush.x=event.x - rect.left;
    brush.y=event.y - rect.top;
    if (brush.down) {
        draw();
    }
    show()
})

canvas.addEventListener("mouseenter", brush.update)
canvas.addEventListener("mousedown", function() {
    draw()
    show()
    console.log("clicking")
})

window.addEventListener("mousedown", function() {
    brush.down = true;
})

window.addEventListener('resize', resize)

window.addEventListener("mouseup", function() {
    brush.down = false;
})


resize()
brush.update()
