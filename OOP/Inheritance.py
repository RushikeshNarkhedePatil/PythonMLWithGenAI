class Parrent:
    def __init__(self):
        print("Inside Parrent Construtor")
        self.No1 = 10
        self.No2 = 20

    def Fun(self):
        print("Inside Fun Method of parrent")

    
class Child(Parrent):
    def __init__(self):
        super().__init__()
        print("Inside child constructor")
        self.A = 11
        self.B = 21

    def Sun(self):
        print("Inside Sun method of child")

cobj = Child()
