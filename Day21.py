#THIS IS ABOUT CLASS INHERITANCE

class Animal:
    def __init__(self):
        self.colour="green"
    
    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def swim(self):
        print("swim")
    def breathe_underwater(self):
        super().breathe()
        print("under water")

Timmy=Fish()
Timmy.breathe_underwater()