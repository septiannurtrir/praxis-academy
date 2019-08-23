#Method Resolution Order (MRO)

class Knight:
    weapon = Sword

class Magician:
    weapon = 

class Thief:
    weapon = Knife

class Archer(Magician,Thief):
    pass
