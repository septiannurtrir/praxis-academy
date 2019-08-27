import unittest

class Hantu:
    def __init__(self, name):
        self.name = name

    def age(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Kuntilanak(Hantu):
    def age(self):
        return self.name+' 900'

class Tuyul(Hantu):
    def age(self):
        return self.name+' 200'

Markunti = Kuntilanak('Markunti')
Sontol = Tuyul('Sontol')

#print(Markunti.age())
#print(Sontol.age())

class Mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(Sontol.age, 200)

if __name__ == '__main__':
    unittest.main()