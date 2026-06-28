# File Inputs 
def InputData():
    Count = int(input("How Many Names ? :"))
    with open("Data.txt","a") as file:
        for Index in range(1,Count+1):
            Name = input(f"Name ({Index}): ")
            file.write(Name+"\n") # Without \n , it'll be appended like Name1Name2Name3

def ReadData():
    NamesArr = []
    with open("Data.txt","r") as file:
        for line in file:
            NamesArr.append(line.rstrip())
    for Name in sorted(NamesArr):
        print(Name)



