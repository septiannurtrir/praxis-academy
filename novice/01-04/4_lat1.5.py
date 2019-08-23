#super()

class MybaseClass:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class MyDerivedClass(MyBaseClass):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z