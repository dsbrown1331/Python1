def count_char(words, char):
    char_count = 0
    for c in words:
        if c == char:
            char_count = char_count + 1
    return char_count

#returns most common char
def most_char(string, char1, char2):
    char1_cnt = count_char(string, char1)
    char2_cnt = count_char(string, char2)
    if char1_cnt > char2_cnt:
        return char1, char1_cnt
    else:
        return char2, char2_cnt

x = count_char("Hello", "l")
print(x)

y = most_char("Thesarus", "t", "h")
print(type(y))
print(y[0])
print(y[1])
print(y)
