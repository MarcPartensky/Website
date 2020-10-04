console.log("inside app.js");


var canvas = document.getElementById("canvas");
var engine = new BABYLON.Engine(canvas, true);
var scene = new BABYLON.Scene(engine);
scene.collisionsEnabled = true;
// scene.gravity = new BABYLON.Vector3(0, -9.81, 0);

scene.clearColor = new BABYLON.Color3(0,0,0);
var camera = new BABYLON.FreeCamera("camera", new BABYLON.Vector3(0, 0, 0), scene);
// var player = BABYLON.Mesh.CreateBox("player", 3, scene);
var player = BABYLON.MeshBuilder.CreateSphere("player", {diameter: 3}, scene)
// player.scaling.x=2;
// player.scaling.y=2;
// player.scaling.z=2;
player.position.z = -10
player.position.y = 10;
player.checkCollisions = true;

// var ground = B

var light = new BABYLON.HemisphericLight("light1", new BABYLON.Vector3(0, 10, 0), scene);
var speed = 20;
var pointerLock = false;
let k = 100;
var seed = parseInt(k*Math.random());

var boxes = [];
var n = 50;

function createBox(id, x, y, z, sx=1/3, sy=1/3, sz=1/3) {
  var box = BABYLON.Mesh.CreateBox(id, 3, scene);
  var material = new BABYLON.StandardMaterial("dirt", scene);
  box.material = material;
  box.diffuseTexture = new BABYLON.Texture("dirt.png", scene);
  box.diffuseTexture.uScale = 8.0;
  box.diffuseTexture.vScale = 8.0;
  box.scaling.x = sx;
  box.scaling.y = sy;
  box.scaling.z = sz;
  box.position.x = x;
  box.position.y = y;
  box.position.z = z;
  box.checkCollisions = true;
  box.checkUpdate = false;
  boxes.push(box);
}

function createBoxes() {
  let width = 50;
  let length = 50;
  let lambda = 1/10;
  let height;
  let k = 10;
  let y;
  for (let x=0; x<width; x++) {
    for (let z=0; z<length; z++) {
      height = parseInt(k*(1+noise.perlin2(x*lambda+seed, z*lambda+seed)));
      // let height = 1
      // for (let y=0; y<height; y++) {
        // createBox("box("+x+"-"+y+"-"+z+")", x, y, z);
      // }
      y = height;
      createBox("box("+x+"-"+y+"-"+z+")", x, y, z);
      createBox("box("+x+"-"+y-1+"-"+z+")", x, y-1, z);
    }
  }
}

console.log("made it here");
createBoxes();
// createBox("box", 0, 0 , 0);
console.log("made it there");


player.movement = {forward: false, backward:false, left:false, right:false};

var mouse = {x:undefined, y:undefined, down:false}
var mouseSensibility = 0.5;

function resize() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}

var angleRatio = 180/Math.PI;
function toRadian(angle) {return angle/angleRatio;}
function toDegree(angle) {return angle*angleRatio;}

function onMouseMotion(evt) {
  mouse.x = evt.clientX;
  mouse.y = evt.clientY;
  camera.rotation.x += toRadian(evt.movementY) * mouseSensibility;
  camera.rotation.y += toRadian(evt.movementX) * mouseSensibility;
}

function onMouseDown() {
  mouse.down = true;
}

function onMouseUp() {
  mouse.down = false;
}

function move(fps) {
  relativeSpeed = speed / fps;
  if (player.movement.forward) {
    forward = new BABYLON.Vector3(
      parseFloat(Math.sin(parseFloat(player.rotation.y))) * relativeSpeed,
      0,
      parseFloat(Math.cos(parseFloat(player.rotation.y))) * relativeSpeed,
    );
    player.moveWithCollisions(forward);
  }
  if(player.movement.backward){
    backward = new BABYLON.Vector3(
      parseFloat(-Math.sin(parseFloat(player.rotation.y))) * relativeSpeed,
      0,
      parseFloat(-Math.cos(parseFloat(player.rotation.y))) * relativeSpeed
    );
    player.moveWithCollisions(backward);
  }
  if(player.movement.left){
    left = new BABYLON.Vector3(
      parseFloat(Math.sin(parseFloat(player.rotation.y) + toRadian(-90))) * relativeSpeed,
      0,
      parseFloat(Math.cos(parseFloat(player.rotation.y) + toRadian(-90))) * relativeSpeed
    );
    player.moveWithCollisions(left);
  }
  if(player.movement.right){
    right = new BABYLON.Vector3(
      parseFloat(-Math.sin(parseFloat(player.rotation.y) + toRadian(-90))) * relativeSpeed,
      0,
      parseFloat(-Math.cos(parseFloat(player.rotation.y) + toRadian(-90))) * relativeSpeed
    );
    player.moveWithCollisions(right);
  }
  if(player.movement.up){
    up = new BABYLON.Vector3(
      0,
      relativeSpeed,
      0,
    );
    player.moveWithCollisions(up);
  }
  if(player.movement.down){
    down = new BABYLON.Vector3(
      0,
      -relativeSpeed,
      0,
    );
    player.moveWithCollisions(down);
  }
}

