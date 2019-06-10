var board = document.getElementById("slate");
var draw = board.getContext("2d");
var wipe = document.getElementById("clear");
var line = document.getElementById("line");
var circle = document.getElementById("circle");
var box = document.getElementById("box");
var stroke = document.getElementById("strokewidth");
var maincolor = document.getElementById("colorp");
var imgurl = document.getElementById("imgurl");
var imgurl2 = document.getElementById("imgurl2");

//for box methods
var startx = 0;
var starty = 0;
var endx = 0;
var endy = 0;

var mouseDown = false;
var mode = "draw";
var thickness = 1;

// fxn driving the drawing
var driver = function(e) {
    if (mode == "draw") {
	if (e.type == "mousedown") {
	    mouseDown = true;
	    draw.beginPath();
            draw.fillStyle = maincolor.value; //makes blue
            draw.strokeStyle = maincolor.value;
	    draw.lineTo(e.offsetX, e.offsetY);
	    draw.stroke;
	    draw.fill();
	}
	else if (e.type == "mousemove" && mouseDown) {
            draw.fillStyle = maincolor.value; //makes blue
            draw.strokeStyle = maincolor.value;
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
    else if (mode == "circle") {
	if (e.type == "mousedown") {
	    draw.fillStyle = maincolor.value; //makes blue
            draw.strokeStyle = maincolor.value;
	    draw.arc(e.offsetX, e.offsetY, thickness, 0, 2 * Math.PI);
	}
    }
    else {
	if (e.type == "mousedown") {
	    startx = e.offsetX;
	    starty = e.offsetY;
	}
	if (e.type == "mouseup") {
            draw.fillStyle = maincolor.value; //makes blue
            draw.strokeStyle = maincolor.value;	    
	    endx = e.offsetX;
	    endy = e.offsetY;
	    draw.rect(startx, starty, endx, endy);
	    draw.stroke();
	    draw.fill();
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

//circle fxn
var round = function() {
    if (mode != "circle") {
	mode = "circle";
	draw.beginPath();
    }
    else {
	mode = "draw";
    }
}

circle.addEventListener("mousedown", round);

//box fxn
var square = function() {
    if (mode != "box") {
	mode = "box";
	draw.beginPath();
    }
    else {
	mode = "draw";
    }
}

box.addEventListener("mousedown", square);

//update stroke length
var update = function() {
    draw.beginPath();
    draw.lineWidth = thickness;
    thickness = stroke.value;
    console.log("got to update");
}

stroke.addEventListener("click", update);

function downloadImage() {
    // var element = document.createElement('a');
    // element.setAttribute('href', board.toDataURL('image/png'));
    // element.setAttribute('download', 'chart.png');
    //
    // element.style.display = 'none';
    // document.body.appendChild(element);

    imgurl.value=board.toDataURL('image/png')
    imgurl2.value=board.toDataURL('image/png')
    


    // element.click();
    // document.body.removeChild(element);
}
