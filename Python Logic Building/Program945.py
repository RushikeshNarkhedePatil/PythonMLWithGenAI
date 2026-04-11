
def check_even(no):
    if no % 2 == 0:
        print("It is even number")
    else:
        print("It is odd number")

def main():
    Value = 0

    print("Enter Number : ")
    Value = int(input())

    check_even(Value)


main()

