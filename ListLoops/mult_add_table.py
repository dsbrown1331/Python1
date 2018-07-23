print("Addition Table")
#print top column
print("x\t0\t1\t2\t3\t4\t5\t6\t7")
print()
#for each row
for i in range(8):
    print(i,end="\t")  #print row number
    #for each column
    for j in range(8):
        #print i times j
        print(i+j, end="\t")
    #skip a line
    print("\n")
