from monster import monster

class pokemon(monster):
    def __init__(self, name):
        self.__name = name
        self.__health = 50
        
    def __str__(self):
        return "My name is "+self.__name+"."
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return "I am a small, yellow pokemon that is specialized in lightning attacks!"
    
    def basicAttack(self,enemy):
        enemy.doDamage(4)
        
    def basicName(self):
        return "Quick Attack"
    
    def defenseAttack(self,enemy):
        enemy.doDamage(5)
    
    def defenseName(self):
        return "Basic block"
    
    def specialAttack(self,enemy):
        enemy.doDamage(17)
    
    def specialName(self):
        return "Lightning strike"
    
    def getHealth(self):
        return self.__health
    
    def doDamage(self,damage):
        self.__health -= damage
        
    def resetHealth(self):
        self.__health = 50
        
    
    
    
    
    
    
    
    
    
        
        
        