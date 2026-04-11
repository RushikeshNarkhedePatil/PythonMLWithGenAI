
def count_capital(brr):
    icount = 0
    for ch in brr:
        if ch >= 'A' and ch <= 'Z':
            icount = icount  + 1
    return icount


def main():
    print("Enter string : ")
    Arr = input()

    count = count_capital(Arr)
    print("Number of captal character are : ", count)

main()

