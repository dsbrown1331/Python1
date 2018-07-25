#to write to a file you need to add the "w" argument for write
file_writer = open("output_test.txt", "w")
#you then use the write() function to write out text
file_writer.write("Hi there!\n")
file_writer.write("Don't forget to add a new line escape character.")
file_writer.write("Otherwise you'll still be writing to the same line...\n")
file_writer.write("\t\tyou can also use the \'\\t\' escape to get a tab")
