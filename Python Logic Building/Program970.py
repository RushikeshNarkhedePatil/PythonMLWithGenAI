
def copy_small(brr):
    Result = ""

    for ch in brr:
        if ch >='a' and ch <='z':
            Result = Result + ch
            
    return Result

def main():
    print("Enter string : ")
    Arr = input()

    Ret = copy_small(Arr)

    print("Updated string is : ",Ret)


main()

