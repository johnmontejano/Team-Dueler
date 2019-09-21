import random
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print('woof!!!')
    def sit(self):
        print('Sit now!')
    def roll_over(self):
        print('roll!')
class Ability:
    def __init__(self, name, max_damage):
        self.name = name 
        self.max_damage = max_damage
    def attack(self):
      return random.randint(0, self.max_damage)

      

class Armor:
    def __init__(self, name, starting_health):
        self.name = name
        self.health = starting_health

class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name 
        self.starting_health = starting_health
    def add_ability(self, Ability):
        pass
    def attack(self):
        pass
    def defend(self, incoming_damage):
        pass
    def take_damage(self,damage):
        pass
    def is_alive(self):
        pass
    def fight(self, Hero):
        pass 

if __name__ == "__main__":
    ability = Ability('debbuging ability', 20)
    print(ability.name)
    print(ability.attack())