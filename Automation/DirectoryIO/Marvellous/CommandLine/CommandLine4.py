import sys
# python3 CommandLine4.py 11 10
def main():
    print("Addition using command Line :",end="")
    
    no1 = int(sys.argv[1])
    no2 = int(sys.argv[2])
    print(no1 + no2)

if __name__ == "__main__":
    main()