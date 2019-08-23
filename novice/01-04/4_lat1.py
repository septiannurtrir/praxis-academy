class Hantu:
    def __init__(self, name):
        self.name = name

        def appearance(self):
            raise NotImplementedError("Subclass must implement abstract method")


class Kuntilanak(Hantu):
    def appearance(self):
        return self.name+' Kain Putih'

class Tuyul(Hantu):
    def appearance(self):
        return self.name+' Cebol'

Markunti = Kuntilanak('Markunti')
Sontol = Tuyul('Sontol')

print(Markunti.appearance())
print(Sontol.appearance())