#code to encript a message using a Caesar cipher

#shift a letter
#example: if shift = 2 then 'a' -> 'c'
def encript_char(character, shift):
    #first change character into unicode
    unicode_val = ord(character)
    #add the shift
    unicode_val += shift
    #convert back into character
    shifted_char = chr(unicode_val)
    return shifted_char

#encript an entire file, character by character
#input arguments are the input and output filenames and the amount to shift
#characters by for the caesar cipher
#Note: this will only encript alphabetical characters
def encript_file(input_filename, output_filename, shift):
    file_reader = open(input_filename)
    file_writer = open(output_filename, "w")

    for line in file_reader:
        for char in line:
            if char.isalpha():
                e_word = encript_char(char, shift)
                file_writer.write(e_word)
            else:
                file_writer.write(char)
    file_writer.close()

#testing code
print(encript_char("a",2))
print(encript_char("C", 4))
encript_file("GettysburgAddress.txt", "encripted.txt", 1)
