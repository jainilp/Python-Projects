'''
Name: Jainil Patel
Drexel ID: jbp85
Purpose: Use pygame to create a interactive mini-game, which use's the user's input.
Launching the ball: Click on the ball, and drag it up and to the right as you think is right.
Scoring points: Now after you had some practice, try to hit the blocks with the ball. Each block is worth one point. 
'''

#imports pygame
import pygame

#imports classes used in this main script
from drawable import *
from block import *
from ball import *
from text import *

#initializes pygame
pygame.init()

#creates block list, will be used for collison and scoring purposes
blocks = []
blocks.append(Block(300,355))
blocks.append(Block(315,355))
blocks.append(Block(330,355))
blocks.append(Block(300,370))
blocks.append(Block(315,370))
blocks.append(Block(330,370))
blocks.append(Block(300,385))
blocks.append(Block(315,385))
blocks.append(Block(330,385))

#asigns the pygame clock to the variable clock, will be used to set tick rate
clock = pygame.time.Clock()

#Assignment of delta time, gravity and other variables used in the physics of ball movement
dt = 0.1
g = 6.67
R = 0.7
eta = 0.5
x = 35
y = 400
xv = 0
yv = 0

#test variable, will be used to animate ball
xTest = False
#empty global lists which will store the position of the mouse.
iLoc = []
fLoc = []
#initializes score to zero
score = 0

#This function is used to keep the score, and update the score board
def scoreCount(score):
    scoreCount = 'Score: ' + str(score)
    score = Text(5,5, scoreCount)
    score.draw(window)

#This function is used to test if the ball and block intersect, and is used to stimulate collision.
def intersect(rect1, rect2):
    if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y):
        return True
    return False

#This function draws the blocks which are in the list blocks created earlier.
def drawBlock():
    for i in blocks:
        i.draw(window)
        
#This function draws the ball object
def drawBall(bX=25, bY=400):
    ball = Ball(bX, bY)
    ball.draw(window)
    return ball

#This function draws the main display
def drawDis(score):
    window.fill((255, 255, 255))
    pygame.draw.line(window, (0,0,0), (0,400), (400,400))
    scoreCount(score)
    drawBlock()
    
    
#Checks to see if the module is main
if __name__ == "__main__":
    #sets window as the display, also sets width and height
    window = pygame.display.set_mode((400,500))
    #Draws display using function
    drawDis(score)
    #Draws the initial ball object
    drawBall()
    pygame.display.update()
    
    #While loop is used for game continuity until user exits.
    while True:
        #checks for events in pygame
        for event in pygame.event.get():
            #checks event types, and executes specific code depending on the event
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                iLoc = pygame.mouse.get_pos()
                
            if (event.type == pygame.MOUSEBUTTONUP):
                fLoc = pygame.mouse.get_pos()
                xTest = True
                xv = fLoc[0] - iLoc[0]
                yv = -1 * (fLoc[1] - iLoc[1])
                
        #if statement used in the animation of the all objects
        if xTest:
            
            #used to animate the ball, when the y velocity is greater then 0.0001
            if abs(yv) > 0.0001:
                #tests to see if the ball is on "ground" and adds takes friction into equation if the ball is on the ground and alters the velocities accordingly
                if y > 400:
                    yv = -R * yv
                    xv = eta * xv
                #executs when ball is in the "air" and alters the y velocity accordingly
                else:
                    yv = yv - g * dt
                #Changes x and y location of the ball depending upon velocities
                x += (dt * xv)
                y -= (dt * yv)
                #Draws display and scoreboard
                drawDis(score)
                #Creates the ball object which will be used for the animation
                ball = Ball(int(x), int(y))
                ball.draw(window)
                #Updates pygame display
                pygame.display.flip()
                #Tests for collision and updates score accordingly
                for test in blocks:
                    cond = intersect(ball.get_rect(), test.get_rect())
                    if cond == True:
                        blocks.remove(test)
                        score+=1
                        drawDis(score)
                        ball.draw(window)
            #resets variables and the display when yv is less than 0.0001, and updates the display
            else:
                xv = 0
                yv = 0
                drawDis(score)
                x = 35
                y = 400
                scoreCount(score)
                ball = drawBall()
                pygame.display.update()
        #sets tick rate to 60
        clock.tick(60)
            
        
        
                
                
        

        
        
        
        
    
        
