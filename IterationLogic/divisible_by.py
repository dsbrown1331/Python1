num_input = input("Enter an integer:")
number = int(num_input)
divisible_by_2 = number % 2 == 0
divisible_by_3 = number % 3 == 0
divisible_by_5 = number % 5 == 0

if divisible_by_2 or divisible_by_3 or divisible_by_5:
    print("divisible by 2 or 3 or 5")
else:
    print("Not a multiple of 2 or 3 or 5")
