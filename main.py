#######################################################################

#CANADA SIMULATOR
#PRAMOD CHAVALI, JANUARY 2025
#It's possible to get an A+, but the highest I've gotten is an A
#let me know somehow if you get an A+

#######################################################################


#main.py is the menu screen, directs you to the tutorial or the main game
from tkinter import *
from math import *  #only if you need sqrt, pi, sin, cos or tan
from time import *
from random import *
import subprocess as sub


root = Tk()
screen = Canvas(root, width=1000, height=600, background="#07000d")
screen.pack()

#define buttons
#using the subprocess library, the buttons will open and close different files to take the player
#between the menu, tutorial, and the main game
def showMenuButton():
    
    menuButton = Button(root, text = "MENU", font = "Arial 30", command = toMenu)
    screen.create_window(700, 550, window = menuButton)
    
def toMenu():
    
    root.destroy()
    sub.Popen(["python", "main.py"])
    
def showPlayButton():
    
    playButton = Button(root, text = "PLAY", font = "Arial 30", command = toPlay)
    screen.create_window(500, 300, window = playButton)
    
def toPlay():
    
    root.destroy()
    sub.Popen(["python", "game.py"])

def showTutorialButton():
    
    tutorialButton = Button(root, text = "TUTORIAL", font = "Arial 30", command = toTutorial)
    screen.create_window(500, 500, window = tutorialButton)
    
def toTutorial():
    
    root.destroy()
    sub.Popen(["python", "tutorial.py"])



#background
screen.create_rectangle(0, 0, 1000, 800, fill = "gray", outline = "gray", tag = "menu")
screen.create_text(500, 100, text = "CANADA SIMULATOR", fill = "white", font = "Arial 40", tag = "menu")

#show buttons
showTutorialButton()
showPlayButton()

screen.mainloop()
