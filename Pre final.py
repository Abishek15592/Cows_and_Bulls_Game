#Importing Required Modules
import pygame, random, sys, time
from pygame.locals import *
from tkinter import *
from tkinter.messagebox import *
import main

main
#Initialising PyGame Module
pygame.init()

#Initialising Global Variables
Canvas = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("Cow Bull Game")
white = (255, 255, 255)
black = (10, 10,10)
font1 = "Times New Roman"
font2 = "Arial"
toggleKey = ["  *" for i in range(0, 11)]

global b_count,c_count


#Function To Show Text As Per The Required Parameters
def text(string, size, color, top, left, fonttype = None, bold = False, italic = False):
    font = pygame.font.SysFont(fonttype, size, bold, italic)
    textobj = font.render(string, 1, color)
    textrect = textobj.get_rect()
    textrect.top = top
    textrect.left = left
    Canvas.blit(textobj, textrect)
    pygame.display.update()

#Function To Set A Word From The Database
def set_word():
    file = open("Wordlist.txt", "r")
    ran = random.randrange(127)
    s = ""
    for i in range(ran):
        s = file.readline()
    file.close()
    return(s[0:4])

#Function To Display numbers
def alph():
    alpha = "0123456789"
    l = 30
    for i in alpha:
        text(i, 55, black, 50, l)
        l = l + 40

#Function To Wait For An Input At Certain Screens
def waitforkey():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == MOUSEBUTTONDOWN:
                return

#Function To Kill The Program
def terminate():
    pygame.quit()
    sys.exit()

#Function to Display Timer
def displayTime(ret = False):
    timeCurrent = time.time()
    timer = float(timeCurrent-timeStart)
    timer = round(timer, 1)
    pygame.draw.rect(Canvas, white, (975 , 15, 120, 30))
    text("Time : " + str(timer), 23, black, 10, 975, font1, False, True)
    if ret:
        return timer
    
#Function To Display/Refresh The Game Screen
def dispGame(turn, words):
    Canvas.fill(white)  #Refresh The Game Screen
    alph()  #Display The numbers
    text("Your 4 digit number has been chosen.", 25, black, 140, 30, font2, False, True)
    text("Choose from the above numbers to guess the word.", 25, black, 170, 30, font2, False, True)
    
    a = "Turn : " + str(turn)
    text(a, 23, black, 10, 30, font1, False, True)  #Display Turn Count
    pygame.draw.line(Canvas, black, (20, 118), (1080, 118), 1)
    for i in range(4):
        text("_", 140, black, 330, i*100+100)   #Display Input Blanks
    for i in range(len(words)): #Display Previous Inputs
        text(str(i+1) + ". " + words[i][0], 22, black, 122+i*55, 930, font1)
        b = "B: " + str(words[i][1]) + " / C: " + str(words[i][2])
        text(b, 19, black, 145+i*55, 950, font1)
        
#Function To Display/Refresh User Input
def updateguess(guess = ""):
    
    #Command To Clear Old Input By Overlapping It With A Rectangle Of Background Color
    pygame.draw.rect(Canvas, white, (100 , 320, 400, 70))
    
    #Command To Display Updated Input
    for i in range(len(guess)):
        text(guess[i], 120, black, 320, i*100+100)
    pygame.display.update()



    
#Main Game Loop
def startGame(b_count,c_count):
    global turn
    global words
    global word
    turn = 1
    words = []
    word = set_word()

    global B,C
    global guess
    
    while len(word)!=4:
        word=set_word()
    
    dispGame(turn, words)
    pygame.display.update()
    timepass(turn,word,words,b_count,c_count)

def ex1():
    pass

def callback(b_count,c_count):
    if askyesno('Verify', "If you take this life you're score would be reduced by 30. So Really want a chance?"):
        print (b_count,"****************************************",c_count)
        showwarning('Yes', timepass(10,word,words,b_count,c_count))
    else:
        showinfo('No', show())

def show():
    return endGame(word, False, 10, displayTime(True),tscore)

