class Parent:
    def __init__(self):
        print("Inside Parent Constructor")
        self.No1 = 10
        self.No2 = 20

        def Fun(self):
            print("Inside Fun Method of Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child Constructor")
        self.A = 11
        self.B = 21

        def Sun(self):
            print("Inside Sun Method of Child")

cobj = Child()