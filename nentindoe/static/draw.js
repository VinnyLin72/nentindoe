var board = document.getElementById("slate");
var draw = board.getContext("2d");
var wipe = document.getElementById("clear");
var line = document.getElementById("line");
var stroke = document.getElementById("strokewidth");
var mouseDown = false;
var mode = "draw";
var thickness = 1;

draw.fillStyle = "#0000ff"; //makes blue
draw.strokeStyle = "#0000ff";

// fxn driving the drawing
var driver = function(e) {
    if (mode == "draw") {
	if (e.type == "mousedown") {
	    mouseDown = true;
	    draw.beginPath();
	    draw.lineTo(e.offsetX, e.offsetY);
	    draw.stroke;
	    draw.fill();
	}
	else if (e.type == "mousemove" && mouseDown) {
	    draw.lineTo(e.offsetX, e.offsetY);
	    draw.moveTo(e.offsetX, e.offsetY);
	    draw.stroke();
	    draw.fill();
	}
	else {
	    mouseDown = false;
	    draw.closePath();
	}
    }
    else if (mode == "line") {
	if (e.type == "mousedown") {
	    draw.lineWidth = thickness;
	    draw.lineTo(e.offsetX, e.offsetY);
	    draw.moveTo(e.offsetX, e.offsetY);
	    draw.stroke();
	    draw.closePath();
	    console.log("closing path");
	}
    }
}

board.addEventListener("mousedown", driver);
board.addEventListener("mousemove", driver);
board.addEventListener("mouseup", driver);

// clear fxn
var clear = function() {
    draw.clearRect(0, 0, board.width, board.height);
    draw.beginPath();
}

wipe.addEventListener("click", clear);

//line fxn
var zip = function() {
    if (mode != "line") {
	mode = "line";
	draw.beginPath();
    }
    else {
	mode = "draw";
    }
}

line.addEventListener("mousedown", zip);


//update stroke length
var update = function() {
    console.log("got to update");
}

stroke.addEventListener("click", update);

function downloadImage() {
    var element = document.createElement('a');
    element.setAttribute('href', board.toDataURL('image/png'));
    element.setAttribute('download', 'chart.png');
    element.style.display = 'none';
    document.body.appendChild(element);
    // element.click();
    // document.body.removeChild(element);
}
