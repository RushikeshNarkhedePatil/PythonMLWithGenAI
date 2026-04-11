
def count_small(brr):
    icount = 0
    for ch in brr:
        if ch >= 'a' and ch <= 'z':
            icount = icount  + 1
    return icount


def main():
    print("Enter string : ")
    Arr = input()

    count = count_small(Arr)
    print("Number of small character are : ", count)

main()

