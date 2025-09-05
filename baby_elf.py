from enemy import Enemy


class Baby_Elf(Enemy):
    def cry():
        print("WAHHHH WAHHHHHHHHHHHHHHHHHHH")

    # override take_damage

    def take_damage(self, damage):
        print("you hit a baby you monster")
        return super.take_damage(damage)
