#Write a program that computes the balance of a bank account with
#interest compounded monthly

balance = 100 #starting balance
rate = 0.05 #interest rate
years = 3

num_compounds = years
while(num_compounds > 0):
    num_compounds -= 1
    balance *= rate + 1
    print(balance)

print("After {} years you will have ${}".format(years, balance))
