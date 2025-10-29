import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="3D Car Game", layout="wide")

st.title("🚗 Simple 3D-Style Car Game (Streamlit Edition)")

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>3D Car Demo</title>
<style>
body { margin:0; overflow:hidden; background:#333; }
canvas { display:block; }
</style>
</head>
<body>
<script src="https://cdn.jsdelivr.net/npm/three@0.150.0/build/three.min.js"></script>
<script>
let scene = new THREE.Scene();
let camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
let renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// ground
let groundGeo = new THREE.PlaneGeometry(200,200);
let groundMat = new THREE.MeshPhongMaterial({color:0x228822});
let ground = new THREE.Mesh(groundGeo, groundMat);
ground.rotation.x = -Math.PI/2;
scene.add(ground);

// car body
let carGeo = new THREE.BoxGeometry(2,0.5,4);
let carMat = new THREE.MeshPhongMaterial({color:0xff0000});
let car = new THREE.Mesh(carGeo, carMat);
car.position.y = 0.3;
scene.add(car);

// lights
let ambient = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambient);
let dir = new THREE.DirectionalLight(0xffffff, 0.8);
dir.position.set(10,10,5);
scene.add(dir);

camera.position.set(0,3,8);
camera.lookAt(car.position);

// controls
let keys = {};
document.addEventListener('keydown', (e)=>keys[e.key.toLowerCase()]=true);
document.addEventListener('keyup',   (e)=>keys[e.key.toLowerCase()]=false);

let speed = 0;
let angle = 0;
function animate(){
  requestAnimationFrame(animate);

  // simple physics
  if(keys['w'] || keys['arrowup']) speed += 0.01;
  if(keys['s'] || keys['arrowdown']) speed -= 0.01;
  if(keys['a'] || keys['arrowleft']) angle += 0.03;
  if(keys['d'] || keys['arrowright']) angle -= 0.03;
  speed *= 0.98;
  if(speed>0.5) speed=0.5;
  if(speed<-0.3) speed=-0.3;

  car.rotation.y = angle;
  car.position.x += Math.sin(angle)*speed;
  car.position.z += Math.cos(angle)*speed;

  // camera follows car
  camera.position.x = car.position.x - Math.sin(angle)*8;
  camera.position.z = car.position.z - Math.cos(angle)*8;
  camera.lookAt(car.position);

  renderer.render(scene, camera);
}
animate();
</script>
</body>
</html>
"""

# render HTML in Streamlit
html(html_code, height=600)
