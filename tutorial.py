from tkinter import *
from math import *  #only if you need sqrt, pi, sin, cos or tan
from time import *
from random import *
import subprocess as sub

global screen, root

root = Tk()
screen = Canvas(root, width=1000, height=600, background="#07000d")

##############################################################################################################################
#DRAW THE BACKGROUND

#road
screen.create_rectangle(0, 250, 1000, 600, fill = "#292929")


#fence
screen.create_rectangle(0, 100, 1000, 250, fill = "#801f1f", outline = "#801f1f")

for i in range(1000):
    
    if i % 26 == 0:
        screen.create_line(i, 100, i, 250, fill = "#2e0f00")
        
    if i % 104 == 0:
        screen.create_rectangle(i + 26, 100, i + 30, 250, fill = "#521511", outline = "#521511")
        screen.create_rectangle(i, 80, i + 26, 250, fill = "brown", outline = "brown")

#sidewalk
screen.create_rectangle(0, 243, 1000, 260, fill = "#6d6d6e", outline = "#6d6d6e")
screen.create_rectangle(0, 243, 1000, 252, fill = "gray", outline = "gray")

#driveway
screen.create_polygon(0, 600, 200, 350, 600, 350, 800, 600, fill = "#424242", outline = "#424242")
screen.create_polygon(0, 315, 200, 315, 0, 565, fill = "#c7c0cf", outline = "#c7c0cf")
screen.create_polygon(200, 315, 200, 350, 0, 600, 0, 565, fill = "#ad9eb5", outline = "#ad9eb5")
          
screen.create_polygon(800, 315, 600, 315, 800, 565, 1000, 600, 1000, 315, fill = "#c7c0cf", outline = "#c7c0cf")
screen.create_polygon(600, 315, 600, 350, 800, 600, 800, 565, fill = "#ad9eb5", outline = "#ad9eb5")
screen.create_polygon(800, 566, 800, 600, 1000, 635, 1000, 600, fill = "#ad9eb5", outline = "#ad9eb5")
##############################################################################################################################

##############################################################################################################################
#OOP
#classes for common objects
class tile:
    
    state = "clean"
    drawings = [0, 0, 0]
    selected = False
    clicked = False
    outlineColour = "yellow"
    outline = screen.create_rectangle(0, 0, 0, 0)
    time = 0
    progress = 0
    #tiles are for the driveway segments and the refill and drink buttons
   
class progressBar:
    
    barX1 = 250
    barY1 = 450
    barX2 = 250
    barY2 = 480
    
    barOutlineX1 = 250
    barOutlineY1 = 450
    barOutlineX2 = 550
    barOutlineY2 = 480
    #progress bars are for all progress bars
    
##############################################################################################################################

#menu shown here to keep the menu button active throughout the whole game
def showMenuButton():
    
    menuButton = Button(root, text = "MENU", font = "Arial 20", command = toMenu)
    screen.create_window(100, 280, window = menuButton)
        
def toMenu():
    
    root.destroy()
    sub.Popen(["python", "main.py"])

showMenuButton()
    
##############################################################################################################################
    
def setInitialValues():
    
    #set everything as global
    global numSnowflakes, snowflakeSize, snowflakeX, snowflakeY, snowflakeSpeedY, snowflakeSpeedX, snowflakes, snowflakeMoving, addedSnowflakes   
    global outline1, outline2, outline3, outline4, outline5, outline6, outline7, outline8, outline9, tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, drinkTile, refillTile
    global mouseX, mouseY, xArray, yArray, startTime, currentTime, timeArray, tileList, gameState, timer
    global cleaning, cleaningBar, cleaningTileIndex, mapleSyrupLevel, energyLevel, mapleSyrupMeter, energyMeter, drinking, refilling
    global drinkingBar, refillingBar, mouseText, car_img, carX, printedTime, insult, insultList, menuButtons, score, tutorialTime, actionDone
    global tutorialStage, previousEnergyLevel, previousMapleSyrupLevel
    
    
    previousMapleSyrupLevel = 0
    previousEnergyLevel = 0

    actionDone = False #keeps track of if the user has done the intened task during the tutorial
    tutorialStage = 0
    
    #mousetext is for error messages, like if you dont have enough energy to shovel snow
    mouseText = ""
    carX = 1080
    score = 0
    
    mapleSyrupLevel = 1 #how many liters of maple syrup the player has left
    mapleSyrupMeter = progressBar()
    energyMeter = progressBar()
    energyLevel = 60 #how much energy the player has
    
    drinking = False
    refilling = False
    
    car_img = PhotoImage(file = "dad's car.png")
    car_img = car_img.zoom(2, 2)

    #define everything (i didnt know the innit function existed when coding this :skull emoji:)
    energyMeter.barOutlineX1 = 875
    energyMeter.barOutlineY1 = 50
    energyMeter.barOutlineX2 = 915
    energyMeter.barOutlineY2 = 550
    
    energyMeter.barX1 = 875
    energyMeter.barY1 = 550 - 500 * (energyLevel / 100)
    energyMeter.barX2 = 915
    energyMeter.barY2 = 550
    
    mapleSyrupMeter.barOutlineX1 = 940
    mapleSyrupMeter.barOutlineY1 = 400
    mapleSyrupMeter.barOutlineX2 = 980
    mapleSyrupMeter.barOutlineY2 = 550
    
    mapleSyrupMeter.barX1 = 940
    mapleSyrupMeter.barY1 = 550 - mapleSyrupLevel * 50
    mapleSyrupMeter.barX2 = 980
    mapleSyrupMeter.barY2 = 550
    
    printedTime = " "
    
    cleaningTileIndex = 0
    
    cleaning = False

    gameState = "tutorial"
    
    timer = 500
    barStartTime = 0
    barTime = 0
    
    
    outline1 = screen.create_rectangle(0, 0, 0, 0)
    outline2 = screen.create_rectangle(0, 0, 0, 0)
    outline3 = screen.create_rectangle(0, 0, 0, 0)
    outline4 = screen.create_rectangle(0, 0, 0, 0)
    outline5 = screen.create_rectangle(0, 0, 0, 0)
    outline6 = screen.create_rectangle(0, 0, 0, 0)
    outline7 = screen.create_rectangle(0, 0, 0, 0)
    outline8 = screen.create_rectangle(0, 0, 0, 0)
    outline9 = screen.create_rectangle(0, 0, 0, 0)
    
    #snowflakes
    numSnowflakes = 100
    snowflakeSize = []
    snowflakeX = []
    snowflakeY = []
    snowflakeSpeedY = 5
    snowflakes = []
    snowflakeMoving = []
    
    for i in range(numSnowflakes):
        
        snowflakeX.append(randint(0, 1000))
        snowflakeY.append(randint(0, 800))
        snowflakeSize.append(randint(0, 5))
        snowflakes.append(0)
        snowflakeMoving.append(True)
        
    insultList = ["I should've gotten the milk", "I should've left when I had the chance", "You had ONE JOB", "You're a disgrace to this bloodline"]
    insult = choice(insultList)

    startTime = time()
    currentTime = time()
    timeArray = [0, 0]

    
    xArray = [0, 0]
    yArray = [0, 0]
    
    mouseX = 0
    mouseY = 0
    
    tile1 = tile()
    tile2 = tile()
    tile3 = tile()
    tile4 = tile()
    tile5 = tile()
    tile6 = tile()
    tile7 = tile()
    tile8 = tile()
    tile9 = tile()
    drinkTile = tile()
    refillTile = tile()
   
    tutorialText = ""
    tutorialTime = 0
    
    drinkTile.state = "drink"
    refillTile.state = "refill"
    
    tileList = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, drinkTile, refillTile]
    
    cleaningBar = progressBar()
    drinkingBar = progressBar()
    refillingBar = progressBar()



