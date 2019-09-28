import random
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print('woof!!!')

my_dogs = list()

my_dogs.append(Dog('james', 'husky'))
my_dogs.append(Dog('james', 'pitbull'))

for dog in my_dogs:
    dog.bark()

    def sit(self):
        print('Sit now!')
    def roll_over(self):
        print('roll!')
class Ability:
    def __init__(self, name, attack_strength):
        self.name = name 
        self.attack_strength = attack_strength
    def attack(self):
        return random.randint(0, self.attack_strength)

      

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block(self):
        return random.randint(0, self.max_block)
        
  
class Hero:
    def __init__(self, name, current_health, starting_health = 100):
        self.name = name 
        self.starting_health = starting_health
        self.current_health = current_health
        self.armors = list()
        self.abilities = list()
    def add_ability(self, ability):
        self.abilities.append(ability)
        
    def attack(self):
        total_attack = 0 
        for ability in self.abilities:
            total_attack += ability.attack()
        return total_attack
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
    # If you run this file from the terminal
    # this block of code is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
    #ERROR:Attack method Value returns none
    

