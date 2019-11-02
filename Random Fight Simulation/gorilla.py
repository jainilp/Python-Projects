from monster import monster

class gorilla(monster):
    def __init__(self, name):
        self.__name = name
        self.__health = 50
        
    def __str__(self):
        return "My name is "+self.__name+"."
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return "I am a large, hairy beast that can destroy in a several attacks!"
    
    def basicAttack(self,enemy):
        enemy.doDamage(7)
        
    def basicName(self):
        return "Smash pound"
    
    def defenseAttack(self,enemy):
        enemy.doDamage(3)
    
    def defenseName(self):
        return "Super smash"
    
    def specialAttack(self,enemy):
        enemy.doDamage(10)
    
    def specialName(self):
        return "Beast mode"
    
    def getHealth(self):
        return self.__health
    
    def doDamage(self,damage):
        self.__health -= damage
        
    def resetHealth(self):
        self.__health = 50
        
    
    
    
    
    
    
    
    
    
        
        
        
