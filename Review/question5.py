import random
num_roll = input("Number of dice to roll: ")
num_roll = int(num_roll)

rolls = []
for i in range(num_roll):
    rolls.append(random.randint(1,6))

print("dice rolls")
print(rolls)
