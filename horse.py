class Horse():
    population = 0
    def __init__(self, name, age, color, breed, hooves, weight, jockey):
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed
        self.hooves = hooves
        self.weight = weight
        self.jockey = jockey
        Horse.population +=1

    def nicker(self):
        print("Igo-go "*3)

    def hop(self):
        print("hop "*5)

    def eat(self):
        print("Horse eat")

    def sleep(self):
        print("Hrrr "*4)

horse1 = Horse ("Masha", 12, "brawn", "inglish", 4, 154, "John")
horse2 = Horse ("Isabel", 15, "blond", "american", 4, 160, "John")

print(Horse.population)


class Jockey():
    def __init__(self, name, horse):

        self.name = name
        self.horse = horse

    def ride(self):
        Horse.hop(horse1)

john = Jockey("John", "Masha")
john.ride()
print(john.name)






