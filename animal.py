class Animal:
    def __init__(self, name):
        self.name = name 
    def eat(self):
        print(f'is eating{self.name}')
    def drink(self):
        print(f'is drinking{self.name}')