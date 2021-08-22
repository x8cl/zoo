class Zoo:

    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        for animal in self.animals:
            if animal.name == new_animal.name:
                return False
        self.animals.append(new_animal)
        return True
        
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            print(animal.display_info())

