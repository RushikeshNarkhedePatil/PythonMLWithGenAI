
def sumesion(brr):
    sum = 0
    for no in brr:
        sum = sum + no

    return sum

def main():
    size = 0
    Arr = [] 
    value = 0

    print("Enter number of element : ")
    size = int(input())

    print("Enter the elements : ")

    for i in range(size):
        value = int(input())
        Arr.append(value)

    Ret = sumesion(Arr)
    print("Sumession is : ",Ret)

main()

