var canvas = document.getElementById("canvas");

var context = new ContextAdapter(canvas.getContext("2d"));


context.width = canvas.width = window.innerWidth;
context.height = canvas.height = window.innerHeight;

context.plane.units.position = new Vector(0.2, 0.2);

// var host = String(document.location);
// var name = prompt("name");
// var socket = io.connect(host, {query: "name="+name});
var group = new SuperGroup();
var game = new Game(canvas, group);
game.main();