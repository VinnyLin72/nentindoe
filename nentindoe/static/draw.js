var board = document.getElementById("slate");
var draw = board.getContext("2d");

draw.fillStyle = "#0000ff"; //makes blue
draw.strokeStyle = "#0000ff";

// board.addEventListener('mousedown', color);
//
// var color = function() {
//     draw.beginPath();
//     draw.ellipse(event.clientX, event.clientY, 1, 1, 0, 360, false);
//     ctx.stroke();
// }

var mouseClicked = false, mouseReleased = true;

document.addEventListener("click", onMouseClick, false);
document.addEventListener("mousemove", onMouseMove, false);
document.add

function onMouseClick(e) {
    mouseClicked = !mouseClicked;
}

function onMouseMove(e) {
    if (mouseClicked) {
        console.log("hello")
        draw.beginPath();
        draw.arc(e.clientX, e.clientY, 2, 0, Math.PI * 2, false);
        draw.lineWidth = 5;
        draw.strokeStyle = "#000";
        draw.stroke();
    }
}
