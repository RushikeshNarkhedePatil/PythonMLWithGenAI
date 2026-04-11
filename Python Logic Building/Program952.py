
def sum_digits(no):
    digit = 0
    sum =0
    while(no != 0):
        digit = no %10
        sum = sum + digit
        no = no // 10

    return sum

def main():
    No = 0
    print("Enter Number : ")
    No = int(input())
    Ret = sum_digits(No)
    print("Sumession of digit is : ", Ret)
main()

