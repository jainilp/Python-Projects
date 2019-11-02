from LinkedList import *
class Employee:
    def __init__(self, ID, wage=0,earnings = 0):
        self.__Id = ID
        self.__hours = float(0)
        self.__wage = float(wage)
        self.__earnings = float(earnings)
        
    def setHours(self,hours):
        self.__hours += float(hours)
        self.__earnings = self.__hours * self.__wage

    def setWage(self,wage):
        self.__wage = float(wage)
        self.__earnings = self.__hours * self.__wage

    def getId(self):
        return self.__Id
    
    def getHours(self):
        return self.__hours
    
    def getWage(self):
        return self.__wage
    
    def getEarnings(self):
        return self.__earnings
    
    def __str__(self):
        x = "\n====Payroll=====\nEmployee ID: " + str(self.__Id) + "\nHours Worked " + str(self.__hours) + "\nHourly Rate: " + str(self.__wage) + "\nGross Wages: " + str(self.__earnings)
        return x
    