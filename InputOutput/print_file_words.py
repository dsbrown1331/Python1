file_handler = open("GettysburgAddress.txt")
for line in file_handler:
    words = line.split()
    for word in words:
        print(word)
