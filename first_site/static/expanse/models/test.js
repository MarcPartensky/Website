var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");



function resize() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}

function loop() {
  m.show(context);
}

function main(e) {
  resize();
  m = new Map(50, 50);
  m.generate();
  requestAnimationFrame(loop);
}

document.addEventListener("DOMContentLoaded", main);
