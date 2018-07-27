things_to_do = ["go to church and play with kids",
                "teach python",
                "go to school",
                "take a nap",
                "teach python",
                "do laundry",
                "read a book"]

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

day = input("Day of week: ")
for i in range(len(days)):
    if day == days[i]:
        print("On {} I like to {}".format(day, things_to_do[i]))
    
