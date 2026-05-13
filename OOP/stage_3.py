import random

class Monster:
    def __init__(self, name, hp, dmg, ):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def take_damage(self, damage):
        self.hp -= damage
        print(f'{self.name} получает {damage} урона. HP: {self.hp}')
        return damage

    def attack_hunter(self, hunter):
        hunter.hp -= self.dmg
        print(f'{self.name} атакует {hunter.name} и наносит {self.dmg} урона! HP охотника: {hunter.hp}')



class Zombie(Monster):
    def __init__(self, name,):
        super().__init__(name, hp=120, dmg=15)

    """Не имеет особенности"""
    def take_damage(self, damage):
        self.hp -= damage
        print(f'{self.name} теряет конечность! Получено: {damage}. HP: {self.hp}')
        return damage


class Vampire(Monster):
    def __init__(self, name):
        super().__init__(name, hp=80, dmg=15)

    """Поглощает 5 урона при каждом попадании"""
    def take_damage(self, damage):
        absorbed = min(5, damage)
        actual_damage = damage - absorbed
        self.hp -= actual_damage
        print(f'{self.name} поглощает 5 урона! Получено: {actual_damage}. HP: {self.hp}')
        return actual_damage


class Ghost(Monster):
    def __init__(self, name):
        super().__init__(name, hp=60, dmg=20)

    """30% шанс уклониться от удара"""
    def take_damage(self, damage):
        if random.random() < 0.3:
            print(f'{self.name} уклоняется от удара! Получено: 0. HP: {self.hp}')
            return 0
        else:
            self.hp -= damage
            print(f'{self.name} получает {damage} урона. HP: {self.hp}')
            return damage


class Werewolf(Monster):
    def __init__(self, name):
        super().__init__(name, hp=100, dmg=25)
        self.transformed = False

    """При HP < 50 трансформируется и сообщает об этом"""
    def take_damage(self, damage):
        old_hp = self.hp
        self.hp -= damage

        if not self.transformed and old_hp >= 50 and self.hp < 50:
            self.transformed = True
            print(f'{self.name} трансформируется в зверя! Получено: {damage}. HP: {self.hp}')
        else:
            print(f'{self.name} получает {damage} урона. HP: {self.hp}')

        return damage


class Weapon:
    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg

    def use(self, monster):
        pass


class SilverSword(Weapon):
    def __init__(self, name = 'Серебрянный меч'):
        super().__init__(name, dmg=30)

    def use(self, monster):
        print(f"Охотник взмахивает оружием {self.name} и наносит удар!")
        monster.take_damage(self.dmg)


class HolyWater(Weapon):
    def __init__(self, name = 'Святая вода'):
        super().__init__(name, dmg=20)

    def use(self, monster):
        print(f"Охотник брызгает {self.name} на {monster.name}! Монстр шипит от боли!")
        monster.take_damage(self.dmg)


class CrossbowBolt(Weapon):
    def __init__(self, name = 'Арбалет'):
        super().__init__(name, dmg=25)

    def use(self, monster):
        print(f"Охотник стреляет из арбалета! Болт вонзается в {monster.name}!")
        monster.take_damage(self.dmg)

weapons = [SilverSword(), HolyWater(), CrossbowBolt()]
zombie = Zombie("Зомби")
for w in weapons:
    w.use(zombie)
# Полиморфизм: один цикл — три разных удара!
