import unittest

class Hantu:
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs

class Jin(Hantu):
    def __init__(self,name,legs=1,booing='yes'):
        Hantu.__init__(self,name,legs)
        self.booing = booing

Tomang = Jin('Tomang')
 #print(Tomang.name)
 #print(Tomang.legs)
 #print(Tomang.booing)

class Mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(Tomang.legs, 0)

if __name__ == '__main__':
    unittest.main()