class Game {
  static dt = 0.1;
  static font = "Arial";
  static index = 0;
  static maps = [];
  static precision = 5;
  static random() {
    return new this([GameMap.random()]);
  }
  constructor(
    maps=Game.maps,
    dt=Game.dt,
    font=Game.font,
    index=Game.index,
    open=Game.open,
    precision=Game.precision
  ) {
    this.maps = maps;
    this.dt = dt;
    this.font = font;
    this.index = index;
    this.open = open;
    this.map = this.maps[this.index];
    this.precision = precision;
  }
  updateMap() {
    this.map = this.maps[this.index];
  }
  update(dt) {
    this.map.update(dt);
  }
  show(context) {
    this.map.show(context);
  }
  getStream() {
    let stream = [];
    let playerStream;
    let ballStream;
    let ballStreams=[];
    for (const [id, player] of this.map.group.players) {
      playerStream = id + "///";
      for (const ball of player.balls) {
        ballStream = "";
        ballStream += String(ball.position.round(this.precision));
        ballStream += "/";
        ballStream += String(ball.velocity.round(this.precision));
        ballStream += "/";
        ballStream += String(round(ball.radius, this.precision));
        ballStreams.push(ballStream);
      }
      playerStream += ballStreams.join("//");
      stream.push(playerStream);
    }
    return stream.join("|");
  }
  setStream(stream) {
    let id, strballs;
    let player;
    let strposition, strvelocity, strradius;
    let position, velocity, motion;
    let ball;
    let x,y;
    for (const strplayer of stream.split("|")) {
      [id, strballs] = strplayer.split("///");
      console.log(id);
      player = this.map.group.players.get(id);
      if (player) {
        player = new Player(player.name, player.color);
      } else {
        player = Player.random();
      }
      player.balls = [];
      for (const strball of strballs.split("//")) {
        [strposition, strvelocity, strradius] = strball.split("/");
        [x, y] = strposition.split(",");
        position = new Vector(Number(x), Number(y));
        [x, y] = strvelocity.split(",");
        velocity = new Vector(Number(x), Number(y));
        motion = new Motion(position, velocity);
        ball = Ball.from(motion, player.radius);
        player.balls.push(ball);
      }
      this.map.group.players.set(id, player);
    }
  }
}