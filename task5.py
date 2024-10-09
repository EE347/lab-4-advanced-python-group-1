import csv

with open("task5.csv","w") as f:
    names = ""
    while (1):

        names = input("Add a name: ")
        if names == "quit":
            break
        f.write(names + "\n")
        
    f.close()