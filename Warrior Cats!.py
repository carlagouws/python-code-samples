# ******************************************************************************************
# Description:
# Warriors Tabby Cat and Bob Cat are fighting in the street
# They each have 9 lives
# They can each attack and produce damage to their enemy's life
# They can each block and thereby counter the damage to their life and get more lives!

# Example output:
'''
        Tabby Cat attacks 1 times!
        Bob Cat retaliates with 2 swipe(s) and has 10 lives left!

        Bob Cat attacks 4 times!
        Tabby Cat retaliates with 3 swipe(s) and has 8 lives left!

        Tabby Cat attacks 0 times!
        Bob Cat retaliates with 4 swipe(s) and has 14 lives left!

        Bob Cat attacks 6 times!
        Tabby Cat retaliates with 3 swipe(s) and has 5 lives left!

        Tabby Cat attacks 2 times!
        Bob Cat retaliates with 2 swipe(s) and has 14 lives left!

        Bob Cat attacks 8 times!
        Tabby Cat retaliates with 4 swipe(s) and has 1 lives left!

        Tabby Cat attacks 5 times!
        Bob Cat retaliates with 2 swipe(s) and has 11 lives left!

        Bob Cat attacks 6 times!
        Tabby Cat retaliates with 0 swipe(s) and has -5 lives left!

        Tabby Cat's 9 lives are over and Bob Cat is victorious!
        Game Over
'''
# ******************************************************************************************

import random
import time

class Warrior:
    def __init__(self, name="", health=0, attackMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attackMax = attackMax
        self.blockMax = blockMax

    def attack(self):
        # random.random() produces a random number between 0 and 1
        attackAmount = self.attackMax * (random.random())
        # Convert float to integer
        return int(attackAmount)

    def block(self):
        blockAmount = self.blockMax * (random.random())
        return int(blockAmount)

class Battle:
    def startWar(self, warrior1, warrior2):
        while (warrior2.health > 0) and (warrior1.health > 0):
            attack1 = warrior1.attack()
            block1 = warrior2.block()
            warrior2.health = warrior2.health - attack1 + block1
            print("{} attacks {} times!".format(warrior1.name, attack1))
            print("{} defends himself with {} swipes and has {} lives left!".format(warrior2.name, block1, warrior2.health))
            print()
            if warrior2.health < 0:
                break

            time.sleep(2)       # Creates a delay of 2 seconds between each attack
            attack2 = warrior2.attack()
            block2 = warrior1.block()
            warrior1.health = warrior1.health - attack2 + block2
            print("{} attacks {} times!".format(warrior2.name, attack2))
            print("{} defends himself with {} swipes and has {} lives left!".format(warrior1.name, block2, warrior1.health))
            print()
            time.sleep(2)

        if warrior1.health > warrior2.health:
            print("{}'s 9 lives are over and {} is victorious!".format(warrior2.name, warrior1.name))
        else:
            print("{}'s 9 lives are over and {} is victorious!".format(warrior1.name, warrior2.name))
        print("Game Over")

def main():

    # Initialise the warriors
    warrior1 = Warrior("Tabby Cat", 9, 9, 5)
    warrior2 = Warrior("Bob Cat", 9, 9, 5)

    # Start the battle!
    battle = Battle()
    battle.startWar(warrior1, warrior2)

main()