#Parent class Media
class Media():
    #initlizaes the type, name, and ratings
    def __init__(self, mediaType, name, rating):
        self.__mediaType = mediaType
        self.__name = name
        self.__rating = int(rating)
    
    #Overloaded str, for the purpose of simulating the media
    def __str__(self):
        message = "You are now enjoying the " + self.__mediaType + ": " + self.__name + " - Ratings: " + str(self.__rating) + "/10"
        return message
        
    #getter for name
    def getName(self):
        return self.__name
    
    #getter for type
    def getType(self):
        return self.__mediaType
    
    #getter for rating
    def getRating(self):
        return self.__getRating
    
    #setter for name
    def setName(self, newName):
        self.__rating = int(newName)
        
    #setter for type
    def setType(self, newType):
        self.__rating = int(newType)
    
    #setter for rating
    def setRating(self, newRating):
        self.__rating = int(newRating)
    

    
#Child/Sub class of Media, named movie
class Movie(Media):
    #initliazes the type, name, ratings, director and running time.
    def __init__(self, mediaType, name, rating, director, runningTime):
        super().__init__(mediaType, name, rating)
        self.__director = director
        self.__runningTime = runningTime
    
    #overrides str for printing purposes
    def __str__(self):
        return super().__str__() + " - Director: " + self.__director + " - Running Time: " + str(self.__runningTime) + " minutes."
    
    #getter for director
    def getDirector(self):
        return self.__director
    
    #getter for time
    def getTime(self):
        return self.__runningTime
    
    #setter for director
    def setDirector(self, newDirector):
        self.__director = newDIrector
        
    #setter for time    
    def setTime(self, newTime):
        self.__runningTime = newTime
    
    #play method for simulation
    def play(self, obj):
        print(obj)
        
class Song(Media):
    #initliazas the type, name, ratings, artist and album.
    def __init__(self, mediaType, name, rating, artist, album):
        super().__init__(mediaType, name, rating)
        self.__artist = artist
        self.__album = album
    
    #overrides str for printing purposes
    def __str__(self):
        return super().__str__() + " - Artist: " + self.__artist + " - Album: " + self.__album + "."
    
    #getter for artist  
    def getArtist(self):
        return self.__artist
    
    #getter for album 
    def getAlbum(self):
        return self.__Album
    
    #setter for artist 
    def setArtist(self, newArtist):
        self.__artist = newArtist
        
    #setter for Album     
    def setAlbum(self, newAlbum):
        self.__album = newAlbum
    
    #play method for simulation
    def play(self, obj):
        print(obj)

class Picture(Media):
    #initliazes the type, name, ratings, and resolution.
    def __init__(self, mediaType, name, rating, resolution):
        super().__init__(mediaType, name, rating)
        self.__resolution = int(resolution)
    
    #overrides str for printing purposes
    def __str__(self):
        return super().__str__() + " - Resolution: " + str(self.__resolution) + " dpi."
    
    #getter for artist 
    def getRes(self):
        return self.__resolution
    
    #setter for resolution 
    def setRes(self, newRes):
        self.__resolution = newRes
        
    #show method for simulation
    def show(self, obj):
        print(obj)
    