import sys

def print_file_lines(filename):
    file_reader = open(filename)
    for line in file_reader:
        print(line)

if len(sys.argv) <= 1:
    print("usage: python print_file_arg.py filename")
    exit()
else:
    try:
        filename = sys.argv[1]
        print_file_lines(filename)
    except:
        print("Can't find file " + filename)
