/**
 * PACMAN handler
 * This program is created  in response to Code-Challenge-1 @ https://github.com/ie/Code-Challenge-1
 * This handler is to simulate Pacman moving in a grid (dimension 5x5) without any obstruction.
 * This program only show the commands/actions of user instructing Pacman
 * Requested functions:PLACE, MOVE, LEFT, RIGHT, REPORT
 * @author: Cynthia W.
 * 15-Sep-2018
 */

//Board size
var maxX = 5;
var maxY = 5;

$(document).ready(function(){
	//prepare the documents
    var x = 0;
    var y=0;
    var directions = new Array("North","East","South","West");
    var f = directions[0];
    var stillOffBoard = true;
    
    //add possible x value options. 
    for(i=0;i<maxX;i++){
    	var option = new Option(i,i);
    	$("#x").append($(option));
    }
    //add possible y value options.
    for(i=0;i<maxY;i++){
    	var option = new Option(i,i);
    	$("#y").append($(option));
    }

    function checkBoard(){
    	//check if Pacman is on the play board
    	if(stillOffBoard){
    		alert("Please place Pacman on board first.");
    		return false;
    	}
    	return true;
    }
    
    function output(str){
    	//print output string in the display board
    	$("#board").append("<p>"+str+"</p>");

    	$('#board').scrollTop($('#board')[0].scrollHeight - $('#board')[0].clientHeight);
    	
    }
    
    $("#btnReport").click(function(){
    	//REPORT function. Print Pacman current location.
    	if(checkBoard()){
    		output("Output X:"+x+", Y:"+y+", Direction:"+f);
    	}
    });
    
    
    
    $("#btnPlace").click(function(){
    	//PLACE function. Place Pacman on Board
    	x = $("#x option:selected").val();
    	y = $("#y option:selected").val();
    	f = $("#f option:selected").val();
    	output("PLACE "+x+", "+y+", "+f);
    	if(stillOffBoard){stillOffBoard=false;} //Pacman is on board now. so this must be off
    });
    
    $("#btnLeft").click(function(){
    	//LEFT function. Rotate Pacman facing direction anti-clockwise
    	if(checkBoard()){
	    	var i = directions.indexOf(f);
	    	i--;
	    	if(i<0){i=directions.length-1;}
	    	f = directions[i];
	    	output("Left")
    	}
    });
    
    $("#btnRight").click(function(){
    	//RIGHT function. Rotate Pacman facing direction clockwise
	    if(checkBoard()){
	    	var i = directions.indexOf(f);
	    	i++;
	    	if(i>=directions.length){i=0;}
	    	f = directions[i];
	    	output("RIGHT")
	    }
    });
    
    
    $("#btnMove").click(function(){
    	//MOVE function. Move Pacman one space forward in its facing direction
    	if(checkBoard()){
    		switch(f){
    			case "North":
    				y++;
    				if(y>=maxY){y=maxY-1;} //Pacman is at the edge already. stop from going over
    				break;
    			case "East":
    				x++;
    				if(x>=maxX){x=maxX-1;}//Pacman is at the edge already. stop from going over
    				break;
    			case "South":
    				y--;
    				if(y<0){y=0;} //Pacman is at the edge already. stop from going over
    				break;
    			case "West":
    				x--;
    				if(x<0){x=0;}//Pacman is at the edge already. stop from going over
    				break;
    				
    		}
    		output("MOVE");
    	}
    });
    
    
    
});

