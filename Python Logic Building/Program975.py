
def toggle_case(brr):
    Result = ""

    for ch in brr:
        if ch >='A' and ch <='Z':
            Result = Result + chr((ord(ch)+32))
        elif ch >='a' and ch <='z':
            Result = Result + chr((ord(ch)-32))
        else:
            Result = Result + ch
        
            
    return Result

def main():
    print("Enter string : ")
    Arr = input()

    Ret = toggle_case(Arr)

    print("Updated string is : ",Ret)


main()

