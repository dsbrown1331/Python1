word = "Jabberwocky"
#Strings are lists of characters
print("Characters in word '{}'".format(word))
for char in word:
    print(char)

print()
#this will do the same thing
print("Same result, using indexing:")
for i in range(len(word)):
    print(word[i])

poem = """Twas brillig and the slithy toves
Did gyre and gimble in the wabe
All mimsy were the borogoves
And the mome raths outgrabe"""

print()
print("The Jabberwocky:")
print("----------------")
print(poem)

#split() allows us to break up a string on whitespace
print()
print("List of words in the Jabberwocky:")
print("------------------------")
print(poem.split())

print()
print("Words in the Jabberwocky:")
print("------------------------")
words_in_poem = poem.split()
for word in words_in_poem:
    print(word)


#TODO: go to https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
#read about other string functions and try at least two of them out
