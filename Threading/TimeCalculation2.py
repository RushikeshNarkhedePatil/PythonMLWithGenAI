import time

def Factorial(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact * i

    return fact

def main(): 
    value = int(input("Enter Number :"))

    start_Time =time.time()
    Ret = Factorial(value)
    End_Time = time.time()

    print("Factorial is : ",Ret)
    print("Total Execution time is :",End_Time - start_Time)

    

if __name__ == "__main__":
    main()