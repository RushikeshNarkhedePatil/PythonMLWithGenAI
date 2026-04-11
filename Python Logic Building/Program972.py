
def count_capital(brr):
    icount = 0
    for ch in brr:  # ord used to provide ASCII value
        if ord(ch) >= 65 and ord(ch) <= 90:
            icount = icount  + 1
    return icount


def main():
    print("Enter string : ")
    Arr = input()

    count = count_capital(Arr)
    print("Number of captal character are : ", count)

main()

