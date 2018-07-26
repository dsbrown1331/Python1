import sys

#if not enough arguments then print error
if len(sys.argv) != 2:
    print("usage: python find_function_defs.py python_file")
    exit()
else:
    try:
        filename = sys.argv[1]
        reader = open(filename)
        for line in reader:
            if line.startswith("def"):
                print(line)
    except:
        print("invalid filename: ", filename)

#read through file and print out all definitions
