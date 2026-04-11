
def minimum(brr):
    min = brr[0]
    for i in range(len(brr)):
        if brr[i] < min:
            min = brr[i]

    return min

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

    Ret = minimum(Arr)
    print("Minimum number is : ",Ret)

main()

