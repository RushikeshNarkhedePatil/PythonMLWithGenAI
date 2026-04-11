
def display_digit(no):
    digit = 0
    while(no != 0):
        digit = no %10
        print(digit)
        no = no // 10 # floar division remove point value /

def main():
    No = 0
    print("Enter Number : ")
    No = int(input())
    display_digit(No)
main()

