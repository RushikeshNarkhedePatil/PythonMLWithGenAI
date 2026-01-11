def main():
    size = 0
    print("Enter the number of element :")
    size = int(input())
    Data = list()
    
    print("Enter the element :")
    value = 0
    for i in range(size):
        value = int(input())
        Data.append(value)
    
    Sum = 0
    for i in range(size):
        Sum = Sum + Data[i]
        
    print("Sumession is : ",Sum)

if __name__ == "__main__":
    main()