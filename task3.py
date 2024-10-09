
def main():
    with open("task3.txt", "a") as f:
        Name = input("What is your name: ")
        f.write(Name + "\n")   
    f.close()

main()