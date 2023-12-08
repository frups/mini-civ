from City import City


class Player():
    def __init__(self, name):
        self.name = name
        self.Cities = []
        self.gold = 0

    def develop_city(self, x, y):
        self.Cities.append(City(x, y))

    def update_account(self):  # on next turn
        s = 0
        for i in self.Cities:
            i.update_resources()
            s += i.gold
        self.gold = s
