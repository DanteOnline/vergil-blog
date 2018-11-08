//var canvas = document.getElementById('main');

function clock() {
  var now = new Date();
  var ctx = document.getElementById('main').getContext('2d');
  ctx.save();
  ctx.clearRect(0, 0, 150, 150);
  ctx.translate(75, 75);
  ctx.scale(0.4, 0.4);
  ctx.rotate(-Math.PI / 2);
  ctx.strokeStyle = 'black';
  ctx.fillStyle = 'white';
  ctx.lineWidth = 8;
  ctx.lineCap = 'round';

  // Hour marks
  ctx.save();
  for (var i = 0; i < 12; i++) {
    ctx.beginPath();
    ctx.rotate(Math.PI / 6);
    ctx.moveTo(100, 0);
    ctx.lineTo(120, 0);
    ctx.stroke();
  }
  ctx.restore();

  // Minute marks
  ctx.save();
  ctx.lineWidth = 5;
  for (i = 0; i < 60; i++) {
    if (i % 5!= 0) {
      ctx.beginPath();
      ctx.moveTo(117, 0);
      ctx.lineTo(120, 0);
      ctx.stroke();
    }
    ctx.rotate(Math.PI / 30);
  }
  ctx.restore();

  var sec = now.getSeconds();
  var min = now.getMinutes();
  var hr  = now.getHours();
  hr = hr >= 12 ? hr - 12 : hr;

  ctx.fillStyle = 'black';

  // write Hours
  ctx.save();
  ctx.rotate(hr * (Math.PI / 6) + (Math.PI / 360) * min + (Math.PI / 21600) *sec);
  ctx.lineWidth = 14;
  ctx.beginPath();
  ctx.moveTo(-20, 0);
  ctx.lineTo(80, 0);
  ctx.stroke();
  ctx.restore();

  // write Minutes
  ctx.save();
  ctx.rotate((Math.PI / 30) * min + (Math.PI / 1800) * sec);
  ctx.lineWidth = 10;
  ctx.beginPath();
  ctx.moveTo(-28, 0);
  ctx.lineTo(112, 0);
  ctx.stroke();
  ctx.restore();

  // Write seconds
  ctx.save();
  ctx.rotate(sec * Math.PI / 30);
  ctx.strokeStyle = '#D40000';
  ctx.fillStyle = '#D40000';
  ctx.lineWidth = 6;
  ctx.beginPath();
  ctx.moveTo(-30, 0);
  ctx.lineTo(83, 0);
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(0, 0, 10, 0, Math.PI * 2, true);
  ctx.fill();
  ctx.beginPath();
  ctx.arc(95, 0, 10, 0, Math.PI * 2, true);
  ctx.stroke();
  ctx.fillStyle = 'rgba(0, 0, 0, 0)';
  ctx.arc(0, 0, 3, 0, Math.PI * 2, true);
  ctx.fill();
  ctx.restore();

  ctx.beginPath();
  ctx.lineWidth = 14;
  ctx.strokeStyle = '#325FA2';
  ctx.arc(0, 0, 142, 0, Math.PI * 2, true);
  ctx.stroke();

  ctx.restore();

  window.requestAnimationFrame(clock);
}

window.requestAnimationFrame(clock);

//if (canvas.getContext) {
//  var ctx = canvas.getContext('2d');
////  ctx.fillStyle = 'rgb(200, 0, 0)';
////        ctx.fillRect(10, 10, 50, 50);
////
////        ctx.fillStyle = 'rgba(0, 0, 200, 0.5)';
////        ctx.fillRect(30, 30, 50, 50);
//
////        ctx.beginPath();
////    ctx.moveTo(75, 50);
////    ctx.lineTo(100, 75);
////    ctx.lineTo(100, 25);
////    ctx.fill();
//
//
////for (var i = 0; i < 6; i++) {
////    for (var j = 0; j < 6; j++) {
////      ctx.fillStyle = 'rgb(' + Math.floor(255 - 42.5 * i) + ', ' +
////                       Math.floor(255 - 42.5 * j) + ', 0)';
////      ctx.fillRect(j * 25, i * 25, 25, 25);
////    }
////  }
//
//ctx.strokeStyle = 'orange';
//ctx.beginPath();
//    ctx.arc(75, 75, 50, 0, Math.PI * 2, true); // Outer circle
//    ctx.moveTo(110, 75);
//    ctx.arc(75, 75, 35, 0, Math.PI, false);  // Mouth (clockwise)
//    ctx.moveTo(65, 65);
//    ctx.arc(60, 65, 5, 0, Math.PI * 2, true);  // Left eye
//    ctx.moveTo(95, 65);
//    ctx.arc(90, 65, 5, 0, Math.PI * 2, true);  // Right eye
//    ctx.stroke();
//} else {
//  alert('waf?');
//}

var canvas = document.getElementById('main');
var ctx = canvas.getContext('2d');
var raf;

var ball = {
  x: 100,
  y: 100,
  vx: 5,
  vy: 2,
  radius: 25,
  color: 'blue',
  draw: function() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, true);
    ctx.closePath();
    ctx.fillStyle = this.color;
    ctx.fill();
  }
};

function draw() {
  ctx.clearRect(0,0, canvas.width, canvas.height);
  ball.draw();
  ball.x += ball.vx;
  ball.y += ball.vy;

  if (ball.y + ball.vy > canvas.height ||
      ball.y + ball.vy < 0) {
    ball.vy = -ball.vy;
  }
  if (ball.x + ball.vx > canvas.width ||
      ball.x + ball.vx < 0) {
    ball.vx = -ball.vx;
  }

  raf = window.requestAnimationFrame(draw);
}

canvas.addEventListener('mouseover', function(e) {
  raf = window.requestAnimationFrame(draw);
});

canvas.addEventListener('mouseout', function(e) {
  window.cancelAnimationFrame(raf);
});

ball.draw();