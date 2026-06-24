print("Hello, World !")

Number = int(input("Enter A Number : "))

def FactorialCalculator():
    Factorial = 1;
    for No in range(1,Number+1):
        Factorial*=No
    return Factorial
    

print(f"Factorial OF {Number} Is : {FactorialCalculator()}")
