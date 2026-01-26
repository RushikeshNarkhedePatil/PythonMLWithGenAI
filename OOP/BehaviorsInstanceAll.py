class Demo:
    No = 10

    def __init__(self,A,B):
        self.Value1 = A
        self.Value2 = B

    def fun(self):
        print("Inside Instance Method fun : ",self.Value1 , self.Value2)

    @classmethod
    def Sun(cls):
        print("Inside Class Method Sun :",cls.No)

    @staticmethod
    def gun():
        print("Inside static method gun : ",Demo.No)

Demo.Sun()
print("Class Variable No :",Demo.No)

obj = Demo(11,21)
obj.fun()
print("Instance Variables : ", obj.Value1 , obj.Value2)

Demo.gun()