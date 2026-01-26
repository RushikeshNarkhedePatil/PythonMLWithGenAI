class Parrent:
    def __init__(self):
        print("Inside Parrent Construtor")

    def Fun(self):
        print("Inside Fun Method of parent")

    
class Child(Parrent):
    def __init__(self):
        super().__init__()
        print("Inside child constructor")

    def Fun(self):
        super().Fun()
        print("Inside Fun method of child")

cobj = Child()

cobj.Fun()

