import keyboard
import time
import colorama 
from colorama import Back,Fore,Style  

rows, cols = (6, 7)
arr = [["-" for i in range(cols)] for j in range(rows)]

gameRunning=True
xTurn=True
end=False
availableSlots=0

def canPlace(input):
    placed=False
    
    for x in range(cols):
        if(arr[5-x][input-1]=='-'):
            if(xTurn):
                arr[5-x][input-1]='X'
                placed=True
                winCheck(input,x,'X')
                return placed
            else:
                arr[5-x][input-1]='O'
                placed=True
                winCheck(input,x,'O')
                return placed
    return placed

def winCheck(input,x,sign):
    y=1
    countx=0
    county=0
    countzr=0
    countzl=0
    while(y<4):
        if(input-y>0):#left
            if(arr[5-x][input-y-1]==sign):
                countx+=1 
            else:
                y+=3
        y+=1
    y=1
    while(y<4):
        if(input+y<8):#right
            if(arr[5-x][input+y-1]==sign):
                countx+=1 
            else:
                y+=3
        y+=1
    if(countx!=4):
        y=1
        while(y<4):#checking down
            if(6-x+y<7):
                #print(arr[5-x+y][input-1])
                if(arr[5-x+y][input-1]==sign):
                    county+=1 
                else:
                    y+=3
            y+=1
    if(countx!=4 and county!=4):
        y=1
        while(y<4):#checking up left
            if((6-x-y>=0)and(input-y>0)):
                #print(arr[5-x-y][input-y-1])
                if(arr[5-x-y][input-y-1]==sign):
                    countzl+=1
                else:
                    y+=3
            y+=1
        y=1
        while(y<4):
            if((5-x+y<6)and(input+y<7)):#checking down right
                #print(arr[5-x+y][input+y-1])
                if(arr[5-x+y][input+y-1]==sign):
                    countzl+=1 
                else:
                    y+=3
            y+=1 
    if(countx!=4 and county!=4 and countzl!=4):
        y=1
        while(y<4):#checking up right
            if((6-x-y>=0)and(input+y<8)):
                if(arr[5-x-y][input+y-1]==sign):
                    countzr+=1
                else:
                    y+=3
            y+=1
        y=1
        while(y<4):
            if((6-x+y<7)and(input-y>0)):#checking down left
                if(arr[5-x+y][input-y-1]==sign):
                    countzr+=1 
                else:
                    y+=3
            y+=1 
    if(countx==3 or county==3 or countzl==3 or countzr==3):
        global gameRunning
        gameRunning=False      
        print(sign+' won!')
        update()
def game(input):
    keyboard.unhook_all()
    time.sleep(.5)
    if(canPlace(input)):
        global availableSlots
        availableSlots+=1
        if(availableSlots==42):
            global gameRunning
            gameRunning=False
            print("Tie!")
        global xTurn 
        if(xTurn): 
            xTurn=False
        else:
            xTurn=True
    else:
        print("Invalid Placement")


def update():
    print('  1  2  3  4  5  6  7 ')
    for x in range(rows):
        print('| ',end="")
        for y in range(cols):
            print(arr[x][y]+'  ',end="")
        print('|')


while(gameRunning):
    update()
    if keyboard.is_pressed('q'):
        break
    if(xTurn):
        print("X's Turn")
        while True:
            try:
                if keyboard.is_pressed('q'):
                    end=True
                    break
                elif keyboard.is_pressed('1'):
                    input=1
                    break
                elif keyboard.is_pressed('2'):
                    input=2
                    break
                elif keyboard.is_pressed('3'):
                    input=3
                    break
                elif keyboard.is_pressed('4'):
                    input=4
                    break
                elif keyboard.is_pressed('5'):
                    input=5 
                    break 
                elif keyboard.is_pressed('6'):
                    input=6
                    break 
                elif keyboard.is_pressed('7'):
                    input=7
                    break
            except:
                print("error")
    else:
        print("O's Turn")
        while True:
            try:
                if keyboard.is_pressed('q'):
                    end=True
                    break
                elif keyboard.is_pressed('1'):
                    input=1
                    break
                elif keyboard.is_pressed('2'):
                    input=2
                    break
                elif keyboard.is_pressed('3'):
                    input=3
                    break
                elif keyboard.is_pressed('4'):
                    input=4
                    break
                elif keyboard.is_pressed('5'):
                    input=5  
                    break 
                elif keyboard.is_pressed('6'):
                    input=6  
                    break 
                elif keyboard.is_pressed('7'):
                    input=7
                    break
            except:
                print("error")
    if(end):
        break
    game(input)



    


