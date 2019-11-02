'''
Name: Jainil Patel
Drexel ID: jbp85
Purpose: The purpose of this class is to display the scoreboard
'''

#imports abstract base class drawable
from drawable import *

#Creates Text class
class Text(Drawable):
    #initalizes the variables when an object of Text is created
    def __init__(self,x,y,message):
        super().__init__(x,y)
        fontObj = pygame.font.Font("freesansbold.ttf", 12)
        self.__surface = fontObj.render(message, True, (0,0,0))
    
    #draw is used to draw the text
    def draw(self, surface):
        surface.blit(self.__surface, self.getLocation())

    #get_rect returns the a rectangle location surronding the object
    def get_rect(self):
        location = self.__getLocation()
        return pygame.Rect( [location[0], location[1], 6] )
