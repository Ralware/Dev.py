file = open("Data.txt","a")
for Num in range(0,1001):
    file.write(f"Current Iteration : {Num}\n")
file.close()