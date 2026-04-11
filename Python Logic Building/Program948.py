
def sum_factors(no):
    isum = 0
    for i in range(1,(int(no/2))+1):
        if no % i == 0:
            isum = isum + i
    return isum

def main():
    Value = 0

    print("Enter Number : ")
    Value = int(input())

    Ret = sum_factors(Value)

    print("Sumesion of factors : ", Ret)


main()

