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
    #ABILITY TEST
    ability = Ability('Dubbger', 50)

    my_hero = Hero('John', 200)
    my_hero.add_ability(ability)
    print(my_hero.abilities)

    # !!! I  NEED HELP IN MY CURRENT_HEALTH VARIABLE
    print(my_hero.current_health)
    
    ability = Ability('debbuger name', 20)
    print(ability.name)
    

