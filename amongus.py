#AmongUs
class Player():
    a = ["red", "blue", "green"]
    def __init__(self, name):
        self.name = name

    def color(self):
        if Player.a == []:
            print("Мест больше нет")
            return
        s = input(f"Выберите цвет: {Player.a} ")
        if s in Player.a:
            self.color = s
            del(Player.a[Player.a.index(s)])
            print("Выбран цвет ", self.color)
        else: print("Нет такого цвета ")

player1 = Player("Alice558")
player2 = Player("Mike557")
player3 = Player("LonelyMan556")
player4 = Player("LonelyMan557")

player1.color()
player2.color()
player3.color()
player4.color()
print(Player.a)
