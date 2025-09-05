from enemy import Enemy
import random


class Boss_Toji(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 500
        self.attack_power = random.randint(15, 25)

    def inverted_spear_of_heaven(e):
        print("Toji used the Inverted Spear of Heaven to bypass Infinity!")
        return 100
