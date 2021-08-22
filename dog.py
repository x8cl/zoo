from animal import Animal

class Dog(Animal):

    def __init__(self, name, age, color, health=0, happiness=0):
        super().__init__(name, age, health, happiness)
        self.color = color