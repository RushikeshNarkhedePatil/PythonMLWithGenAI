
def check_perfect(no):
    isum = 0
    for i in range(1,(int(no/2))+1):
        if no % i == 0:
            isum = isum + i
    return (isum == no)

def main():
    Value = 0

    print("Enter Number : ")
    Value = int(input())

    Ret = check_perfect(Value)

    if Ret:
        print("It is perfect number")
    else:
        print("It is not perfect number")

main()

