from monster import monster

class Human(monster):
    def __init__(self, name):
        self.__name = name
        self.__health = 50
        
    def __str__(self):
        return "The name is" + self.__name + "and I am a Human"

    def getName(self):
        return self.__name
        
    def getDescription(self):
        return "From where I rise, is where you fall. Don't mess with me, cause I am tall."
        
    def basicAttack(self,enemy):
        enemy.doDamage(6)
        
    def basicName(self):
        return "Regular Punch"
        
    def defenseAttack(self,enemy):
        enemy.doDamage(2)
        
    def defenseName(self):
        return "Regular Rodea"
        
    def specialAttack(self,enemy):
        enemy.doDamage(15)
        
    def specialName(self):
        return "Regular (sorta super) Kick"
        
    def getHealth(self):
        return self.__health
        
    def doDamage(self,damage):
        self.__health -= damage
        
    def resetHealth(self):
        self.__health = 50