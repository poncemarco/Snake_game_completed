
"""Se crea una clase Animal que es la superior, y una clase Fish de clase inferior que puede usar sus atributos"""
class Animal:
    def __int__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __int__(self):
        super().__int__()
    def swim(self):
        print('moving in water')
nemo =Fish()
nemo.swim()
"""Así Nemo puede usar el atributo de animal, que es respirar y además las de un pez"""
nemo.breathe()