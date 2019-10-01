import random

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
    def __init__(self, name):
        self.name = name 
        self.starting_health = 100
        self.current_health = self.starting_health
        self.armors = list()
        self.abilities = list()
        self.kills = 0
        self.deaths = 0
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        #add armor to the armor list
    def add_armor(self, armor):
        self.armors.append(armor)
    #add kill and death depending on num_kills and num_deaths
    def add_kills(self, num_kills):
         self.kills += num_kills
    def add_deaths(self, num_deaths):
        self.deaths += num_deaths
    #add abilities to the abilities list
    def add_ability(self, ability):
        self.abilities.append(ability)
    
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
        if self.current_health > opponent.current_health:
            result += self.name
            opponent.add_deaths(1)
        else:
            result += opponent.name 
            opponent.add_kills(1)
            self.add_deaths(1)

        print(result + ' You Win!')
class Weapon(Ability):
    #return between the half of attack strength and the full value of attack strength
    def attack(self):
        return random.randint(self.attack_strength // 2, self.attack_strength)
class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        if self.name in self.heroes: 
            self.heroes.remove(self.name)
        else: 
            return 0
    def add_hero(self, hero):
        self.heroes.append(hero)
           
    def view_heroes(self):
        print([hero for hero in self.heroes])
    #attack, revive, and stat methods here:
    def attack(self, other_team):
        first_hero = random.choice(self.heroes)
        second_hero = random.choice(other_team.heroes)
        while first_hero.is_alive() and second_hero.is_alive():
            first_hero.fight(second_hero)
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.
        
    #revive every hero in list
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health
    #loop through hero list to print hero name and the ratio of kills to deaths
    def stats(self):
        for hero in self.heroes:
           print(hero.name, hero.kills/hero.deaths)

#arena class 
class Arena:
    def __init__(self):
        self.team1 = Team('DC')
        self.team2 = Team('Marvel')
    #asks user for name and damage magnitude for weapon, armor, and ability
    def create_ability(self):
        skill = input('Enter ability: ')
        max_damage = int(input('Enter ability magnitude: '))
        ability = Ability(skill, max_damage)
        return ability
    def create_weapon(self):
        name = input('Enter weapon name: ')
        max_damage = int(input('Enter weapon damage: '))
        weapon = Weapon(name, max_damage)
    def create_armor(self):
        name = input('Enter armor name: ')
        max_damage = int(input('Enter armor damage: '))
        armor = Armor(name, max_damage)
    def create_hero(self):
        name = input('Enter Hero Name: ')
        hero = Hero(name)
        selection = ['abilities', 'armor', 'weapons']
        index = 0
        while index < 3:
            user_response = input('Do you want ' + selection[index] + ". (Y/N)")
            if index == 0 and user_response.lower() == 'y':
                hero.add_armor(self.create_armor())
            elif index == 1 and user_response.lower() == 'y':
                hero.add_weapon(self.create_weapon())
            elif index == 2 and user_response.lower() == 'y':
                hero.add_ability(self.create_ability())
            else:
                index += 1
            if len(hero.abilities) == 0 and index == 3:
                print('You need at least one ability!')
                index = 2
        return hero
    def build_team_one(self):
        name = str(input('Enter name for team one: '))
        self.team1 = Team(name)
        heroes = int(input('Enter number of heroes on team one: '))

        for i in range(heroes):
            hero = self.create_hero()
            self.team1.add_hero(hero)

    def build_team_two(self):
        name = input('Enter name for team two: ')
        self.team2 = Team(name)
        heroes = int(input('Enter number of heroes on team one: '))

        for i in range(heroes):
            hero = self.create_hero()
            self.team2.add_hero(hero)
    def team_battle(self):
        self.team1.attack(self.team2)
    #Iterate through every hero to check for alive and dead teams
    def team_deaths(self, team_alive):
        team_deaths = 0
        for hero in team_alive:
            if hero.current_health == 0:
                team_deaths += 1
        if team_deaths == len(team_alive):
            return True
        else:
            return False

    def show_stats(self):
        team1 = self.team_deaths(self.team1.heroes)
        team2 = self.team_deaths(self.team2.heroes)        
        
        if team1 == False:
            print("The winner is: {}".format(self.team1.name))
            for hero in self.team1.heroes:
                if hero.is_alive():
                    print('The survivors are: ' + hero.name)
        elif team2 == False:
            print("The winner is: {}".format(self.team1.name))
            for hero in self.team2.heroes:
                if hero.is_alive():
                    print('The survivors are: ' + hero.name)
                else:
                    print("All of my teamates are dead. Game Over!")
        elif team1 == False and team2 == False:
            print("DRAW!")

        print("Team One Kill/Death: {}".format(self.team1.stats()))
        print("Team One Kill/Death: {}".format(self.team2.stats()))
    
    

    

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team1.revive_heroes()
            arena.team2.revive_heroes()
