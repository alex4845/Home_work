
class GreatTalent():
    name = "Alex"
    age = 36
    year_of_b = 2022 - age
    fav_prog_lang = "Python"
    city = "Minsk"
#    def __init__(self, name, age, year_of_b, fav_prog_lang, city):
#       self.name = name
print(GreatTalent.name, GreatTalent.age, GreatTalent.year_of_b)










exit(0)


# Students
class Student():
    def __init__(self, name, zel, ist_m, grass_v, transfig):
        self.name = name
        self.zel = zel
        self.ist_m = ist_m
        self.grass_v = grass_v
        self.transfig = transfig

    def sum_ball(self):
        print(self.name, self.zel + self.ist_m + self.grass_v + self.transfig)

germiona = Student("Germiona", 10, 10, 10, 9)
wizly = Student("Wizly", 7, 8, 7, 6)
germiona.sum_ball()
wizly.sum_ball()




