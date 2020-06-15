var canvas  = document.querySelector('#canvas');
var context = canvas.getContext('2d');

function resize() {
  context.width = canvas.width = window.innerWidth;
  context.height = canvas.height = window.innerHeight;
}

class Game {
  /**
  * Create an array using its width, height and the value of all cases.
  */
  static createGrid(width, height, value) {
    var grid = [];
    for (var y=0; y<height; y++) {
      var line = [];
      for (var x=0; x<width; x++) {
        line.push(value);
      }
      grid.push(line);
    }
    return grid;
  }

  /**
  * Create a connect4 game using optional width and size
  */
  constructor(width=7, height=6) {
    this.over = false;
    this.width = width;
    this.height = height;
    this.grid = Game.createGrid(this.width, this.height, 0);
    this.state = 0;
    this.connection = 4;
    this.choice = undefined;
    this.line = undefined;
    this.lineWidth = 1/100;
    this.winningLineColor = "lightgreen";
    this.winningLineWidth = 3/100;
    this.emptyTokenColor = "white";
    this.tokenColors = ["yellow", "red"];
    this.case_ratio = 0.8;
    this.case_color = "white";
  }

  contains(x, y) {
    return 0<=x && x<this.width && 0<=y && y<this.height;
  }

  /**
  * Determine if the last move is a winning move, and returns it.
  */
  searchWinnerFrom(px, py) {
    for (var d of [[-1, 0], [-1,-1], [0,-1], [1,-1]]) {
      var dx = d[0]; var dy=d[1];
      var lim1 = this.getLimit(px, py, dx ,dy);
      var lim2 = this.getLimit(px, py, -dx, -dy);
      var line = this.makeLine(lim1, lim2);
      if (line.length>=this.connection) {
        this.line = {lim1:lim1, lim2:lim2};
        return true;
      }
    }
    return false;
  }
  /**
  * Check if all tokens are the same when going in one direction,
  * and return the position of the last same token before finding
  * either another token, an empty case or a wall.
  */
  getLimit(px, py, dx, dy) {
    var x = px;
    var y = py;
    var token = this.grid[y][x];
    while (true) {
      if (!this.contains(x+dx, y+dy)) break;
      if (this.grid[y+dy][x+dx] != token) break;
      x += dx;
      y += dy;
    }
    return {x:x, y:y};
  }

  /**
  * Return the segment using its 2 extremities under the form of
  * an array of positions.
  */
  makeLine(lim1, lim2) {
     if (lim2.x-lim1.x>0) {
       var dx = 1;
     } else if (lim2.x-lim1.x<0) {
       var dx = -1;
     } else {
       var dx = 0;
     }
     if (lim2.y-lim1.y>0) {
       var dy = 1;
     } else if (lim2.y-lim1.y<0) {
       var dy = -1;
     } else {
       var dy = 0;
     }
    var x = lim1.x;
    var y = lim1.y;
    var l = [[x,y]];
    while (x!=lim2.x || y!=lim2.y) {
      x+=dx;
      y+=dy;
      l.push([x,y]);
    }
    return l;
  }

  /**
  * Determine if the grid is full.
  */
  isFull() {
    var full = true;
    for (var y=0; y<this.height; y++) {
      for (var x=0; x<this.width; x++) {
        if (this.grid[y][x]==0) {
          full=false;
        }
      }
    }
    return full;
  }

  /**
  * Determine if the game is over.
  */
  isOver() {
    if (this.isFull()) {
      return true;
    } else if (this.searchWinnerFrom(this.choice.x, this.choice.y)){
      return true;
    } else {
      return false;
    }
  }

  /**
  * Show the game.
  */
  show(context, mouse) {
    var m = Math.min(context.width, context.height);
    context.lineWidth = this.lineWidth*m;
    this.showBackground(context);
    this.showGrid(context);
    this.showCurrentChoice(context, mouse);
    if (this.over) {
      this.showWinningLine(context);
    }
  }

  /**
  *
  */
  showCurrentChoice(context, mouse) {
    var x = Math.floor(mouse.x/context.width*game.width);
    var y = game.height-1;
    if (!game.grid[y][x]) {
      game.showToken(context, x, y, game.getToken(), "lightblue");
    }
  }

  /**
  * Show the background of the game.
  */
  showBackground(context) {
    context.fillStyle = "blue";
    context.fill();
  }

  /**
  * Show the grid of the game.
  */
  showGrid(context) {
    for (var y=0; y<this.height; y++) {
      for (var x=0; x<this.width; x++) {
        this.showToken(context, x, y, this.grid[y][x]);
      }
    }
  }

  /**
  *
  */
  showWinningLine(context) {
    var m = Math.min(context.width, context.height);
    context.strokeStyle = this.winningLineColor;
    context.lineWidth = this.winningLineWidth*m;
    context.beginPath();
    context.moveTo((this.line.lim1.x+1/2)*context.width/this.width,
                   (this.height-(this.line.lim1.y+1/2))*context.height/this.height);
    context.lineTo((this.line.lim2.x+1/2)*context.width/this.width,
                   (this.height-(this.line.lim2.y+1/2))*context.height/this.height);
    context.stroke();
  }

  /**
  * Show a given token.
  */
  showToken(context, x, y, token, strokeStyle="black") {
    context.strokeStyle = strokeStyle;
    if (token==0) {
      context.fillStyle = "white";
    } else if (token==1) {
      context.fillStyle = "yellow";
    } else if (token==2){
      context.fillStyle = "red";
    }
    var min_context = Math.min(context.width, context.height);
    var max_grid = Math.max(this.width, this.height);
    var r = min_context/max_grid*this.case_ratio/2;
    context.beginPath();
    context.arc((x+1/2)*context.width/this.width,
                context.height-(y+1/2)*context.height/this.height,
                r, 0, 2*Math.PI);
    context.fill();
    context.stroke();
    if (token!=0) {
      context.beginPath();
      context.arc((x+1/2)*context.width/this.width,
                  context.height-(y+1/2)*context.height/this.height,
                  r*2/3, 0, 2*Math.PI);
      context.stroke();
    }
  }

  /**
  * Play the game.
  */
  play(choice) {
    var token = this.getToken();
    if (this.choose(choice, token)) {
      this.state++;
      this.over = this.isOver();
      return true;
    } else {
      alert("You can't play here! This column is already full.")
      return false;
    }
  }

  /**
  * Choose given position with a given token.
  */
  choose(x, token) {
    for (var y=0; y<this.height; y++) {
      if (this.grid[y][x]==0) {
        this.grid[y][x] = token;
        this.choice = {x:x, y:y};
        return true;
      }
    }
    return false;
  }

  /**
  * Return the current turn
  */
  getTurn() {
    return this.state%2;
  }

  /**
  * Return the current token.
  */
  getToken() {
    return this.getTurn()+1;
  }
}

var mouse = {x: 0, y: 0};
var game = new Game();
resize();
game.show(context, mouse);

window.addEventListener("resize",resize);

window.addEventListener("click",
  function() {
    var choice = Math.floor(mouse.x*game.width/context.width);
    if (game.over) {
      alert("The game is over.\n You can refresh the page to start a new game.");
    }
    if (!game.over) {
      if (game.play(choice)) {
        game.show(context, mouse);
      }
    }
  }
);

window.addEventListener("mousemove",
  function(event) {
    mouse.x=event.x;
    mouse.y=event.y;
    game.show(context, mouse);
  }
)
