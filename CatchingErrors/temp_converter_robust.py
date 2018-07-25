while True:
    inp = input('Enter Fahrenheit Temperature: ')
    try:
        fahr = float(inp)
        cel = (fahr - 32.0) * 5.0 / 9.0
        print("Celsius temperature is {}".format(cel))
        break
    except:
        print("Invalid temperature. Please enter a number")

    #TODO: add a while loop so that this program will repeat until valid input is given
