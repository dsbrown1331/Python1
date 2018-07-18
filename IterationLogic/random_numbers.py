#to generate random numbers import the random module
import random
#generate a random number betwen 0 and 1
x = random.random()
print("x = ", x)

#generate a random numbers with a range [lower, upper]
lower = 3
upper = 5
num = 10
while num > 0:
    print(random.randint(lower, upper))
    num = num - 1
