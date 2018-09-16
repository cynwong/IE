'''

* This program is created  in response to Code-Challenge-1 @ https://github.com/ie/Code-Challenge-1
* This handler is to simulate Pacman moving in a grid (dimension 5x5) without any obstruction.
* This program only show the commands/actions of user instructing Pacman
* Requested functions:PLACE, MOVE, LEFT, RIGHT, REPORT


This program can either accept instruction  either from manual input or from a file. 
Available functions are:
    1. PLACE
    2. MOVE
    3. LEFT
    4. RIGHT
    5. REPORT
    6. READ [filename.txt] - Text files only. used for inputs from files
    7. BYE - to end the program
    8. HELP - short manual printout. 

 
@author: Cynthia W.
15-Sep-2018
'''

import sys
import os.path

'''
  Tuple 'faces' and Dictionary 'directions' are added here 
  so that user can enter either 'N' or 'North' for North
'''
faces = 'n','e','s','w'
directions = {'n':"North",'e':"East",'s':"South",'w':"West"}
'''dimension 5x5'''
boardsize = {"x":5,"y":5}
'''pacman default position'''
position = {"x":0,"y":0,"f":'n'}
'''list of availabe commands'''
commandList = 'place','move','left','right','report','read','bye','help'

'''
    This funciton will rotate PacMan anti-clockwise
'''
def left():
    p = faces.index(position['f']) - 1
    position['f'] = faces[p] if p >=0 else faces[len(faces)-1]
    
    
'''
    This funciton will rotate PacMan clockwise
'''
def right():
    p = faces.index(position['f']) + 1
    position['f'] = faces[p] if p<len(faces) else faces[0]
    

'''
    This function will move PacMan Position by one in the direction it is facing
'''       
def move():
    if position['f']=='n':
        position['y'] = getValueWithinBoundary(position['y']+1,'y')
    elif position['f']=='s':
        position['y'] = getValueWithinBoundary(position['y']-1,'y')
    elif position['f']=='e':
        position['x'] = getValueWithinBoundary(position['x']+1,'x')
    elif position['f']=='w':
        position['x'] = getValueWithinBoundary(position['x']-1,'x')


'''
    This function will only return the value within the Boundary. 
'''            
def getValueWithinBoundary(value,axis):
    ''' for left or bottom border'''
    if value < 0:
        return 0
    '''for top or right border'''
    if value >= boardsize[axis]:
        return boardsize[axis] - 1
    '''value is still within range'''
    return value

'''
    This function will format the error messages
'''
def printError(errno,errmsg):
    print "Error %s: %s" % (errno, errmsg)
    
'''
    To print out command manuals
    
'''
def print_help(command):
    help_text = {
        "list": "Available commands: place,left,right,move,read,help,bye",
        "place": "place: Put PacMan on certain location on Board.\nsyntax:   place x,y,direction",
        "left" : "left: Rotate PacMan anti-clockwise",
        "right": "right: Rotate PacMan clockwise",
        "move" : "move: Move PacMan one space in the direction it faces",
        "read" : "read: Input the commands from file.\nsyntax: read filename.txt",
        "bye"  : "bye: end the game."
    }
    print help_text[command] if command in help_text else help_text["list"]
    
'''
    This funciton will put PacMan at the coordinate as per user instruction. 
    
''' 
def place(command):
    def printplaceerror(errno):
        printError("3%s"%errno, "Invalid 'place' command. Try again")
        print_help('place')
    
    if command.find(',') != -1:
        tmp = command.split(' ',1)[1].split(',')
            
        if len(tmp)< 3:
            printplaceerror(1)
            return
        
        '''x'''
        if tmp[0].strip().isdigit():
            position['x'] = getValueWithinBoundary(int(tmp[0]),'x')
        else:
            printplaceerror(2)
            return
           
        '''y''' 
        if tmp[1].strip().isdigit():
            position['y'] = getValueWithinBoundary(int(tmp[1]),'y')
        else:
            printplaceerror(3)
            return
        
        '''face/direction'''
        tmp[2]= tmp[2].strip()
        if not tmp[2] in faces and not tmp[2] in map(lambda x:x.lower(),directions.values()):
            printplaceerror(4)
            return
        position['f']=tmp[2][0].lower()
    else:
        printplaceerror(5)
    

'''
    To print out the current location of PacMan
'''
def report():
    print "Output: %s, %s, %s" % (position['x'],position['y'],directions[position['f']])

'''
    Terminate the program
'''
def end():
    '''user want to quit the application. so stop'''
    print "Thank you for playing. Goodbye."
    sys.exit()
    
'''
    To wait for user command
'''
def listen(isFirstMove=False):
    command = raw_input("What should PacMan do?   ").strip().lower()
    print command.upper()
    
    if command.find('read') != -1:
        '''input from file.'''
        read(command,isFirstMove)
    else:
        '''user will input the command manually'''
        play(command,isFirstMove)

'''
    This will check if PacMan is placed on Board. 
'''
def isBoardEmpty(command,isFirstMove):
    '''first move must always be a "PLACE" command'''
    if command.find("place") == -1:
        print "Place Pacman on board first"
        listen(isFirstMove)
    return False
        
'''
    This will use the input from file
    This funciton can only read text files(*.txt)
'''
def read(command,isFirstMove):
    filename = command[5:].strip()
    if not filename.endswith('.txt'):
        '''check file type'''
        printError(1.1,"invalid file type. Try again.")
    elif os.path.exists(filename):
        f = open(filename)
        data = f.readlines()
        for line in data:
            line = line.strip()
            if line and line[:2] != '//':
                isFirstMove = action(line.lower(),isFirstMove)
                print line.upper()
        f.close()
    else:
        printError(1.2,"Input file not found.")
    listen(isFirstMove)
'''
    Main function where we direct the progam what to do. 
'''
def action(command,isFirstMove):
    
    if not command in commandList:
        printError(2.1,"Invalid Command")
        print_help('list')
        return isFirstMove
    
    if command == 'bye':
        end()

    if command.find('help',0) != -1:
        title = command.split(' ',1)[1] if command.find(' ') != -1 else ''
        print_help(title)
        return isFirstMove
            
    if isFirstMove:
        isFirstMove = isBoardEmpty(command,isFirstMove) 
        
    
    if command == "move":
        move()
    elif command == "left":
        left()
    elif command == "right":
        right()
    elif command == 'report':
        report()    
    elif command[0:5] == 'place':
        place(command)
    
    return isFirstMove


        
'''
    This function is used when user input manually
'''    
def play(command,isFirstMove): 
    isFirstMove = action(command,isFirstMove)
    listen(isFirstMove)
        
    
    
    
if __name__ == "__main__":
    print "Hello. Let's play Pacman."
    
    listen(True);
