Addition = lambda A,B : A + B

Substraction = lambda A,B : A - B

no1 = 0
no2 = 0
ans = 0

no1=int(input("Enter First Number :"))    # --> 11
no2=int(input("Enter Second Number :"))   # --> 10

ans = Addition(no1 ,no2)        # ans = no1 + no2    -->  ans = 11 + 10
print("Addition is : ",ans)

ans = Substraction(no1 ,no2)    # ans = no1 - no2    -->  ans = 11 - 10
print("Substractin is : ",ans)