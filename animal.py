import random

class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        return ("Hi my name is {}, health level {} and happiness level {}".format(self.name, self.health,self.happiness))

    def feed(self):
        self.health += random.randint(0,10)
        self.happiness += random.randint(0,10)
        return print(self.display_info())