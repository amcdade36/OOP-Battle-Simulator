import random


class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 500
        self.attack_power = 30
        self.defence_power = 10

    def strike(self):
        dice = random.randint(1, 50)
        if dice == 25:
            print('Gojo: "Hollow Purple"')
            return 1000000000
        else:
            return random.randint(30, self.attack_power)

    def receive_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def reversed_cursed_technique(self):
        dice = random.randint(1, 3)
        if dice == 1:
            self.health = 200
            print('Gojo: "When you stabbed me through the throat, I gave up on counter attacking and poured all my focus into the reversed cursed technique. \nCursed energy is negative energy. While it can enhance the body, it can’t regenerate it. So you multiply that negative energy against itself \nto create positive energy. That’s the reversed cursed technique!"')