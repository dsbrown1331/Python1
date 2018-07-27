def is_even(integer):
    remainder = integer % 2
    return remainder == 0

def is_odd(integer):
    return not is_even(integer)


if __name__=="__main__":
    #testing code
    print("testing math_functions.py")
    print("4 is even", is_even(4))
    print("151 is even", is_even(151))
    print("4 is odd", is_odd(4))
    print("151 is even", is_even(151))
