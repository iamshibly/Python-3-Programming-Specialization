import random#this random is name of a module
prob = random.random()#rnadom() is the fucntion inside random module
print(prob)
dice = random.randrange(1,7)#randrange is the function inside random module
print(dice)
print(random.random())
#or
from random import randrange, random
prob = random()
print(prob)
dice = randrange(1,7)
print(dice)
print(randrange(1,8))