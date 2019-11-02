#Source
#File:     LinkListDemo.py
#Purpose:  Demo on how to create and use a link list
#Author:   Adelaida A. Medlock
#Date:     Febraury 18, 2019

class Node:
    def __init__(self, data, next = None):
        self.__data = data
        self.__next = next
    
    # getters
    def getData(self):
        return self.__data
    
    def getNext(self):
        return self.__next
    
    #setters
    def setData(self,d):
        self.__data = d

    def setNext(self,n):
        self.__next = n

    #overloaded operators
    def __str__(self):
        return str(self.__data)