def timepass(turn,word,words,b_count,c_count):
    #'Turn' Loop
    
    while turn<11:
        letter = 1
        B = 0
        C = 0
        guess = ""
        submit = True
        sub = True
        erase = True
        
        #'Letter' Loop
        while submit:
            while erase:
                text("Erase", 50, black, 620, 950, font2)
                erase = False
                
            #To initiate timer
            displayTime()
            
            #Detect Certain Events Such As Mouse Motion And Mouse Clicks
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()

                #Underline The number That The Mouse Cursor Is Hovering On
                if event.type == MOUSEMOTION:
                    if event.pos[0]>50 and event.pos[0]<400 and event.pos[1]>50 and event.pos[1]<120:
                        x = int((event.pos[0] - 30)/40)
                        pygame.draw.line(Canvas, white, (1, 90), (1099, 90), 2)
                        pygame.draw.line(Canvas, black, (x*40+25, 90), (x*40 + 60, 90), 2)
                        pygame.display.update()
                        
                            
                #Detect Click On Erase Button
                if event.type == MOUSEBUTTONDOWN:
                    if letter>1 and event.pos[0]>950 and event.pos[0]<1070 and event.pos[1]>620 and event.pos[1]<670:
                        letter = letter - 1
                        guess = guess[0:-1]
                        updateguess(guess)
                        
                    #Detect Click On A Certain number
                    if event.pos[0]>30 and event.pos[0]<400 and event.pos[1]>50 and event.pos[1]<95:
                        x = int((event.pos[0] - 30)/40)
                        string = "0123456789"
                        if letter == 1:
                            guess = guess + string[x]
                            updateguess(guess)
                            letter = letter + 1
                        else:
                            #Avoid Any number From Being Re-entered
                            if (string[x] in guess) or (letter == 5):
                                pass
                            else:
                                guess = guess + string[x]
                                updateguess(guess)
                                letter = letter + 1
                if letter == 5:
                    if sub:
                        text("Submit", 60, black, 550, 80, font2)
                        sub = False

                    #Detect Click On Submit Button And Exit The 'Letter' Loop
                    if event.type == MOUSEBUTTONDOWN:
                        if event.pos[0]>80 and event.pos[0]<270 and event.pos[1]>550 and event.pos[1]<600:
                            submit = False

        #Analysing The Input
        for i in range(4):
            if guess[i] in word:
                if word.index(guess[i]) == i:
                    B = B + 1
                    b_count=b_count+1
                else:
                    C = C + 1
                    c_count=c_count+1
        
                print (b_count,"****",c_count)
                global tscore
                tscore=b_count*10+c_count*5

        if turn==10:
            tscore=time123(tscore)
                    
        #End Game If User Wins Else Restart
        repeat = False
        for i in range(len(words)):
            if guess in words[i]:
                repeat = True
        if B == 4:
            print ("hello guys ",b_count,"Now cows",c_count)
            return endGame(word, True, turn, displayTime(True),tscore)
        elif repeat:
            dispGame(turn, words)
        else:
            turn = turn + 1
            words.append([guess, B, C])
            dispGame(turn, words)

        if turn==10:
            Button(text=tscore, command=ex1).pack(fill=X)
            Button(text='Extra Chance', command=callback(b_count,c_count)).pack(fill=X)
            mainloop()

        elif turn==11:
            return endGame(word, False, turn, displayTime(True),tscore)
            

    #End Game Once All 10 Turns Are Used Up
    return endGame(word, False, turn, displayTime(True),tscore)

def time123(tscore):
    return (tscore-30)

#Function To Display The End Game Screen
def endGame(word, result, turn, timer,tscore):
    global bonus
    bonus=0
    if turn<10:
        bonus=1000-(turn-1)*100
    elif turn==10:
        bonus=0
    Canvas.fill(black)
    text("The required answer was", 50, white, 125, 200)
    text(word, 100, white, 200, 325)
    if result:
        text("Congratulations! You guessed the word correctly.", 50, white, 325, 200)
        text("Score: " + str(tscore+bonus), 75, white, 425, 320)

    
    else:
        text("Score: " + str(tscore+bonus), 75, white, 425, 320)
        

#Main Function
text("Welcome to the Cow Bull Game", 60, white, 300, 160, font1, True)
text("Click to Start!", 40, white, 400, 400, font2)

global b_count
global c_count

b_count=0
c_count=0

waitforkey()
global timeStart
timeStart = time.time()
start = startGame(b_count,c_count)
while start:
    toggleKey = ["  *" for i in range(0, 26)]
    timeStart = time.time()
    start = startGame(b_count,c_count)
