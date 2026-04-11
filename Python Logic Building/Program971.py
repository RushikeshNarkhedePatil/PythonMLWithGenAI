
def count_capital(brr):
    icount = 0
    for ch in brr:  # issue 
        if ch >= 65 and ch <= 90:
            icount = icount  + 1
    return icount


def main():
    print("Enter string : ")
    Arr = input()

    count = count_capital(Arr)
    print("Number of captal character are : ", count)

main()

