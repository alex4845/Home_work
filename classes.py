class Elevator():
    def __init__(self, total_levels = 5, level = 3):
        self.total_levels = total_levels
        self.level = level

    def up(self):
        if self.level == self.total_levels: print("MAX LEVEL")
        else:
            self.level += 1
            print(self.level, "LEVEL")

    def down(self):
        if self.level == 1: print("MIN LEVEL")
        else:
            self.level -= 1
            print(self.level, "LEVEL")

class Newelevator(Elevator):
    def __init__(self, total_levels = 5, level = 3):
        super().__init__(total_levels, level)

    def move(self, new_level):
        if new_level > self.total_levels or new_level < 1:
            print("NOT LEVEL")
        else:
            self.level = new_level
            print(self.level, "LEVEL")


elevator1 = Elevator()
elevator2 = Elevator(1, 1)
elevator2.down()
elevator3 = Newelevator(12, 5)
elevator3.move(1)









exit(0)

class Rectangle():
    def __init__(self, a = 5, b = 10):
        self.a = a
        self.b = b

    def calculat_area(self):
        print ("Площадь = ", end = "")
        return self.a*self.b

    def draw(self):
        for i in range(0, self.a):
            print("")
            for y in range (0, self.b):
                print ("*", end = "")


class Square(Rectangle):
    def __init__(self, a, b, c = 3):
        super().__init__(a, b)
        self.c = c






r1 = Rectangle()
r2 = Rectangle(5, 3)
print(r1.calculat_area())
#print(r2.calculat_area())
#r2.draw()
r1.draw()
r3 = Square(3, 3, 3)
r3.draw()





#AmongUs( НЕ ЗАКОНЧЕНО)
class Player():
    def __init__(self, name):
        self.name = name

    def color(self):
        a = ["red", "blue", "green"]
        s = input(f"Change color: {a}  ")
        if s in a:
            del(a[a.index(s)])
            print (a)

        self.color = s
        print(self.name, self.color)





player1 = Player("Alice558")
player2 = Player("Mike557")
player3 = Player("LonelyMan556")
player4 = Player("LonelyMan557")
player1.color()
player2.color()



class Money():
    def __init__(self, dollars, cents):
        self.__dollars = dollars
        self.__cents = cents

    def total_cents(self):
        self.total_cents = self.__dollars*100 + self.__cents
        return self.total_cents

    def get_cents(self):
        return self.__cents

    def get_dollars(self):
        return self.__dollars

    def set_cents(self, cents):
        if cents != int(cents) or cents < 0 or cents > 100:
            print ("Error cents")
        else:
            self.__cents = cents

    def set_dollars(self, dollars):
        if dollars != int(dollars) or dollars < 0:
            print("Error dollars")
        else:
            self.__dollars = dollars

    def __str__(self):
        print(f"Ваше состояние состовляет {cash.get_dollars()} долларов и {cash.get_cents()} центов")


cash = Money(34, 77)

cash.set_dollars(-50)
cash.set_cents(85)

cash.__str__()



class Robot():
    def __init__(self, name, age, ps_sost, phis_sost):
        self.name = name
        self.age = age
        self.__ps_sost = ps_sost
        self.__phis_sost = phis_sost

    def total_sost(self):
        self.__total_sost = self.__ps_sost + self.__phis_sost
        a = self.__total_sost
        if a <= -1: return "Я чувствую себя несчастным !"
        if 0 >= a > -1: return "Я чувствую себя плохо !"
        if 0.5 >= a > 0: return "Могло быть хуже !"
        if 1 >= a > 0.5: return "Кажется, все в порядке !"
        return "Супер !!"


robot1 = Robot("Marvin", 1979, 0.2, 0.9)
robot2 = Robot("Caliban", 1993, -0.4, 0.3)
print(robot1.total_sost())
print(robot2.total_sost())





class UserMail():

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self):
        a = k.email
        if "@" in a and a.count("@") == 1:
            if "." in a[a.index("@"):] and a[a.index("@"):].count(".") == 1:
                self.__email = a
                return self.__email
        print("ошибочная почта")




k = UserMail("belosnezhka227", "prince@wait.you")
k.email = "666gmail.com"
k.set_email()
print (k.get_email())


