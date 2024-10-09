with open("task3.txt", "r") as f:
        names = f.readlines()

        for n in names:
            print(n)

        f.close() 