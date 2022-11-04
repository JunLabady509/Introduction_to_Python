import random
import string
import time
from entity import *
from items import *

# def check_active_quest(self,action):
#     for quest in self.quest_list:
#       if quest.action == action:
#         print("Vous avez reussi une quete")
#         self.inventory.append(quest.reward)
#         self.quest_list.remove(quest)

# La fonction StartGame() permet de démarrer commencer à jouer. 
# Elle va etre appelée quand le joueur choisira "New Game"


def startGame():
    print("Welcome to Death Game! Hope you enjoy. GG (-_-)")
    boss = monster("gobelin")

    player_name = input("Please enter your name: ")
    print("Choose your adventurer type:")
    print("1. Warrior - Meilleur en Force, moins bon en défense")
    print("2. Wizard - Meilleur en Défense, moins bon en Force")
    adventurer_type = input("Your choice: ")
    if adventurer_type == "1":
        adventurer_type = "Warrior"
    elif adventurer_type == "2":
        adventurer_type = "Wizard"
    else: 
        print("Invalid Choice, try again")
        adventurer_type = input("Your choice: ")

    
    actual_player = Player(player_name,adventurer_type)
    print("Your Available Weapons :", see_inventory(actual_player))
    
    print("Votre Frère a été enlevé par le monstre Jet-Li")
    keep_fighting = True
    while (keep_fighting is True):
        print("Current Score:")
        print("You - {0}".format(actual_player.wins))
        print("boss - {0}".format(boss.wins))

        boss.hp = 100
        actual_player.hp = 100
        fight_round(boss, actual_player)
        print()
        response = input("Play another round?(Y/N)")
        if (response.lower() == "n"):
            break


def fight_round(boss, actual_player):
    fight_in_progress = True
    current_player = boss
    
    while fight_in_progress:
        # Changer de tour après chaque attaque
        if (current_player == boss):
            current_player = actual_player
        else:
            current_player = boss
            
        print()
        print(
            "You have {0} hp remaining and the "
            "boss has {1} hp remaining."
            .format(actual_player.hp, boss.hp))
        print()
        
        if (current_player == actual_player):
            print("Available attacks:")
            print("1. Electrocute - Causes moderate damage.")
            print("2. Wild Swing - high or low damage, "
                  "depending on your luck!")
            print("3. Nature's Kiss - Restores a moderate amount of hp.")
            move = select_attack()
        else:
            move = boss_attack(boss.hp)
            
        if (move == 1):
            damage = random.randrange(18, 25)
            if (current_player == actual_player):
                boss.damage(damage, actual_player.name)
            else:
                actual_player.damage(damage, boss.name)
        elif (move == 2):
            damage = random.randrange(10, 35)
            if (current_player == actual_player):
                boss.damage(damage, actual_player.name)
            else:
                actual_player.damage(damage, boss.name)
        # elif (move == 3):
        #     heal = random.randrange(18, 25)
        #     current_player.calculate_heal(heal)
        else:
            print ("The input was not valid. Please select a choice again.")

        if (actual_player.hp == 0):
            print("Sorry, you lose!")
            boss.wins += 1
            fight_in_progress = False

        if (boss.hp == 0):
            print("Congratulations, you beat the boss!")
            actual_player.wins += 1
            fight_in_progress = False

def select_attack():
    valid_input = False
    while (valid_input is False):
        print()
        choice = input("Select an attack: ")
        if (parse_int(choice) is True):
            return int(choice)
        else:
            print("The input was invalid. Please try again.")
            
def parse_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

def boss_attack(hp):
    sleep_time = random.randrange(2, 5)
    print("....thinking....")
    time.sleep(sleep_time)

    if (hp <= 35):
        # Have the computer heal ~50% of its turns when <= 35
        result = random.randint(1, 6)
        if (result % 2 == 0):
            return 3
        else:
            return random.randint(1, 2)
    elif (hp == 100):
        return random.randint(1, 2)
    else:
        return random.randint(1, 3)
    
    