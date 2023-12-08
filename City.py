import gameSetup


class City():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.currentPop = 1
        self.nextPop = 3
        self.progressPop = 0
        self.food = 0
        self.gold = 0
        self.cult = 0
        self.currentFields = 1
        self.nextField = 5
        self.firstField = gameSetup.board.get_field(x,y)
        # make colors of aquired fields
        self.Fields = [gameSetup.board.get_field(x,y)]

    def get_food_income(self):
        s = 0
        for i in self.Fields:
            s += i.food
        return s

    def get_gold_income(self):
        s = 0
        for i in self.Fields:
            s += i.gold
            print("s_gold" + str(s))
        return s

    def get_cult_income(self):
        s = 0
        for i in self.Fields:
            s += i.cult
        return s

    def update_resources(self):  # on nezt turn
        # print("food inc:",self.getFoodIncome())
        # print(self.getGoldIncome())
        # print(self.getCultIncome())
        self.food += self.get_food_income()
        self.consume_food()
        if self.progressPop >= self.nextPop:
            self.expand_pop()
        self.gold += self.get_gold_income()
        self.cult += self.get_cult_income()
        if self.cult >= self.nextField:
            self.acquire_field()
        print("pop" + str(self.currentPop))
        print("food" + str(self.food))

    def consume_food(self):
        self.food -= self.currentPop  # consumption
        if self.food < 0:  # too low food
            self.progressPop -= self.currentPop  # consuming from storage
            if self.progressPop < 0:  # too low storage
                self.kill_pop()
                self.progressPop = 0
            self.food = 0
        self.progressPop += self.food  # surplus adding to storage

    def kill_pop(self):
        self.currentPop -= 1
        # here do sth -remove workers from tiles,
        if self.currentPop < 0:
            print("test")
            # self.destroyCity()

    def expand_pop(self):
        self.currentPop += 1
        self.nextPop *= 2.5  # set higher restriction for new pop
        gameSetup.board.get_field(self.x,self.y).update_pop(self.currentPop)

    def find_new_field(self):
        c_max = 0
        c_coord = [0, 0]
        for i in self.Fields:
            s = 0
            s_max = 0
            s_coord = [0, 0]
            s = self.calc_field_score(i.xPos, i.yPos)
            if gameSetup.board[i.xPos][i.yPos].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
                s = self.calc_field_score(i.xPos + 1, i.yPos)
            if gameSetup.board[i.xPos + 1][i.yPos].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
                s = self.calc_field_score(i.xPos, i.yPos + 1)
            if gameSetup.board[i.xPos][i.yPos + 1].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
                s = self.calc_field_score(i.xPos - 1, i.yPos)
            if gameSetup.board[i.xPos - 1][i.yPos].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
                s = self.calc_field_score(i.xPos, i.yPos - 1)
            if gameSetup.board[i.xPos][i.yPos - 1].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
                s = self.calc_field_score(i.xPos + 1, i.yPos + 1)
            if gameSetup.board[i.xPos + 1][i.yPos + 1].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
                s = self.calc_field_score(i.xPos - 1, i.yPos - 1)
            if gameSetup.board[i.xPos - 1][i.yPos - 1].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
                s = self.calc_field_score(i.xPos - 1, i.yPos + 1)
            if gameSetup.board[i.xPos - 1][i.yPos - 1].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
                s = self.calc_field_score(i.xPos + 1, i.yPos - 1)
            if gameSetup.board[i.xPos - 1][i.yPos - 1].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
            if s_max > c_max:
                c_max = s_max
                c_coord[0] = s_coord[0]
                c_coord[1] = s_coord[1]
        return c_coord

    def calc_field_score(self, x, y):
        if gameSetup.board.get_field(x,y).food <= 0:
            return 0
        else:
            return gameSetup.board[x][y].food + gameSetup.board[x][y].cult + gameSetup.board[x][y].gold

    def acquire_field(self):
        coord = self.find_new_field()
        if coord[0] != 0 and coord[1] != 0:
            self.Fields += gameSetup.board[coord[0]][coord[1]]
        # make colors of acquired fields
        self.nextField *= 2.6
