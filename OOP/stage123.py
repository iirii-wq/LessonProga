import random

class Monster:
    def __init__(self, name, hp, dmg):
        self.__name = name
        self.__hp = hp
        self.__dmg = dmg

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def get_dmg(self):
        return self.__dmg

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def is_alive(self):
        return self.__hp > 0

    def show_status(self):
        print("Имя: ", self.get_name())
        print("HP: ", self.get_hp())

    def take_damage(self, damage):
        """Стандартная версия получения урона"""
        new_hp = self.get_hp() - damage
        self.set_hp(new_hp)
        print(f'{self.get_name()} получает {damage} урона. HP: {self.get_hp()}')
        return damage

    def attack_hunter(self, hunter):
        hunter.set_hp(hunter.get_hp() - self.get_dmg())
        print(
            f'{self.get_name()} атакует {hunter.get_name()} и наносит {self.get_dmg()} урона! HP охотника: {hunter.get_hp()}')


class Zombie(Monster):
    def __init__(self, name):
        super().__init__(name, hp=120, dmg=10)

    """Не имеет особенности"""
    def take_damage(self, damage):
        new_hp = self.get_hp() - damage
        self.set_hp(new_hp)
        print(f'{self.get_name()} теряет конечность! Получено: {damage}. HP: {self.get_hp()}')
        return damage


class Vampire(Monster):
    def __init__(self, name):
        super().__init__(name, hp=80, dmg=15)

    """Поглощает 5 урона при каждом попадании"""
    def take_damage(self, damage):
        absorbed = min(5, damage)
        actual_damage = damage - absorbed
        new_hp = self.get_hp() - actual_damage
        self.set_hp(new_hp)
        print(f'{self.get_name()} поглощает 5 урона! Получено: {actual_damage}. HP: {self.get_hp()}')
        return actual_damage


class Ghost(Monster):
    def __init__(self, name):
        super().__init__(name, hp=60, dmg=20)

    """30% шанс уклониться от удара"""
    def take_damage(self, damage):
        if random.random() < 0.3:
            print(f'{self.get_name()} уклоняется от удара! Получено: 0. HP: {self.get_hp()}')
            return 0
        else:
            new_hp = self.get_hp() - damage
            self.set_hp(new_hp)
            print(f'{self.get_name()} получает {damage} урона. HP: {self.get_hp()}')
            return damage


class Werewolf(Monster):
    def __init__(self, name):
        super().__init__(name, hp=100, dmg=25)
        self.__transformed = False

    """При HP < 50 трансформируется и сообщает об этом"""
    def take_damage(self, damage):
        old_hp = self.get_hp()
        new_hp = old_hp - damage
        self.set_hp(new_hp)

        if not self.__transformed and old_hp >= 50 and self.get_hp() < 50:
            self.__transformed = True
            print(f'{self.get_name()} трансформируется в зверя! Получено: {damage}. HP: {self.get_hp()}')
        else:
            print(f'{self.get_name()} получает {damage} урона. HP: {self.get_hp()}')

        return damage


class Weapon:
    def __init__(self, name, dmg):
        self.__name = name
        self.__dmg = dmg

    def get_name(self):
        return self.__name

    def get_dmg(self):
        return self.__dmg

    def use(self, monster):
        pass


class SilverSword(Weapon):
    def __init__(self, name='Серебряный меч'):
        super().__init__(name, dmg=30)

    def use(self, monster):
        print(f"Охотник взмахивает оружием {self.get_name()} и наносит удар!")
        monster.take_damage(self.get_dmg())


class HolyWater(Weapon):
    def __init__(self, name='Святая вода'):
        super().__init__(name, dmg=20)

    def use(self, monster):
        print(f"Охотник брызгает {self.get_name()} на {monster.get_name()}! Монстр шипит от боли!")
        monster.take_damage(self.get_dmg())


class CrossbowBolt(Weapon):
    def __init__(self, name='Арбалет с болтом'):
        super().__init__(name, dmg=25)

    def use(self, monster):
        print(f"Охотник стреляет из арбалета! Болт вонзается в {monster.get_name()}!")
        monster.take_damage(self.get_dmg())

weapons = [SilverSword(), HolyWater(), CrossbowBolt()]
zombie = Zombie("Зомби")
for w in weapons:
    w.use(zombie)
# Полиморфизм: один цикл — три разных удара!
