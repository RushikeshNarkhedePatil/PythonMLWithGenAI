def main():
    Ans = 0
    try:
        print("Inside try")
        print("Enter First Number :")
        No1 = int(input())

        print("Enter Second Number :")
        No2 = int(input())

        Ans = No1 / No2
    except:
        print("Inside except")
    finally:
        print("Inside finally")

    print("Division is : ",Ans)


if __name__ == "__main__":
    main()