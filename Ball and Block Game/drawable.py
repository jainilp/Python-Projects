'''
Name: Jainil Patel
Drexel ID: jbp85
Purpose: Is the abstract base class, which three other classes derive from.
'''

#imports pygame and abstract base class
import pygame
import abc

#Creates abstract base class, Drawable
class Drawable(metaclass = abc.ABCMeta):
    #initializes the variables passed into the child classes
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    #Used to return the location objects
    def getLocation(self):
        return (self.__x, self.__y)
    
    #Sets X of object
    def setX(self, newX):
        self.__x = newX
    
    #Sets Y of object
    def setY(self, newY):
        self.__y = newY
        
    #abstract methods draw used in the child classes
    @abc.abstractmethod
    def draw(self, surface):
        pass
    
    #abstract methods get_rect used in the child classes
    @abc.abstractmethod
    def get_rect(self):
        pass