from monster import monster

class Hero(monster):
    def __init__(self, name):
        self.__name = name
        self.__health = 50
        
    def __str__(self):
        return "The name is" + self.__name + "and I am a Human"

    def getName(self):
        return self.__name
        
    def getDescription(self):
        return "From where you fall, is where I will rise. Mess with me, and is will be your demise."
        
    def basicAttack(self,enemy):
        enemy.doDamage(7)
        
    def basicName(self):
        return "Super Punch"
        
    def defenseAttack(self,enemy):
        enemy.doDamage(4)
        
    def defenseName(self):
        return "Super Southpaw"
        
    def specialAttack(self,enemy):
        enemy.doDamage(20)
        
    def specialName(self):
        return "Super (really super) Kick"
        
    def getHealth(self):
        return self.__health
        
    def doDamage(self,damage):
        self.__health -= damage
        
    def resetHealth(self):
        self.__health = 50