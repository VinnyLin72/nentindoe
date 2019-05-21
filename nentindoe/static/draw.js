var board = document.getElementById("slate");
var draw = board.getContext("2d");

draw.fillStyle = "#0000ff"; //makes blue
draw.strokeStyle = "#0000ff"; 

board.addEventListener('mousedown', color);

var color = function() {
    draw.beginPath();
    draw.ellipse(event.clientX, event.clientY, 1, 1, 0, 360, false);
    ctx.stroke();
}
