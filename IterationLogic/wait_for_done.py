#program that waits until user enters "done" to quit
while True:
    line = input('> ')
    if line == "done":
        print("Bye bye")
        break
    print(line)
