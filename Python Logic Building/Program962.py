
def maximum(brr):
    max = brr[0]
    for i in range(len(brr)):
        if brr[i] > max:
            max = brr[i]

    return max

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

    Ret = maximum(Arr)
    print("Maximum number is : ",Ret)

main()

