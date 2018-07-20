def add(a, b):
    print("ADDING {} + {}".format(a, b))
    return a + b

def multiply(a, b):
    print("MULTIPLYING {} * {}".format(a, b))
    return a * b

print("Let's do some math with just functions!")
age = add(10, 5)
height = multiply(9, 6)
print("Age: {}, Height: {}".format(age, height))

print("Here is a puzzle.")
what = add(age, multiply(height, add(age, height)))
print("That becomes: ", what, "Can you do it by hand?")
