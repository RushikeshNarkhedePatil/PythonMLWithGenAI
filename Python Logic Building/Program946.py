
def display_factor(no):

    for i in range(1,no+1):
        if no % i == 0:
            print(i)

def main():
    Value = 0

    print("Enter Number : ")
    Value = int(input())

    display_factor(Value)


main()

