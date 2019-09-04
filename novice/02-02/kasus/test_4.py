
import unittest

class Assasin:
    def __init__(self,weapons=2):
        self.weapons = weapons
        #Assasin is a fictional character which has two weapons called Katar on his hands, no matter his skills or attributes.

class Agility(Assasin):
    def __init__(self,Attribute='Agility',speed_cap=480):
        Assasin.__init__(self)
        self.Attribute = Attribute
        self.speed_cap = speed_cap 
        #it describes his main attributes is attack speed.

        self.speed = 280

    def levelup(self):
        self.speed = self.speed_cap

class Strength(Assasin):
    def __init__(self,Attribute='Strength',damage_second=3):
        Assasin.__init__(self)
        self. Attribute = Attribute
        self.damage_second = damage_second
        #describes about his other abilities, strength, to kill enemy called damage per second.

        self.damage = 1

    def rebuff(self):
        self.damage = self.damage_second

class Hybrid(Agility, Strength):
    def __init__(self,Attribute='Hybrid',speed_cap=420,damage_second=5):
        Agility.__init__(self,Attribute,speed_cap)
        Strength.__init__(self,Attribute,damage_second)
        #there is a hybrid type off Assassin which has both of the abilities Agility and Strength.

AssassinCross = Hybrid()
#print(AssassinCross.speed)
#print(AssassinCross.damage)

#AssassinCross.rebuff()
#print(AssassinCross.damage)

class Mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(AssassinCross.damage, 2)

if __name__ == '__main__':
    unittest.main()