def drawObjects():
    
    #set the variables needed to global
    global timer, cleaning, mapleSyrupMeter, refillingBar, printedTime, car_img, printedTime, carX, gameState, insult, insultList, score, pizzaTruckX, pizzaTruck
    global tutorialText, tutorialTime, actionDone, tutorialStage, previousEnergyLevel, previousMapleSyrupLevel, snowflakeSpeedY, screen

    #gamestate is always tutorial in this version of the code
    if gameState == "tutorial":
        
        #tutorial stage keeps track of how far the player is into the tutorial level
        
        #STAGE 0 IS JUST THE DAD CUTSCENE
        if tutorialStage == 0:
            
            if (timeArray[1]) < 6:       
                
                
                if carX >= 400:
                    screen.create_image(carX, 200, image = car_img, tag = "car")
                    
                    carX -= 10
                    
                  
                else:
                    
                    screen.create_image(carX, 200, image = car_img, tag = "car")
                    screen.create_line(400, 313, 430, 250, fill = "black", width = 10, tag = "dad")
                    screen.create_line(430, 250, 460, 313, fill = "black", width = 10, tag = "dad")
                    screen.create_line(430, 135, 430, 250, fill = "black", width = 10, tag = "dad")
                    screen.create_oval(460, 135, 400, 65, fill = "white", outline = "black", width = 10, tag = "dad")
                    screen.create_line(395, 175, 465, 175, fill = "black", width = 10, tag = "dad")
                    
                    screen.create_oval(345, 210, 850, 310, fill = "white", outline = "black", width = 10, tag = "dad")
                    screen.create_text(610, 260, text = "Keep the driveway clean until I come home!", font = "Arial 15", fill = "black", tag = "dad")
                    
                
            elif (timeArray[1] - tutorialTime) >= 6:
                screen.create_image(carX, 200, image = car_img, tag = "car")
                    
                carX -= 10
                
                
                if carX == -200:
                    carX = 1050
                    tutorialStage = 1
                    timer = 9999999999999999999999999999999
                    actionDone = False
              
        #Stage 1 shows the user how to shovel snow
        elif tutorialStage == 1:
            
            for i in range(numSnowflakes):
                snowflakes[i] = screen.create_oval(snowflakeX[i], snowflakeY[i], snowflakeX[i] + snowflakeSize[i], snowflakeY[i] + snowflakeSize[i], fill = "white", outline = "white", tag = "snowflakes")
              
            
            screen.create_text(430, 150, text = "Click the snow to shovel it!", font = "Arial 30", fill = "white", tag = "text")
                
                
            
            if actionDone == False:
                tile5.state = "snow1"
                actionDone = True
                
            if tile5.state == "clean":
                
                tutorialStage = 2
                actionDone = False 
                
        #Stage 2 shows how larger layers take more energy
        elif tutorialStage == 2:
            
            screen.create_text(430, 150, text = "Larger layers take longer to shovel", font = "Arial 30", fill = "white", tag = "text")
            screen.create_text(430, 200, text = "and take more energy (green bar)", font = "Arial 30", fill = "white", tag = "text")
                
            
            if actionDone == False:
                tile4.state = "snow1"
                tile5.state = "snow2"
                tile6.state = "snow3"
                actionDone = True
            
            #when all these tiles are clean, it moves on to the next stage
            tutorialTileList = [tile4, tile5, tile6]
            numClean = 0
            
            for i in range(len(tutorialTileList)):
                
                if tutorialTileList[i].state == "clean":
                    numClean += 1
                    
            
            if numClean == 3:
                
                tutorialStage = 3
                actionDone = False
                previousEnergyLevel = energyLevel
        
        #stage 3 shows them how to refill energy       
        elif tutorialStage == 3:
            
            screen.create_text(430, 150, text = "To refill energy, drink maple syrup", font = "Arial 30", fill = "white", tag = "text")
            screen.create_text(430, 200, text = "Press the button under the green bar", font = "Arial 30", fill = "white", tag = "text")
            
            
            if previousEnergyLevel < energyLevel:
                
                tutorialStage = 4
                previousMapleSyrupLevel = mapleSyrupLevel
            
        #stage 4 shows them how to refill syrup      
        elif tutorialStage == 4:
            
            screen.create_text(430, 150, text = "To restock on maple syrup, press", font = "Arial 30", fill = "white", tag = "text")
            screen.create_text(430, 200, text = "the button under the short bar", font = "Arial 30", fill = "white", tag = "text")
                
            if previousMapleSyrupLevel < mapleSyrupLevel:
                tutorialStage = 5
                tutorialTime = timeArray[1]
           
        #stage 5 shows them how ice can't be shovelled     
        elif tutorialStage == 5:
            
            if timeArray[1] - 3 <= tutorialTime:
                
                #this shows for 3-4 seconds
                screen.create_text(430, 150, text = "Careful! If you leave a layer", font = "Arial 30", fill = "white", tag = "text")
                screen.create_text(430, 200, text = "too long, it'll ice over", font = "Arial 30", fill = "white", tag = "text")
                screen.create_text(430, 270, text = "(You won't be able to shovel it anymore)", font = "Arial 20", fill = "white", tag = "text")
                
            else:
                
                #this shows after the first one is done
                screen.create_text(430, 150, text = "If the driveway fully freezes over,", font = "Arial 30", fill = "white", tag = "text")
                screen.create_text(430, 200, text = "you lose INSTANTLY", font = "Arial 30", fill = "white", tag = "text")
                screen.create_text(430, 270, text = "(dad will be mad)", font = "Arial 20", fill = "white", tag = "text")
                
            
            if actionDone == False:
                
                for i in range(len(tileList)):
                    
                    tileList[i].state = "clean"
                
                tile5.state = "iced"
                tile5.outlineColour = "red"
                
            if timeArray[1] - 8 == tutorialTime: # after 8 seconds, tutorial will move one
                
                tutorialStage = 6
                tile5.state = "clean"
                tile5.outlineColour = "yellow"
                tutorialTime = timeArray[1]
            
        #Stage 6 shows how snow gets faster and faster over time    
        elif tutorialStage == 6:
            
            
            screen.create_text(430, 150, text = "Snow will fall faster and", font = "Arial 30", fill = "white", tag = "text")
            screen.create_text(430, 200, text = "faster as the game progresses", font = "Arial 30", fill = "white", tag = "text")
            screen.create_text(430, 270, text = "(Stay on your toes!)", font = "Arial 20", fill = "white", tag = "text")
            
            if timeArray[0] != timeArray[1]:
                snowflakeSpeedY += 15
                
            if timeArray[1] - 3 == tutorialTime: #after 3 seconds, tutorial moves on
                tutorialStage = 7
                tutorialTime = timeArray[1]
        
        #stage 7 hints at the key strategy to the game     
        elif tutorialStage == 7: 
            
            screen.create_text(430, 150, text = "Conserving your resources is", font = "Arial 30", fill = "white", tag = "text")
            screen.create_text(430, 200, text = "key to getting a high grade", font = "Arial 30", fill = "white", tag = "text")
            screen.create_text(430, 270, text = "(good luck!)", font = "Arial 20", fill = "white", tag = "text")
        
            if timeArray[1] - 3 == tutorialTime:
                
                tutorialStage = 8 
                
        elif tutorialStage == 8:
            
            screen.create_text(430, 150, text = "You've completed the tutorial!", font = "Arial 30", fill = "white")
            screen.create_text(430, 200, text = "Return to the menu", font = "Arial 30", fill = "white")
            screen.create_text(430, 270, text = "<------------------- (this button)", font = "Arial 20", fill = "white", tag = "text")
                
    
    if gameState != "menu": 
    
        #drink and refill tiles
        if gameState == "in progress" or tutorialStage > 0:     
            
            drinkTile.drawings[0] = screen.create_rectangle(882, 565, 907, 590, fill = "white", outline = "gray", width = 3, tag = "tile")
            refillTile.drawings[0] = screen.create_rectangle(948, 565, 973, 590, fill = "white", outline = "gray", width = 3, tag = "tile")
            
        #BRUTEFORCE THE SNOW LAYERS
        #First the side profiles are drawn or they get drawn on top of the actual snow and look super weird
        
        if tile1.state == "snow1":
            tile1.drawings[0] = screen.create_polygon(210, 347, 185, 372, 220, 357, fill = "#c7c0cf", outline = "#c7c0cf", smooth = "true", tag = "tile")
            tile1.drawings[1] = screen.create_polygon(250, 360, 265, 390, 315, 380, 319, 350, fill = "#c7c0cf", outline = "#c7c0cf", smooth = "true", tag = "tile")
            tile1.drawings[2] = screen.create_polygon(143, 410, 186, 389, 210, 412, fill = "#c7c0cf", outline = "#c7c0cf", smooth = "true", tag = "tile")
     
        elif tile1.state == "snow2":
            tile1.drawings[0] = screen.create_polygon(153, 395, 153, 410, 300, 410, 300, 395, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            tile1.drawings[1] = screen.create_polygon(300, 395, 300, 410, 325, 350, 325, 335, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
        
        elif tile1.state == "snow3":
            tile1.drawings[0] = screen.create_polygon(153, 380, 153, 410, 300, 410, 300, 380, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            tile1.drawings[1] = screen.create_polygon(300, 380, 300, 410, 325, 350, 325, 320, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            
        elif tile1.state == "iced":
            tile1.drawings[0] = screen.create_polygon(153, 380, 153, 410, 300, 410, 300, 380, fill = "#7e9abd", outline = "#7e9abd", tag = "tile")
            tile1.drawings[1] = screen.create_polygon(300, 380, 300, 410, 325, 350, 325, 320, fill = "#7e9abd", outline = "#7e9abd", tag = "tile")
            
        
        ##########################################
        
        if tile2.state == "snow1":            
            tile2.drawings[0] = screen.create_polygon(300, 410, 305, 350, 460, 370, 430, 375, 500, 410, 400, 390, fill = "#c7c0cf", outline = "#c7c0cf", smooth = "true", tag = "tile")
        
        elif tile2.state == "snow2":
            tile2.drawings[0] = screen.create_polygon(300, 395, 300, 410, 500, 410, 500, 395, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
        
        elif tile2.state == "snow3":
            tile2.drawings[0] = screen.create_polygon(300, 380, 300, 410, 500, 410, 500, 380, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            
        elif tile2.state == "iced":
            tile2.drawings[0] = screen.create_polygon(300, 380, 300, 410, 500, 410, 500, 380, fill = "#7e9abd", outline = "#7e9abd", tag = "tile")
            
        
        ##########################################
        
        if tile3.state == "snow1":
            tile3.drawings[0] = screen.create_polygon(565, 375, 571, 402, 665, 415, 580, 350, fill = "#c7c0cf", outline = "#c7c0cf", smooth = "true", tag = "tile")
        
        elif tile3.state == "snow2":
            tile3.drawings[0] = screen.create_polygon(475, 335, 475, 350, 500, 410, 500, 395, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            tile3.drawings[1] = screen.create_polygon(500, 395, 500, 410, 647, 410, 647, 395, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            
        elif tile3.state == "snow3":
            tile3.drawings[0] = screen.create_polygon(475, 320, 475, 350, 500, 410, 500, 380, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            tile3.drawings[1] = screen.create_polygon(500, 380, 500, 410, 647, 410, 647, 380, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            
        elif tile3.state == "iced":
            tile3.drawings[0] = screen.create_polygon(475, 320, 475, 350, 500, 410, 500, 380, fill = "#7e9abd", outline = "#7e9abd", tag = "tile")
            tile3.drawings[1] = screen.create_polygon(500, 380, 500, 410, 647, 410, 647, 380, fill = "#7e9abd", outline = "#7e9abd", tag = "tile")
            
        ###########################################    
        
        if tile4.state == "snow1":
            tile4.drawings[0] = screen.create_polygon(140, 410, 163, 412, 150, 450, 250, 450, 300, 410, fill = "#c7c0cf", outline = "#c7c0cf", smooth = "true", tag = "tile")
            
        elif tile4.state == "snow2":
            tile4.drawings[0] = screen.create_polygon(82, 485, 82, 500, 260, 500, 260, 485, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            tile4.drawings[1] = screen.create_polygon(260, 500, 260, 485, 300, 395, 300, 410, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
    
        elif tile4.state == "snow3":
            tile4.drawings[0] = screen.create_polygon(82, 470, 82, 500, 260, 500, 260, 470, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            tile4.drawings[1] = screen.create_polygon(260, 500, 260, 470, 300, 380, 300, 410, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            
        elif tile4.state == "iced":
            tile4.drawings[0] = screen.create_polygon(82, 470, 82, 500, 260, 500, 260, 470, fill = "#7e9abd", outline = "#7e9abd", tag = "tile")
            tile4.drawings[1] = screen.create_polygon(260, 500, 260, 470, 300, 380, 300, 410, fill = "#7e9abd", outline = "#7e9abd", tag = "tile")
    
        #####################################################
    
        if tile5.state == "snow1":
            tile5.drawings[0] = screen.create_polygon(490, 430, 450, 450, 410, 460, 460, 490, 545, 510, fill = "#c7c0cf", outline = "#c7c0cf", smooth = "true", tag = "tile")
        
        elif tile5.state == "snow2":
            tile5.drawings[0] = screen.create_polygon(260, 485, 260, 500, 540, 500, 540, 485, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
        
        elif tile5.state == "snow3":
            tile5.drawings[0] = screen.create_polygon(260, 470, 260, 500, 540, 500, 540, 470, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            
        elif tile5.state == "iced":
            tile5.drawings[0] = screen.create_polygon(260, 470, 260, 500, 540, 500, 540, 470, fill = "#7e9abd", outline = "#7e9abd", tag = "tile")
              
        
        #######################################################
        if tile6.state == "snow1":
            tile6.drawings[0] = screen.create_polygon(620, 363, 640, 500, 730, 510, fill = "#c7c0cf", outline = "#c7c0cf", smooth = "true", tag = "tile")
            
        elif tile6.state == "snow2":
            tile6.drawings[0] = screen.create_polygon(500, 395, 500, 410, 540, 500, 540, 410, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            tile6.drawings[1] = screen.create_polygon(540, 500, 540, 485, 718, 485, 718, 500, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
        
        elif tile6.state == "snow3":
            tile6.drawings[0] = screen.create_polygon(500, 380, 500, 410, 540, 500, 540, 470, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            tile6.drawings[1] = screen.create_polygon(540, 500, 540, 470, 718, 470, 718, 500, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            
        elif tile6.state == "iced":
            tile6.drawings[0] = screen.create_polygon(500, 380, 500, 410, 540, 500, 540, 470, fill = "#7e9abd", outline = "#7e9abd", tag = "tile")
            tile6.drawings[1] = screen.create_polygon(540, 500, 540, 470, 718, 470, 718, 500, fill = "#7e9abd", outline = "#7e9abd", tag = "tile")
            
    
        #######################################################
        
        if tile7.state == "snow1":
            tile7.drawings[0] = screen.create_polygon(82, 500, 100, 600, -50, 650, fill = "#c7c0cf", outline = "#c7c0cf", smooth = "true", tag = "tile")
            tile7.drawings[1] = screen.create_oval(214, 505, 245, 520, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
            
        elif tile7.state == "snow2":
            tile7.drawings[0] = screen.create_polygon(0, 585, 0, 600, 215, 600, 215, 585, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            tile7.drawings[1] = screen.create_polygon(215, 585, 215, 600, 260, 500, 260, 485, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
        
        elif tile7.state == "snow3":
            tile7.drawings[0] = screen.create_polygon(0, 570, 0, 600, 215, 600, 215, 570, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            tile7.drawings[1] = screen.create_polygon(215, 570, 215, 600, 260, 500, 260, 470, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            
        elif tile7.state == "iced":
            tile7.drawings[0] = screen.create_polygon(0, 570, 0, 600, 215, 600, 215, 570, fill = "#7e9abd", outline = "#7e9abd", tag = "tile")
            tile7.drawings[1] = screen.create_polygon(215, 570, 215, 600, 260, 500, 260, 470, fill = "#7e9abd", outline = "#7e9abd", tag = "tile")
          
        #######################################################
    
        if tile8.state == "snow1":
            tile8.drawings[0] = screen.create_oval(300, 550, 600, 670, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
            
        elif tile8.state == "snow2":
            tile8.drawings[0] = screen.create_polygon(215, 585, 215, 600, 585, 600, 585, 585, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
        
        elif tile8.state == "snow3":
            tile8.drawings[0] = screen.create_polygon(215, 570, 215, 600, 585, 600, 585, 570, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
    
        elif tile8.state == "iced":
            tile8.drawings[0] = screen.create_polygon(215, 570, 215, 600, 585, 600, 585, 570, fill = "#7e9abd", outline = "#7e9abd", tag = "tile")
    
    
        #######################################################
        
        if tile9.state == "snow1":
            tile9.drawings[0] = screen.create_polygon(750, 540, 800, 600, 585, 600, fill = "#c7c0cf", outline = "#c7c0cf", smooth = "true", tag = "tile")
        
        elif tile9.state == "snow2":
            tile9.drawings[0] = screen.create_polygon(540, 485, 540, 500, 585, 600, 585, 585, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            tile9.drawings[1] = screen.create_polygon(585, 585, 585, 600, 800, 600, 800, 585, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
        
        elif tile9.state == "snow3":
            tile9.drawings[0] = screen.create_polygon(540, 470, 540, 500, 585, 600, 585, 570, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
            tile9.drawings[1] = screen.create_polygon(585, 570, 585, 600, 800, 600, 800, 570, fill = "#ad9eb5", outline = "#ad9eb5", tag = "tile")
        
        elif tile9.state == "iced":
            tile9.drawings[0] = screen.create_polygon(540, 470, 540, 500, 585, 600, 585, 570, fill = "#7e9abd", outline = "#7e9abd", tag = "tile")
            tile9.drawings[1] = screen.create_polygon(585, 570, 585, 600, 800, 600, 800, 570, fill = "#7e9abd", outline = "#7e9abd", tag = "tile")
        
        
        #now draw the top section of the snow
        
        #tile1----------------------------------------------------------------------------------------------------------------
        if tile1.state == "snow2":
            tile1.drawings[2] = screen.create_polygon(200, 335, 153, 395, 300, 395, 325, 335, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
            
        elif tile1.state == "snow3":
            tile1.drawings[2] = screen.create_polygon(200, 320, 153, 380, 300, 380, 325, 320, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
            
        elif tile1.state == "iced":
            tile1.drawings[2] = screen.create_polygon(200, 320, 153, 380, 300, 380, 325, 320, fill = "#8fb0d9", outline = "#8fb0d9", tag = "tile")
            
        #tile2----------------------------------------------------------------------------------------------------------------
        if tile2.state == "snow2":
            tile2.drawings[1] = screen.create_polygon(300, 395, 325, 335, 475, 335, 500, 395, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
            
        elif tile2.state == "snow3":
            tile2.drawings[1] = screen.create_polygon(300, 380, 325, 320, 475, 320, 500, 380, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
        
        elif tile2.state == "iced":
            tile2.drawings[1] = screen.create_polygon(300, 380, 325, 320, 475, 320, 500, 380, fill = "#8fb0d9", outline = "#8fb0d9", tag = "tile")
         
            
        #tile3----------------------------------------------------------------------------------------------------------------
        if tile3.state == "snow2":
            tile3.drawings[2] = screen.create_polygon(600, 335, 647, 395, 500, 395, 475, 335, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
           
        elif tile3.state == "snow3":
            tile3.drawings[2] = screen.create_polygon(600, 320, 647, 380, 500, 380, 475, 320, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
            
        elif tile3.state == "iced":
            tile3.drawings[2] = screen.create_polygon(600, 320, 647, 380, 500, 380, 475, 320, fill = "#8fb0d9", outline = "#8fb0d9", tag = "tile")
               
           
        #tile4----------------------------------------------------------------------------------------------------------------
        if tile4.state == "snow2":
            tile4.drawings[2] = screen.create_polygon(153, 395, 82, 485, 260, 485, 300, 395, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
            
        elif tile4.state == "snow3":
            tile4.drawings[2] = screen.create_polygon(153, 380, 82, 470, 260, 470, 300, 380, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
            
        elif tile4.state == "iced":
            tile4.drawings[2] = screen.create_polygon(153, 380, 82, 470, 260, 470, 300, 380, fill = "#8fb0d9", outline = "#8fb0d9", tag = "tile")
              
            
        #tile5----------------------------------------------------------------------------------------------------------------
        if tile5.state == "snow2":
            tile5.drawings[1] = screen.create_polygon(260, 485, 300, 395, 500, 395, 540, 485, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
            
        elif tile5.state == "snow3":
            tile5.drawings[1] = screen.create_polygon(260, 470, 300, 380, 500, 380, 540, 470, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
            
        elif tile5.state == "iced":
            tile5.drawings[1] = screen.create_polygon(260, 470, 300, 380, 500, 380, 540, 470, fill = "#8fb0d9", outline = "#8fb0d9", tag = "tile")
           
            
        #tile6-----------------------------------------------------------------------------------------------------------------
        if tile6.state == "snow2":
            tile6.drawings[2] = screen.create_polygon(647, 395, 718, 485, 540, 485,  500, 395, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
        
        elif tile6.state == "snow3":
            tile6.drawings[2] = screen.create_polygon(647, 380, 718, 470, 540, 470, 500, 380, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
        
        elif tile6.state == "iced":
            tile6.drawings[2] = screen.create_polygon(647, 380, 718, 470, 540, 470, 500, 380, fill = "#8fb0d9", outline = "#8fb0d9", tag = "tile")
        
        
        #tile7-----------------------------------------------------------------------------------------------------------------
        if tile7.state == "snow2":
            tile7.drawings[2] = screen.create_polygon(82, 485, 0, 585, 215, 585, 260, 485, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
        
        elif tile7.state == "snow3":
            tile7.drawings[2] = screen.create_polygon(82, 470, 0, 570, 215, 570, 260, 470, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
            
        elif tile7.state == "iced":
            tile7.drawings[2] = screen.create_polygon(82, 470, 0, 570, 215, 570, 260, 470, fill = "#8fb0d9", outline = "#8fb0d9", tag = "tile")
             
        
        #tile8-----------------------------------------------------------------------------------------------------------------
        if tile8.state == "snow2":
            tile8.drawings[1] = screen.create_polygon(260, 485, 215, 585, 585, 585, 540, 485, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
         
        elif tile8.state == "snow3":
            tile8.drawings[1] = screen.create_polygon(260, 470, 215, 570, 585, 570, 540, 470, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
               
        elif tile8.state == "iced":
            tile8.drawings[1] = screen.create_polygon(260, 470, 215, 570, 585, 570, 540, 470, fill = "#8fb0d9", outline = "#8fb0d9", tag = "tile")
                
        
        #tile9-----------------------------------------------------------------------------------------------------------------
        if tile9.state == "snow2":
            tile9.drawings[2] = screen.create_polygon(718, 485, 800, 585, 585, 585, 540, 485, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
        
        elif tile9.state == "snow3":
            tile9.drawings[2] = screen.create_polygon(718, 470, 800, 570, 585, 570, 540, 470, fill = "#c7c0cf", outline = "#c7c0cf", tag = "tile")
             
        elif tile9.state == "iced":
            tile9.drawings[2] = screen.create_polygon(718, 470, 800, 570, 585, 570, 540, 470, fill = "#8fb0d9", outline = "#8fb0d9", tag = "tile")
              
         
        #now draw outlines based on the mouse position (this is also bruteforced) 
        if gameState == "in progress" or 0 < tutorialStage < 8:
        
            if len(xArray) == 2:
                
                #outline1
                if 150 < xArray[1] < 325:
                    
                    #because of diagonal lines, the equations of the side lines are calculated, and lineY is the y point on that line for the X value of the mouse
                    #using lineY and lineY2, it checks if the mouse is above or below the lines and detmines whether to draw the outlines
                    #math is the same for all outlines, numbers vary
                    
                    lineY = 600 - (1.25 * xArray[1])
                    lineY2 = 600 - (2.4 * xArray[1] - 530)
                    if (410 >= yArray[1] >= 350 and yArray[1] >= lineY and yArray[1] <= lineY2) or tile1.clicked == True:
                        outline1 = screen.create_polygon(200, 350, 153, 410, 300, 410, 325, 350, fill = "", outline = tile1.outlineColour, width = 4, tag = "outline")
                        tile1.selected = True
                 
                else:
                    
                    tile1.selected = False
                 
                # #outline 2
                if 300 < xArray[1] < 500:
                    
                    lineY = 600 - (2.4 * xArray[1] - 530)
                    lineY2 = 600 - (-2.4 * xArray[1] + 1390)
                    if (410 >= yArray[1] >= 350 and yArray[1] >= lineY and yArray[1] >= lineY2) or tile2.clicked == True:
                        outline2 = screen.create_polygon(300, 410, 325, 350, 475, 350, 500, 410, fill = "", outline = tile2.outlineColour, width = 4, tag = "outline")
                        tile2.selected = True
                        
                else:
                    
                    tile2.selected = False   
                        
                # #outline 3
                if 475 < xArray[1] < 650:
                    
                    lineY = 600 - (-2.4 * xArray[1] + 1390)
                    lineY2 = 600 - (-1.25 * xArray[1] + 1000)
                    if (410 >= yArray[1] >= 350 and yArray[1] <= lineY and yArray[1] >= lineY2) or tile3.clicked == True:
                        outline3 = screen.create_polygon(600, 350, 647, 410, 500, 410, 475, 350, fill = "", outline = tile3.outlineColour, width = 4, tag = "outline")
                        tile3.selected = True
                        
                else:
                    
                    tile3.selected = False
                    
                #outline 4
                if 82 < xArray[1] < 300:
                    
                    lineY = 600 - (1.25 * xArray[1])
                    lineY2 = 600 - (2.4 * xArray[1] - 530)
                    if (500 >= yArray[1] >= 410 and yArray[1] >= lineY and yArray[1] <= lineY2) or tile4.clicked == True:
                        outline4 = screen.create_polygon(153, 410, 82, 500, 260, 500, 300, 410, fill = "", outline = tile4.outlineColour, width = 4, tag = "outline")
                        tile4.selected = True
                
                else:
                    
                    tile4.selected = False
            
                #outline5 
                if 260 < xArray[1] < 540:
                    
                    lineY = 600 - (2.4 * xArray[1] - 530)
                    lineY2 = 600 - (-2.4 * xArray[1] + 1390)
                    if (500 >= yArray[1] >= 410 and yArray[1] >= lineY and yArray[1] >= lineY2) or tile5.clicked == True:
                        outline5 = screen.create_polygon(260, 500, 300, 410, 500, 410, 540, 500, fill = "", outline = tile5.outlineColour, width = 4, tag = "outline")
                        tile5.selected = True
                
                else:
                    
                    tile5.selected = False
            
                #outline 6
                if 500 < xArray[1] < 718:
                    
                    lineY = 600 - (-2.4 * xArray[1] + 1390)
                    lineY2 = 600 - (-1.25 * xArray[1] + 1000)
                    if (500 >= yArray[1] >= 410 and yArray[1] <= lineY and yArray[1] >= lineY2) or tile6.clicked == True:
                        outline6 = screen.create_polygon(647, 410, 718, 500, 540, 500, 500, 410, fill = "", outline = tile6.outlineColour, width = 4, tag = "outline")
                        tile6.selected = True
                
                else:
                    
                    tile6.selected = False
                
                #outline 7
                if 0 < xArray[1] < 260:
                    
                    lineY = 600 - (1.25 * xArray[1])
                    lineY2 = 600 - (2.4 * xArray[1] - 530)
                    if (600 >= yArray[1] >= 500 and yArray[1] >= lineY and yArray[1] <= lineY2) or tile7.clicked == True:
                        outline7 = screen.create_polygon(82, 500, 0, 600, 215, 600, 260, 500, fill = "", outline = tile7.outlineColour, width = 4, tag = "outline")
                        tile7.selected = True
                
                else:
                    
                    tile7.selected = False
                
                #outline 8
                if 210 < xArray[1] < 600:
                    
                    lineY = 600 - (2.4 * xArray[1] - 530)
                    lineY2 = 600 - (-2.4 * xArray[1] + 1390)
                    if (600 >= yArray[1] >= 500 and yArray[1] >= lineY and yArray[1] >= lineY2) or tile8.clicked == True:
                        outline8 = screen.create_polygon(260, 500, 215, 600, 585, 600, 540, 500, fill = "", outline = tile8.outlineColour, width = 4, tag = "outline")
                        tile8.selected = True
                
                else:
                    
                    tile8.selected = False
                
                #outline 9
                if 540 < xArray[1] < 800:
                    
                    lineY = 600 - (-2.4 * xArray[1] + 1390)
                    lineY2 = 600 - (-1.25 * xArray[1] + 1000)
                    if (600 >= yArray[1] >= 500 and yArray[1] <= lineY and yArray[1] >= lineY2) or tile9.clicked == True:
                        outline9 = screen.create_polygon(718, 500, 800, 600, 585, 600, 540, 500, fill = "", outline = tile9.outlineColour, width = 4, tag = "outline")
                        tile9.selected = True
                    
                else:
                    
                    tile9.selected = False
                    
                if 882 < xArray[1] < 907:
                    
                    if 565 < yArray[1] < 590:
                        drinkTile.outline = screen.create_rectangle(882, 565, 907, 590, fill = "", outline = "yellow", width = 5, tag = "outline")
                        drinkTile.selected = True
                        
                else:
                    
                    drinkTile.selected = False
                        
                if 948 < xArray[1] < 973:
                    
                    if 565 < yArray[1] < 907:
                        refillTile.drawings[0] = screen.create_rectangle(948, 565, 973, 590, fill = "", outline = "yellow", width = 5, tag = "tile")
                        refillTile.selected = True
                        
                else:
                    
                    refillTile.selected = False
                    
        #draw snowflakes            
        for i in range(numSnowflakes):
            snowflakes[i] = screen.create_oval(snowflakeX[i], snowflakeY[i], snowflakeX[i] + snowflakeSize[i], snowflakeY[i] + snowflakeSize[i], fill = "white", outline = "white")
    
        ####################################################################################################
        ####################################################################################################
        ####################################################################################################
    
        #draw the progress bars, if they are inactive the values are simply reset
        if gameState == "in progress" or tutorialStage > 0:
            
            #cleaning bar
            if cleaning == True:
                screen.create_rectangle(cleaningBar.barX1, cleaningBar.barY1, cleaningBar.barX2, cleaningBar.barY2, fill = "#02de35", outline = "#02de35", tag = "outline")
                screen.create_rectangle(cleaningBar.barOutlineX1, cleaningBar.barOutlineY1, cleaningBar.barOutlineX2, cleaningBar.barOutlineY2, fill = "", outline = "black", width = 10, tag = "outline")
            
            
            elif cleaning == False:
                
                cleaningBar.barX1 = 250
                cleaningBar.barY1 = 450
                cleaningBar.barX2 = 250
                cleaningBar.barY2 = 480
                
                cleaningBar.barOutlineX1 = 250
                cleaningBar.barOutlineY1 = 450
                cleaningBar.barOutlineX2 = 550
                cleaningBar.barOutlineY2 = 480
            
            #drinking bar    
            if drinking == True:
                
                screen.create_rectangle(drinkingBar.barX1, drinkingBar.barY1, drinkingBar.barX2, drinkingBar.barY2, fill = "#8c4501", outline = "#8c4501", tag = "outline")
                screen.create_rectangle(drinkingBar.barOutlineX1, drinkingBar.barOutlineY1, drinkingBar.barOutlineX2, drinkingBar.barOutlineY2, fill = "", outline = "black", width = 10, tag = "outline")
            
            elif drinking == False:
                
                drinkingBar.barX1 = 250
                drinkingBar.barY1 = 450
                drinkingBar.barX2 = 250
                drinkingBar.barY2 = 480
                
                drinkingBar.barOutlineX1 = 250
                drinkingBar.barOutlineY1 = 450
                drinkingBar.barOutlineX2 = 550
                drinkingBar.barOutlineY2 = 480
            
            #refilling bar     
            if refilling == True:
                
                screen.create_rectangle(refillingBar.barX1, refillingBar.barY1, refillingBar.barX2, refillingBar.barY2, fill = "#05273b", outline = "#05273b", tag = "outline")
                screen.create_rectangle(refillingBar.barOutlineX1, refillingBar.barOutlineY1, refillingBar.barOutlineX2, refillingBar.barOutlineY2, fill = "", outline = "black", width = 10, tag = "outline")
            
            elif refilling == False:
                
                refillingBar.barX1 = 250
                refillingBar.barY1 = 450
                refillingBar.barX2 = 250
                refillingBar.barY2 = 480
                
                refillingBar.barOutlineX1 = 250
                refillingBar.barOutlineY1 = 450
                refillingBar.barOutlineX2 = 550
                refillingBar.barOutlineY2 = 480
            
            
            #energy bar
            screen.create_rectangle(energyMeter.barX1, energyMeter.barY1, energyMeter.barX2, energyMeter.barY2, fill = "forest green", outline = "forest green", tag = "outline")
            screen.create_rectangle(energyMeter.barOutlineX1, energyMeter.barOutlineY1, energyMeter.barOutlineX2, energyMeter.barOutlineY2, fill = "", outline = "black", width = 8, tag = "outline")
            
            #maple syrup bar
            screen.create_rectangle(mapleSyrupMeter.barX1, mapleSyrupMeter.barY1, mapleSyrupMeter.barX2, mapleSyrupMeter.barY2, fill = "#8c4501", outline = "#8c4501", tag = "outline")
            screen.create_rectangle(mapleSyrupMeter.barOutlineX1, mapleSyrupMeter.barOutlineY1, mapleSyrupMeter.barOutlineX2, mapleSyrupMeter.barOutlineY2, fill = "", outline = "black", width = 8, tag = "outline")
        
        ####################################################################################################
        ####################################################################################################
        #draws the mouse text that displays text if there is an error (the user doesnt have enough energy, etc.)
        
        #depending on which half of the screen it is on, it is displayed on a different side of the cursor
        
        #if on the left side, diplayed right of the cursor
        if xArray[1] <= 500:
            screen.create_text(xArray[1] + 150, yArray[1] - 50, text = mouseText, font = "Arial 25", fill = "yellow", tag = "text")
        
        #if on the right side, displayed left of the cursor
        else:
            
            screen.create_text(xArray[1] - 150, yArray[1] - 50, text = mouseText, font = "Arial 25", fill = "yellow", tag = "text")
        

        
    
def updateObjects():
    global snowflakeSpeedY, cleaning, currentTime, startTime, addedSnowflakes, numSnowflakes, timeArray, timer, gameState, energyLevel, energyMeter, mapleSyrupLevel, mapleSyrupMeter, drinking, drinkTile
    global refilling, refillingBar, mouseText, score, playTile, tutorialTile, controlsTile, controlsBackTile, actionDone, root, screen

    #calculates time for the other functions to use. rounds them to a whole number and puts them in an array that is
    #2 items long. using it normally is too accurate. the time updates every frame, so it will display the same
    #number for multiple frames, we need it to only update every second
    #by instead putting it into an array, and detecting instead if there is a change in the array,
    #we can get the accurate time every second.
    
        
    
    ##########################################################################
    #updates time and timer
    #every frame, exact time is calculated
    #we round to the nearest second
    #if the 2 values in the array aren't equal, we know that one second has passed
    currentTime = ceil((time() - startTime))
    
    
    timeArray.append(currentTime)
    
    if len(timeArray) == 3:
        
        timeArray.remove(timeArray[0])
        
    if timeArray[0] != timeArray[1]:
        timer -= 1
        
    ##########################################################################
    #updates energy and maple syrup bars
        
    if energyLevel < 0:
        
        energyLevel = 0
    
    #updates energy meter
    energyMeter.barY1 = 550 - 500 * (energyLevel / 100)
    
    #updates maple syrup meter
    mapleSyrupMeter.barY1 = 550 - 50 * mapleSyrupLevel
    
    if mapleSyrupLevel > 3:
        mapleSyrupLevel = 3
        
    ##########################################################################
        #snowflake sheinanegans
    
    # updates snowflakes
    for i in range(numSnowflakes):
        
        
        if snowflakeY[i] < 600:
            
            snowflakeY[i] += snowflakeSpeedY
        
        else:
            snowflakeY[i] = randint(-200, 0)

    ##########################################################################
    
    #updates progress bars for drinking, cleaning, and refilling
    
    #progress bar is 300 px long, for drinking and refilling
    #to see if a bar is complete, you check if the X2 inner rectangle of the bar is equal to or greater than the outline's X2
    
    #cleaning
    if cleaning == True:
                
        #check if its filled
        if cleaningBar.barX2 >= cleaningBar.barOutlineX2:
            
            #resets values
            cleaning = False
            tileList[cleaningTileIndex].clicked = False
            tileList[cleaningTileIndex].outlineColour = "yellow"
            tileList[cleaningTileIndex].progress = 0
            
            #updates score, more points for larger snow layers
            if tileList[cleaningTileIndex].state == "snow1":
                
                score += 100
                
            elif tileList[cleaningTileIndex].state == "snow2":
                
                score += 300
                
            elif tileList[cleaningTileIndex].state == "snow3":
                
                score += 500
            
            tileList[cleaningTileIndex].state = "clean"
        
    #drinking   
    elif drinking == True:
        
        #every second, bar goes up 75px
        # 300px bar/ 75px = 4
        #takes 4 seconds for it to drink
        if timeArray[0] != timeArray[1]:
            
            drinkingBar.barX2 += 75 
            
            #if it finishes
            if drinkingBar.barX2 >= cleaningBar.barOutlineX2:
                
                #reset and update values
                drinking = False
                drinkTile.clicked = False
                drinkTile.outlineColour = "yellow"
                
                mapleSyrupLevel -= 1
                energyLevel += 60
                
                #doesn't let it go past 100
                if energyLevel > 100:
                    energyLevel = 100
    
    #refilling                
    elif refilling == True:
        
        #every second, goes up 45 px
        #300 / 45 = ~6.5 seconds
        
        if timeArray[0] != timeArray[1]:
            
            refillingBar.barX2 += 45
            
            #check if its done
            if refillingBar.barX2 >= refillingBar.barOutlineX2:
                
                #reset and update
                refilling = False
                refillTile.clicked = False
                refillTile.outlineColour = "yellow"
                
                mapleSyrupLevel += 1
                
    ##########################################################################
    
    #updates the mouse text to be blank every second           
    if timeArray[0] != timeArray[1]:
        mouseText = " "
                
    ##########################################################################

    #if timer runs out, you win
    if timer <= 0:
        
        gameState = "win"
        
    ##########################################################################
    
    #checks all the tiles to see if all the tiles have been fully iced
    #if all tiles are iced, you lose
    for i in range(len(tileList)):
        
        if tileList[i].state != "iced":
            break
        
        if i == 8 and tileList[i].state == "iced":
            gameState = "lose"

    ##########################################################################         
       
    #if you win or lose, the snow will gradually come to a stop before dad comes back on screen
    if gameState == "win" or gameState == "lose":
        
        if (snowflakeSpeedY) - 1 <= 0:
            snowflakeSpeedY = 0
            
        else:
            
            snowflakeSpeedY -= 1

    ##########################################################################

            
#handles mouse clicks
def mouseClickHandler( event ):
    
    global cleaning, cleaningTileIndex, drinking, refilling, mouseText, energyLevel, tutorialStage, gameState, menuTiles
    
    #if something is already happening (a tile is being cleaned or whatever), the mouse clicks won't register
    if cleaning == False and drinking == False and refilling == False and (gameState == "in progress" or 0 < tutorialStage < 8):
        for i in range(len(tileList)):
            
            #if the tile isn't clean and it is selected
            if tileList[i].state != "clean" and tileList[i].selected == True: 
                
                #if its not the drink or refill tile
                if tileList[i] not in [drinkTile, refillTile]:
                    ##########################################################################
                    
                    #different energy levels are required based on the size of the snow layer
                    if tileList[i].state == "snow1" and energyLevel >= 3 or tileList[i].clicked == True:
                        
                        tileList[i].clicked = True
                        tileList[i].outlineColour = "spring green"
                        cleaningTileIndex = i
                        cleaning = True
                        tileList[i].progress += 100 #300 / 100 = 3 clicks to shovel
                        
                    #error messages show if you don't have enough energy
                    elif tileList[i].state == "snow1" and energyLevel < 3:
                        
                        mouseText = "Not enough energy!"
                        
                    ##########################################################################
                    
                    elif tileList[i].state == "snow2" and energyLevel >= 10 or tileList[i].clicked == True:
                        
                        tileList[i].clicked = True
                        tileList[i].outlineColour = "spring green"
                        cleaningTileIndex = i
                        cleaning = True
                        tileList[i].progress += 30 #300 / 30 = 10 clicks to shovel
                        
                    elif tileList[i].state == "snow2" and energyLevel < 10:
                        
                        mouseText = "Not enough energy!"
                        
                    ##########################################################################
                    elif tileList[i].state == "snow3" and energyLevel >= 20 or tileList[i].clicked == True:
                    
                        tileList[i].clicked = True
                        tileList[i].outlineColour = "spring green"
                        cleaningTileIndex = i
                        cleaning = True
                        tileList[i].progress += 15 #300 / 15 = 20 clicks to shovel
                        
                    elif tileList[i].state == "snow3" and energyLevel < 20:
                        
                        mouseText = "Not enough energy!"
                    
                    ##########################################################################    
                    elif tileList[i].state == "iced":
                        
                        mouseText = "Can't shovel ice!"
                    
                    break
                
                ##########################################################################
                
                #if the tile is the drink or refill tile
                elif tileList[i] == drinkTile and mapleSyrupLevel > 0 and energyLevel < 100:
                    
                    drinking = True
                    drinkTile.clicked = True
                    break
                
                #error message
                elif tileList[i] == drinkTile and mapleSyrupLevel == 0 and energyLevel < 100:
                    
                    mouseText = "Not enough maple syrup!"
                
                ##########################################################################
                
                #refill tile
                elif tileList[i] == refillTile and mapleSyrupLevel < 3:
                    
                    refilling = True
                    refillTile.clicked = True
                    break
                
                #error message
                elif tileList[i] == refillTile and mapleSyrupLevel == 3:
                    
                    mouseText = "Maple syrup full!"
                
                ##########################################################################
            
       
    #for every click, energy goes down by 1            
    elif cleaning == True and drinking == False and refilling == False and gameState == "in progress" or tutorialStage > 0:

        if tileList[cleaningTileIndex].state != "clean" and tileList[cleaningTileIndex].selected == True:
            
            cleaningBar.barX2 += tileList[cleaningTileIndex].progress
            energyLevel -= 1
            
#updates mouse coordianates               
def mouseMotionHandler(event):
    
    #mouse coordinates need to be appended to an array so they can be accessed at any time, and they
    #work when the mouse stays still
    
    global xArray, yArray, mouseX, mouseY
    
    mouseX = event.x
    mouseY = event.y
    
    xArray.append(mouseX)
    yArray.append(mouseY)

    #if the array gets too long, it deletes part of itself, leaving us with the only 2 values
    if len(xArray) == 3:
        xArray.remove(xArray[0])
        yArray.remove(yArray[0])
        

def runGame():
    
    setInitialValues()

    #game loop
    while True:
        
        
        drawObjects()
		
		
        screen.update()
        sleep(0.03)
        
        
        for i in range(numSnowflakes):
            
            screen.delete(snowflakes[i])
            
        screen.delete("outline", "tile", "text", "progress bar", "car", "driveway snow", "dad", "snowflakes", "menu")
        
        updateObjects()
        




#Call the runGame function
root.after(0, runGame)

#binds
screen.bind( "<Button-1>", mouseClickHandler )
screen.bind("<Motion>", mouseMotionHandler )

screen.pack()
screen.focus_set()
root.mainloop()