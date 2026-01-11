def Sumession(Arr):
    Sum = 0
    for i in range(len(Arr)):
        Sum = Sum + Arr[i]
    return Sum

def main():
    size = 0
    Ret = 0
    print("Enter the number of element :")
    size = int(input())
    Data = list()
    
    print("Enter the element :")
    value = 0
    for i in range(size):
        value = int(input())
        Data.append(value)
    
    Ret = Sumession(Data)

        
    print("Sumession is : ",Ret)

if __name__ == "__main__":
    main()