temp_str = input("temperature:")
temp = float(temp_str)
if temp < 0:
    print("I'm staying inside")
elif temp < 30:
    print("wear a coat")
elif temp < 70:
    print("wear pants")
elif temp < 100:
    print("wear shorts")
elif temp > 150:
    print("you're in trouble")
else:
    print("go to the pool")
