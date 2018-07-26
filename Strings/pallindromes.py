import sys

def is_pallindrome(input_str):
    if len(input_str) < 2:
        return True
    else:
        i = 0
        j = len(input_str)-1
        while i < j:
            if input_str[i] == input_str[j]:
                i = i + 1
                j = j- 1
            else:
                return False
        return True

def is_pallindrome2(input_str):
    if len(input_str) < 2:
        return True
    else:
        for i in range(len(input_str)):
            j = len(input_str) - 1 - i
            if input_str[i] == input_str[j]:
                continue
            else:
                return False
        return True

def is_pallindrome3(input_str):
    reversed = input_str[::-1]
    if reversed == input_str:
        return True
    else:
        return False

if len(sys.argv) < 2:
    print("usage: python pallindromes.py string")
    exit()

input_word = sys.argv[1]

print("{} is a pallindrome".format(input_word), is_pallindrome3(input_word))
