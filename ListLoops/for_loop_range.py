print("Print numbers 0 through 4:")
for i in range(5):
    print(i)

print()
print("i, i^2, i^3")
print("---------")
for i in range(2,7):
    print(i, i*i, i*i*i)

print("You can use range with different step sizes")
print("Counting to 100 by 10's")
for j in range(0, 101, 10):
    print(j)


char_list = ["a", "b", "c", "d", "e"]
print()
print("There are {} items in the list {}".format(len(char_list), char_list))
print("elements in list:")
for i in range(len(char_list)):
    print(char_list[i])
