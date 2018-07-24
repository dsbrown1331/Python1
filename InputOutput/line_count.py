def line_count(filename):
    file_h = open(filename)
    count = 0
    for line in file_h:
        count += 1
    return count

num_lines = line_count("Jabberwocky.txt")
print(num_lines)
