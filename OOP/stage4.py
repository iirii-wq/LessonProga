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

    def take_damage(self, damage):
        """Не имеет особенности"""
        new_hp = self.get_hp() - damage
        self.set_hp(new_hp)
        print(f'{self.get_name()} теряет конечность! Получено: {damage}. HP: {self.get_hp()}')
        return damage


class Vampire(Monster):
    def __init__(self, name):
        super().__init__(name, hp=80, dmg=15)

    def take_damage(self, damage):
        """Поглощает 5 урона при каждом попадании"""
        absorbed = min(5, damage)
        actual_damage = damage - absorbed
        new_hp = self.get_hp() - actual_damage
        self.set_hp(new_hp)
        print(f'{self.get_name()} поглощает 5 урона! Получено: {actual_damage}. HP: {self.get_hp()}')
        return actual_damage


class Ghost(Monster):
    def __init__(self, name):
        super().__init__(name, hp=60, dmg=20)

    def take_damage(self, damage):
        """30% шанс уклониться от удара"""
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

    def take_damage(self, damage):
        """При HP < 50 трансформируется и сообщает об этом"""
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


class Hunter:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100
        self.__weapons = [] # Приватный список для хранения оружия

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def is_alive(self):
        return self.__hp > 0

    def add_weapon(self, weapon):
        """Добавляет оружие в инвентарь"""
        self.__weapons.append(weapon)
        print(f"{self.get_name()} добавил {weapon.get_name()} в инвентарь!")

    def show_inventory(self):
        """Выводит список оружия с номерами"""
        if not self.__weapons:
            print(f"Инвентарь {self.get_name()} пуст!")
            return

        print(f"\n=== Инвентарь охотника {self.get_name()} ===")
        for i, weapon in enumerate(self.__weapons, 1):
            print(f"{i}. {weapon.get_name()} (урон: {weapon.get_dmg()})")
        print("=" * 40)

    def attack(self, weapon_index, monster):
        """Атакует монстра указанным оружием по индексу"""
        if not self.is_alive():
            print(f"{self.get_name()} мёртв и не может атаковать!")
            return False

        if weapon_index < 1 or weapon_index > len(self.__weapons):
            print(f"Неверный индекс оружия! Доступны номера от 1 до {len(self.__weapons)}")
            return False

        weapon = self.__weapons[weapon_index - 1]
        print(f"\n{self.get_name()} атакует монстра {monster.get_name()}!")
        weapon.use(monster)

        # Проверяем, жив ли монстр после атаки
        if not monster.is_alive():
            print(f"{monster.get_name()} повержен!")

        return True

# Проверка класса охотника:

if __name__ == "__main__":
    # Создаём охотника
    hunter = Hunter("Ван Хельсинг")

    # Создаём оружие
    silver_sword = SilverSword()
    holy_water = HolyWater()
    crossbow = CrossbowBolt()

    # Добавляем оружие в инвентарь
    hunter.add_weapon(silver_sword)
    hunter.add_weapon(holy_water)
    hunter.add_weapon(crossbow)

    # Показываем инвентарь
    hunter.show_inventory()

    # Создаём монстра
    zombie = Zombie("Зомби")
    print(f"\nПоявляется монстр: {zombie.get_name()} (HP: {zombie.get_hp()})")

    # Атакуем разным оружием
    hunter.attack(1, zombie)  # Серебряный меч
    hunter.attack(2, zombie)  # Святая вода
    hunter.attack(3, zombie)  # Арбалет

    # Показываем финальный статус
    print(f"\n=== Финальный статус ===")
    zombie.show_status()
    print(f"Охотник {hunter.get_name()} HP: {hunter.get_hp()}")