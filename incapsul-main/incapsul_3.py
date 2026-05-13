class BestiaryEntry:
    def __init__(self, name, species, age, weakness, habitat, loot):
        self.name = name
        self.species = species
        self.age = age
        self.weakness = weakness
        self.habitat = habitat
        self.loot = loot


    def isprivate(self, field):
        if field == "name":
            self.__name = self.name
            del self.name
            print("Имя чудовища скрыто во мраке!")
        elif field == "species":
            self.__species = self.species
            del self.species
            print("Вид существа больше нет!")
        elif field == "age":
            self.__age = self.age
            del self.age
            print("Возраст монстра замеряется!")
        elif field == "weakness":
            self.__weakness = self.weakness
            del self.weakness
            print("Слабость существа теперь тайна!")
        elif field == "habitat":
            self.__habitat = self.habitat
            del self.habitat
            print("Место обитания стерется с карт!")
        elif field == "loot":
            self.__loot = self.loot
            del self.loot
            print("Добыча надежно спрятана!")


entry = BestiaryEntry("Фенрир", "Оборотень", 300, "Серебро", "Темный лес", "Волчьяшкура")
entry.isprivate("weakness")
entry.isprivate("loot")