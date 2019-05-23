var board = document.getElementById("slate");
var draw = board.getContext("2d");
var wipe = document.getElementById("clear");
var mouseDown = false;

draw.fillStyle = "#0000ff"; //makes blue
draw.strokeStyle = "#0000ff"; 

var driver = function(e) {
    console.log("in driver");
    if (e.type == "mousedown") {
	mouseDown = true;
	draw.beginPath();
	draw.arc(e.offsetX, e.offsetY, 1, 0, 2 * Math.PI);
	draw.stroke();
	draw.fill();
    }
    else if (e.type == "mousemove" && mouseDown) {
	draw.beginPath();
	//draw.lineTo();
	draw.arc(e.offsetX, e.offsetY, 1, 0, 2 * Math.PI);
	draw.stroke();
	draw.fill();
    }
    else {
	mouseDown = false;
	draw.closePath();
    }
}

board.addEventListener("mousedown", driver);
board.addEventListener("mousemove", driver);
board.addEventListener("mouseup", driver);
/*
var startColor = function() {
    console.log("got here");
    draw.beginPath();
}

var color = function(e) {
    draw.beginPath();
    draw.arc(e.clientX, e.clientY, 1, 0, 2 * Math.PI);
    draw.stroke();
    draw.closePath();
    draw.beginPath();
    console.log("got here");
}

board.addEventListener("mousedown", startColor);
board.addEventListener("moveto", color);
board.addEventListener("mouseup", draw.closePath());
*/
var clear = function() {
    draw.clearRect(0, 0, board.width, board.height);
}

wipe.addEventListener("click", clear);
/*

var colorHold = function() {
    if (e.type == 'mousedown') {
	console.log(e.type);
    }
    console.log(e.type);
}

board.addEventListener('mousedown mouseup', colorHold);

function mousedown()
{
    hold = true;
    callEvent();
}
function mouseup()
{
    hold = false;
}
function callEvent()
{
    if (hold)
    {
	color
	
	
	animationFrame("callEvent()",1);
    }
    else
	return;
}
*/