function onKeyDown(evt) {
    switch(evt.keyCode){
        case 87: // KeyW
          player.movement.forward = true;
          break;
        case 90: // KeyW
          player.movement.forward = true;
          break;
        case 83: // KeyS
          player.movement.backward = true;
          break;
        case 65: // KeyA
          player.movement.left = true;
          break;
        case 81: // KeyA
          player.movement.left = true;
          break;
        case 68: // KeyD
          player.movement.right = true;
          break;
        case 32: // SpaceBar
          player.movement.up = true;
          break;
        case 38: // ArrowUp
          player.movement.up = true;
          break;
        case 40: // ArrowDown
          player.movement.down = true;
          break;
        case 27: // EscapeBar
          console.log("escape");
          pointerLock = false;
          onPointerLockChange();
          break;
    }
  }

  function onKeyUp(evt) {
      switch(evt.keyCode){
          case 87: // KeyW
            player.movement.forward = false;
            break;
          case 90: // KeyW
            player.movement.forward = false;
            break;
          case 83: // KeyS
            player.movement.backward = false;
          break;
          case 65: // KeyA
            player.movement.left = false;
            break;
          case 81: // KeyA
            player.movement.left = false;
            break;
          case 68: // KeyD
            player.movement.right = false;
            break;
          case 32: // SpaceBar
            player.movement.up = false;
            break;
          case 38: // ArrowUp
            player.movement.up = false;
            break;
          case 40: // ArrowDown
            player.movement.down = false;
            break;
      }
    }

function onPointerLockChange() {
  if (pointerLock) {
    canvas.addEventListener('mousemove', onMouseMotion);
    canvas.addEventListener('mousedown', onMouseDown);
    canvas.addEventListener('mouseup', onMouseUp);
    canvas.addEventListener("keydown", onKeyDown);
    canvas.addEventListener("keyup", onKeyUp);
    canvas.requestPointerLock();
  } else {
    canvas.removeEventListener('mousemove', onMouseMotion);
    canvas.removeEventListener('mousedown', onMouseDown);
    canvas.removeEventListener('mouseup', onMouseUp);
    canvas.removeEventListener("keydown", onKeyDown);
    canvas.removeEventListener("keyup", onKeyUp);
  }
  console.log(pointerLock);
}

function onClick(e) {
  if (!pointerLock) {
    pointerLock = true;
    onPointerLockChange();
  }
  canvas.addEventListener('keydown', function(evt) {
    switch (evt.keyCode) {
      case 27:
        evt.preventDefault();
        break;
      case 32:
        evt.preventDefault();
        break;
      case 38:
        evt.preventDefault();
        break;
      case 40:
        evt.preventDefault();
        break;
    }
  });
}


function main(e) {
  resize();
  canvas.addEventListener("click", onClick);

  canvas.addEventListener("onPointerLockChange", onPointerLockChange);
  canvas.addEventListener("msonPointerLockChange", onPointerLockChange);
  canvas.addEventListener("mozonPointerLockChange", onPointerLockChange);
  canvas.addEventListener("webkitonPointerLockChange", onPointerLockChange);

  scene.registerBeforeRender(() => {
    camera.position = player.position;
    camera.rotation = player.rotation;
  });

  engine.runRenderLoop(function() {
    var fps = Math.round(1000/engine.getDeltaTime());
    if (pointerLock) {
      move(fps);
    }
    scene.render();
  });
}

document.addEventListener("DOMContentLoaded", main);
