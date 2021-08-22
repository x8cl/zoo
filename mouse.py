from animal import Animal

class Mouse(Animal):

    def __init__(self, name, age, gender, health=0, happiness=0):
        super().__init__(name, age, health, happiness)
        self.gender = gender