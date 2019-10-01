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
    #add abilities to the abilities list
    def add_ability(self, ability):
        self.abilities.append(ability)
    #add armor to the armor list
    def add_armor(self, armor):
        return self.armors.append(armor)
    #runs a loop through abilities list and adds total attack
    def attack(self):
        total_attack = 0 
        for ability in self.abilities:
            total_attack += ability.attack()
        return total_attack
        
    #runs a loop through armors list and adds total damage
    def defend(self):
        damage = 0
        for armor in self.armors:
            damage += armor.block()
        return damage
        
    # current health minus damage_total
    def take_damage(self,damage):
        damage_total = damage - self.defend()
        self.current_health -= damage_total
        pass
    #return false if current health is > 0
    def is_alive(self):
        return self.current_health > 0 == False
    #fight method    
    def fight(self, opponent):
        result = ""
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        
        pass 
    
if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(20)
    print(hero.is_alive())