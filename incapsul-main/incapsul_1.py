class DarkEntity:
    def __init__(self, name, species, danger_level):
        self.__name = name
        self.__species = species
        self.__danger_level = danger_level

#    def get_name(self):
#        return self.__name
#    def get_species(self):
#        return self.__species
#    def get_danger_level(self):
#        return self.__danger_level


monster = DarkEntity('Балор','Высший вампир',99)

data = (monster._DarkEntity__name, monster._DarkEntity__species, monster._DarkEntity__danger_level)
print(data)
