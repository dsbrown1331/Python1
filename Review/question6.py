
def change_string(string):
    new_string = ""
    for char in string:
        if char == "e":
            new_string += "i"
        elif char == "o":
            new_string += "a"
        else:
            new_string += char
    return new_string



string_in = input("Type something: ")
print(change_string())
