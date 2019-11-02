'''
Name: Jainil Patel
Drexel ID: jbp85
Purpose: This class is used to create the ball object, and used in it's animation.
'''

#imports abstract base class drawable
from drawable import *
#Creates ball class
class Ball(Drawable):
    #Initializaes the variables passed in when creating a object of Ball
    def __init__(self,x,y):
        super().__init__(x,y)
        
    #Draws the ball, using the location, which is gotten from the parent class
    def draw(self, surface):
        location = super().getLocation()
        pygame.draw.circle(surface, (255,0,0), [location[0],location[1]], 6)
       
    #Sets the X coordinate accordingly
    def setX(self, x):
        super().setX(x)
    
    #Sets the y coordinate accordinly
    def setY(self, y):
        super().setX(y)
        
    #returns rectangle which surrongs the object, used in intersect function and collision detection.
    def get_rect(self):
        location = super().getLocation()
        return pygame.Rect( [location[0]-7, location[1]-7, 15, 15] )