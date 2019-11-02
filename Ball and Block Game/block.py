'''
Name: Jainil Patel
Drexel ID: jbp85
Purpose: This class was used to create the blocks, the user hits.
'''

#imports abstract base class drawable
from drawable import *

#Creates block class
class Block(Drawable):
    #Initializes the variables passed in when creating a block object
    def __init__(self,x,y):
        super().__init__(x,y)
    #draw is used to draw the block object, along with the border lines
    def draw(self, surface):
        #draws the block itself
        pygame.draw.rect(surface, (0,43,205), [self._Drawable__x,self._Drawable__y, 15, 15])
        #Draws four lines, (the border of the block)
        pygame.draw.line(surface, (0,0,0), [self._Drawable__x,self._Drawable__y],(self._Drawable__x,self._Drawable__y+15))
        pygame.draw.line(surface, (0,0,0), [self._Drawable__x,self._Drawable__y],[self._Drawable__x+15,self._Drawable__y])
        pygame.draw.line(surface, (0,0,0), [self._Drawable__x+15,self._Drawable__y],[self._Drawable__x+15,self._Drawable__y+15])
        pygame.draw.line(surface, (0,0,0), [self._Drawable__x,self._Drawable__y+15],[self._Drawable__x+15,self._Drawable__y+15])
    #get_rect returns a rectangle surronding the block, and is used in determining if the ball and block intersect
    def get_rect(self):
        location = super().getLocation()
        return pygame.Rect( [location[0], location[1], 15, 15] )