#Mark Boady and Matthew Burlick
#Drexel University 2018
#CS 172


from human import *
from hero import *
from gorilla import *
from pokemon import *
from monster import monster
import random


#This function has two monsters fight and returns the winner
def monster_battle(m1, m2):

    m1.resetHealth()
    m2.resetHealth()

    print("Starting Battle Between")
    print(m1.getName()+": "+m1.getDescription())
    print(m2.getName()+": "+m2.getDescription())
    print("\n")
    
    
    randomInt = random.randint(1,11)
    if randomInt <= 5:
        attacker = m1
        defender = m2
    else:
        defender = m1
        attacker = m2
    
    print(attacker.getName()+" goes first.")
    
    while( m1.getHealth() > 0 and m2.getHealth() > 0):
        #Determine what move the monster makes
        #Probabilities:
        #   60% chance of standard attack
        #   20% chance of defense move
        #   20% chance of special attack move

        #Pick a number between 1 and 100
        move = random.randint(1,100)
        #It will be nice for output to record the damage done
        before_health=defender.getHealth()
        
        #for each of these options, apply the appropriate attack and 
        #print out who did what attack on whom
        attackUsed = ''
        if( move >=1 and move <= 60):
            attacker.basicAttack(defender)
            attackUsed = attacker.basicName()
        elif move>=61 and move <= 80:
            attacker.defenseAttack(defender)
            attackUsed = attacker.defenseName()
        else:
            attacker.specialAttack(defender)
            attackUsed = attacker.specialName()
        
        print(attacker.getName() + ": " + attackUsed)
        
        if attacker == m1:
            attacker = m2
            defender = m1
        else:
            attacker = m1
            defender = m2
        
        
        if m1.getHealth() > 0:
            print(m1.getName() + " at " + str(m1.getHealth()))
        else:
            print(m1.getName() + " at " + "0")
        if m2.getHealth() > 0:
            print(m2.getName() + " at " + str(m2.getHealth()) + "\n")
        else:
            print(m2.getName() + " at " + "0")
        
    if m1.getHealth() > 0:
        return m1
    else:
        return m2

#----------------------------------------------------
if __name__=="__main__":
    randomIntSeed = random.randint(1,450)
    random.seed(randomIntSeed)
    first = Human("Joe")
    second = Hero("Joey")
    third = pokemon("Pikachu")
    fourth = gorilla("King Kong")
    winner = ""
    winner2 = ""
    if randomIntSeed <= 150:
        winner = monster_battle(first,second)
        print("Match 1 goes to: " + winner.getName() + "\n")
        winner2 = monster_battle(third,fourth)
        print("Match 2 goes to: " + winner2.getName() + "\n")
    elif randomIntSeed > 150 and randomIntSeed <= 300:
        winner = monster_battle(second,third)
        print("Match 1 goes to: " + winner.getName() + "\n")
        winner2 = monster_battle(first,fourth)
        print("Match 2 goes to: " + winner2.getName() + "\n")
    elif randomIntSeed > 300 and randomIntSeed <= 450:
        winner = monster_battle(first,third)
        print("Match 1 goes to: " + winner.getName() + "\n")
        winner2 = monster_battle(second,fourth)
        print("Match 2 goes to: " + winner2.getName() + "\n")
    
    Victor = monster_battle(winner, winner2)
    print("\nThe Absolute Victor is " + Victor.getName())
    