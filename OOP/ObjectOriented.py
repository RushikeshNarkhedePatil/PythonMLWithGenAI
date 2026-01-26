class Arithematic:
    def Addition(self,A,B):
        return A + B

    def Substraction(self,A,B):
        return A - B
    
no1 = 0
no2 = 0
ans = 0

no1=int(input("Enter First Number :"))
no2=int(input("Enter Second Number :"))

ans = Arithematic().Addition(no1,no2)
print("Addition is : ",ans)

ans = Arithematic().Substraction(no1,no2)
print("Substractin is : ",ans)