import unittest

class Hantu:
    def __init__(self,name,place):
        self.name = name
        self.place = place

class Jin(Hantu):
    def __init__(self,name,place='akik',booing='yes'):
        Hantu.__init__(self,name,place)
        self.booing = booing

Tomang = Jin('Tomang')
 #print(Tomang.name)
 #print(Tomang.place)
 #print(Tomang.booing)

class Mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(Tomang.place, "akik")

if __name__ == '__main__':
    unittest.main()

