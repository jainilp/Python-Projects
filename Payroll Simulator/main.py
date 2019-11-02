#Created by Jainil Patel


from LinkedList import *
from Employee import *
from Node import *
import sys

def options():
    print("\n")
    print("Please select one of the following items, and enter the cooresponding number.")
    print("1) Add New Employee")
    print("2) Enter Hours Worked")
    print("3) Display Payroll")
    print("4) Update Employee Hourly Rate")
    print("5) Remove Employee from Payroll")
    print("6) Exit the program\n")

def selection():
    
    #User Validation Loop starts (ends when the input is valid)
    
    userIn = ValidateN("Enter the cooresponding number: ", upper=7)
    #User Validation Loop ends
            
    #Calls the function cooresponding to the number
    if userIn == 1:
        Add()
    elif userIn == 2:
        HoursWorked()
    elif userIn == 3:
        PayrollDis()
    elif userIn == 4:
        UpdateWage()
    elif userIn == 5:
        RmEmp()
    elif userIn == 6:
        sys.exit()

eList = LinkedList()

def ValidateN(state, lower=0, upper=1000000000000):
    x = True
    while x==True:
        try:
            userIn = float(input(state))
            if type(userIn) == float:
                if userIn > lower and userIn < upper:
                    x = False
                else:
                    print("Invalid, try again.")
                
        except:
            print("Invalid, try again.")
    return userIn

def Validate(state):
    y = True
    while y==True:
        try:
            userIn = float(input(state))
            if type(userIn) == float:
                y = False
            else:
                print("Invalid, try again.")
                
        except:
            print("Invalid, try again.")
    return userIn
def Add():
    IDin = Validate("Enter Employee ID: ")
    pay = ValidateN("Enter hourly rate: ",lower=6.00)
    employee = Employee(ID=IDin, wage=pay)
    eList.append(employee)
def HoursWorked():
    userIn = ValidateN("Enter ID: ")
    newHours = ValidateN("Enter Hours Worked: ")
    for i in range(0,len(eList)):
        temp = eList[i]
        if temp.getId() == userIn:
            temp.setHours(newHours)
def PayrollDis():
    for i in range(0,len(eList)):
        print(eList[i])
def UpdateWage():
    
    userIn = ValidateN("Enter ID: ")
    newWage = ValidateN("Enter New Wage: ")
    
    for i in range(0,len(eList)):
        temp = eList[i]
        if temp.getId() == userIn:
            temp.setWage(newWage)
def RmEmp():
    userIn = ValidateN("Enter ID: ")
    for i in range(0,len(eList)):
        temp = eList[i]
        if temp.getId() == userIn:
            eList.remove(temp)

if __name__ == "__main__":
    #Formatting
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Payroll Simulator")
    print("------------------------------")
    
    x = True
    #Loop of the program. Ends when user enters 6.
    while x == True:
        options()
        selection()
    