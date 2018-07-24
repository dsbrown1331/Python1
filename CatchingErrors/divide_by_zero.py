#get user input
num_inp = input("Numerator: ")
denom_inp = input("Denominator: ")

#convert to integers
numerator = int(num_inp)
denominator = int(denom_inp)

#output fraction and decimal values
print("Fraction: {}/{}".format(numerator, denominator))
print("Decimal: {}".format(numerator / denominator))

#TODO: try giving 0 as the Denominator, what error do you get?
#TODO: try giving a string as numerator, what error do you get?
#TODO: Add a try and except statement to catch exceptions
