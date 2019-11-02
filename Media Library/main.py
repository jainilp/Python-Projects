#Developed by: Jainil Patel
#Drexel ID: jbp85
#Purpose: Create a program which simulates a Media Library. By selecting certain optiosn you are able to see the list of the Media Items themselves, and through other options you are able to "play/view/hear" the item.
#Date Created: May 1, 2019

#Import Classes
from media import *

import sys

#Options Function, when called displays the menu/list of options to the user.
def options():
    print("\n")
    print("Please select one of the following items, and enter the cooresponding number.")
    print("1) Display all items in the Media Library")
    print("2) Display Movies in Media Library")
    print("3) Display Songs in Media Library")
    print("4) Display Pictures in Media Library")
    print("5) Play a Movie")
    print("6) Play a Song")
    print("7) See a Picture")
    print("8) Quit the program")

#Selection Function, when called it asks the user to enter the corresponding number
def selection():
    
    #User Validation Loop starts (ends when the input is valid)
    x = True
    while x==True:
        try:
            userIn = int(input("Enter cooresponding number here: "))
            if type(userIn) == int:
                if userIn > 0 and userIn < 9:
                    x = False
                else:
                    print("Invalid, try again.")
                
        except:
            print("Invalid, try again.")
    #User Validation Loop ends
            
    #Calls the function cooresponding to the number
    if userIn == 1:
        displayAll()
    elif userIn == 2:
        displayMovie()
    elif userIn == 3:
        displaySong()
    elif userIn == 4:
        displayPicture()
    elif userIn == 5:
        playMovie()
    elif userIn == 6:
        playSong()
    elif userIn == 7:
        showPicture()
    elif userIn == 8:
        sys.exit()

#Function to display all of the Media items. 
def displayAll():
    print("\n")
    print("Displaying all items in Media Library")
    
    #Iterate through the list of objects, and print each object.
    for i in Media:
        print(i.getName())
    
#Function to display all of the Movie Objects' Names
def displayMovie():
    print("\n")
    print("Displaying all Movies")
    
    #Iterate through the list of objects, and print each movies name.
    for i in Media:
        if i.getType() == "Movie":
            print(i.getName())
        
#Function to display all of the Song Objects' Names
def displaySong():
    print("\n")
    print("Displaying all Songs")
    
    #Iterate through the list of objects, and print each songs name.
    for i in Media:
        if i.getType() == "Song":
            print(i.getName())

#Function to display all of the Picture Objects' Names
def displayPicture():
    print("\n")
    print("Displaying all Pictures")
    #Iterate through the list of objects, and print each pictures name.
    for i in Media:
        if i.getType() == "Picture":
            print(i.getName())

#Function which validates if the name inputted by the user exists.
def exists(userInName):
    x = False
    #Iterate through list to check if input is found anywhere
    for i in Media:
        temp = i.getName()
        if temp.lower() == userInName.lower() or temp == userInName:
            x = True
    return x

#Function to simulate playing of Movie
def playMovie():
    print("\n")
    x = True
    #Nested loops, for purpose of simulating the playing of the Movie.
    while x==True:
        userInName = input("Enter name of Movie you would like to watch: ")
        #Validation
        if exists(userInName) == False:
            print("\nNot Found! Try again after displaying the movies.")
            break
        #For Loop for iteration and playing of the selected movie   
        for i in Media:
            temp = i.getName()
            if i.getType() == "Movie" and (temp == userInName or temp.lower() == userInName.lower()):
                i.play(i)
                x = False
                break
        
        break

#Function to simulate playing of Song
def playSong():
    print("\n")
    x = True
    #Nested loops, for purpose of simulating the playing of the Song.
    while x==True:
        userInName = input("Enter name of Song you would like to hear: ")
        #Validation
        if exists(userInName) == False:
            print("\nNot Found! Try again after displaying the songs.")
            break 
        #For Loop for iteration and playing of the selected song  
        for i in Media:
            temp = i.getName()
            if i.getType() == "Song" and (temp == userInName or temp.lower() == userInName.lower()):
                i.play(i)
                x = False
                break
        
        break

#Function to simulate showing of Picture
def showPicture():
    print("\n")
    x = True
    #Nested loops, for purpose of simulating the showing of the Picture.
    while x==True:
        userInName = input("Enter name of Picture you would like to see: ")
        #Validation
        if exists(userInName) == False:
            print("\nNot Found! Try again after displaying the pictures.")
            break
        #For Loop for iteration and playing of the selected picture     
        for i in Media:
            temp = i.getName()
            if i.getType() == "Picture" and (temp == userInName or temp.lower() == userInName.lower()):
                i.show(i)
                x = False
                break
        
        break

#Checks to see if this is the main module
if __name__ == "__main__":
    #Media list will be populated with objects
    Media = []
    
    #Appending of all the objects to the Media List (12 objects to be exact)
    Media.append(Movie("Movie", "Endgame", 10, "Joe Russo", 180))
    Media.append(Movie("Movie", "War", 7, "Tony Styles", 170))
    Media.append(Movie("Movie", "Avatar", 9, "James Cameron", 160))
    Media.append(Song("Song", "Fort", 6, "Ninja", "Tunes"))
    Media.append(Song("Song", "Table", 6, "Marshmellow", "Furniture"))
    Media.append(Song("Song", "Computer", 6, "Brian", "Future"))
    Media.append(Picture("Picture", "Trees", 10, 400))
    Media.append(Picture("Picture", "Lake", 8, 320))
    Media.append(Picture("Picture", "Mountain", 4, 280))
    Media.append(Picture("Picture", "Drexel", 7, 400))
    Media.append(Picture("Picture", "Philadelphia", 10, 360))
    Media.append(Picture("Picture", "Yorktown", 6, 360))
    
    #Test variable
    x = True
    
    #Formatting
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Welcome to your Movie Libarary")
    print("------------------------------")
    
    #Loop of the program. Ends when user enters 8.
    while x == True:
        options()
        selection()
        
        
        