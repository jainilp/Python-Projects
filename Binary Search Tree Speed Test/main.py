import random
from BST import *
from time import *
import matplotlib.pyplot as plt


def populate(n):
    main = random.sample(range(1,10000), n)
    tree = BST()
    for i in main:
        tree.append(i)
    return main, tree

def listin(l, n):
    if n in l:
        return True
    else:
        return False
LList = []
BList = []
avgL = 0
avgB = 0
count = 0
countBS = 0
avgList = []
avgBist = []
nL = []
for n in range(0,10000,1000):
    m, tree = populate(n)
    initialL = time()
    finalL = 0
    finalB = 0
    initialB = 0
    for i in m:
        count += 1
        finalL = time()
        initialB = time()
        finalB = 0
        if tree.isin(i):
            countBS += 1
            finalB = time()
            LTime = finalL-initialL
            bTime = finalB-initialB
            LList.append(LTime)
            BList.append(bTime)
    tempC = 0
    tempCi = 0
    tempL = 0
    tempB = 0
    for i in LList:
        tempC += 1
        tempL += i
        avgL = tempL/tempC
    avgList.append(avgL)
    avgL = 0
    for i in BList:
        tempCi += 1
        tempB += i
        avgB = tempB/tempCi
    avgBist.append(avgB)
    avgB = 0
    nL.append(n)
    
plt.plot(nL,avgList,label='List Search')
plt.plot(nL,avgBist,label='Binary Search Tree')
plt.legend()
plt.show()





