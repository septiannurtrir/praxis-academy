#Unpickling

import pickle

class Animal:
    def __init__(self, number_of_paws, color):
        self.number_of_paws = number_of_paws
        self.color = color

class Sheep(Animal):
    def __init__(self, color):
        Animal.__init__(self, 4, color)

mary = Sheep("white")
my_pickled_mary = pickle.dumps(mary)
dolly = pickle.loads(my_pickled_mary)
dolly.color = "black"

print(str.format("Dolly is {0} ", dolly.color))
print(str.format("Mary is {0} ", mary.color))