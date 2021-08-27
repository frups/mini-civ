import os
import pygame as pg
from pygame.compat import geterror
from random import seed
from random import randint

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")
size = 10
fieldSize = int(500 / size)


class Field(pg.sprite.Sprite):
    def __init__(self, width, height, xPos, yPos, address):
        pg.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.xPos = xPos
        self.yPos = yPos
        self.address = address
        self.image = pg.Surface([width - 1, height - 1])
        self.image.fill([126, 126, 126])
        self.rect = self.image.get_rect()
        self.food = randint(0, 2)
        self.gold = randint(0, 2)
        self.cult = randint(0, 2)
        print(width)
        self.owner = 0  # 0-no owner, 1-owner without city, 2-owner with city
        if pg.font:
            font = pg.font.Font(None, int(width / 1.38))
            text = font.render(str(self.food), 0, [0, 255, 0])
            textpos = text.get_rect(centerx=6)
            self.image.blit(text, textpos)
            text = font.render(str(self.gold), 0, [255, 255, 0])
            textpos = text.get_rect(centerx=self.image.get_width() - 8)
            self.image.blit(text, textpos)
            text = font.render(str(self.cult), 0, [255, 0, 0])
            textpos = text.get_rect(centery=self.image.get_height() - 8)
            self.image.blit(text, textpos)

    def updatePop(self, pop):
        if pg.font:
            font = pg.font.Font(None, int(self.width / 1.38) * 2)
            text = font.render(str(pop), 0, [64, 64, 64])
            textpos = text.get_rect(centerx=int(self.image.get_width() / 2), centery=int(self.image.get_height() / 2))
            self.image.blit(text, textpos)

    def updateResources(self, nfood, ngold, ncult):
        print("updateRes")


class Player():
    def __init__(self, name):
        self.name = name
        self.Cities = []
        self.gold = 0

    def developCity(self, x, y):
        self.Cities.append(City(x, y))

    def updateAccount(self):  # on nezt turn
        s = 0
        for i in self.Cities:
            i.updateResources()
            s += i.gold
        self.gold = s


class City():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.currentPop = 1
        self.nextPop = 3
        self.progressPop=0
        self.food = 0
        self.gold = 0
        self.cult = 0
        self.currentFields = 1
        self.nextField = 5
        self.firstField = board[x][y]
        #make colors of aquired fields
        self.Fields = [board[x][y]]

    def getFoodIncome(self):
        s = 0
        for i in self.Fields:
            s += i.food
        return s

    def getGoldIncome(self):
        s = 0
        for i in self.Fields:
            s += i.gold
            print("s_gold"+str(s))
        return s

    def getCultIncome(self):
        s = 0
        for i in self.Fields:
            s += i.cult
        return s

    def updateResources(self):  # on nezt turn
        # print("food inc:",self.getFoodIncome())
        # print(self.getGoldIncome())
        # print(self.getCultIncome())
        self.food += self.getFoodIncome()
        self.consumeFood()
        if self.progressPop>=self.nextPop:
            self.expandPop()
        self.gold += self.getGoldIncome()
        self.cult += self.getCultIncome()
        if self.cult>=self.nextField:
            self.aquireField()
        print("pop"+str(self.currentPop))
        print("food"+str(self.food))
    def consumeFood(self):
        self.food -= self.currentPop#consumption
        if self.food<0:#too low food
            self.progressPop-=self.currentPop#consuming from storage
            if self.progressPop<0:#too low storage
                self.killPop()
                self.progressPop=0
            self.food=0
        self.progressPop += self.food#surplus adding to storage
    def killPop(self):
        self.currentPop-=1
        # here do sth -remove workers from tiles,
        if self.currentPop<0:
            print("test")
            # self.destroyCity()
    def expandPop(self):
        self.currentPop+=1
        self.nextPop *= 2.5#set higher resctriction for new pop
        board[self.x][self.y].updatePop
    def findNewField(self):
        c_max=0
        c_coord=[0,0]
        for i in self.Fields:
            s=0
            s_max=0
            s_coord=[0,0]
            s=self.calcFieldScore(i.xPos,i.yPos)
            if board[i.xPos][i.yPos].owner==0:
                if s>s_max:
                    s_max=s
                    s_coord[0]=i.xPos
                    s_coord[1]=i.yPos
                s = self.calcFieldScore(i.xPos+1, i.yPos)
            if board[i.xPos+1][i.yPos].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
                s = self.calcFieldScore(i.xPos, i.yPos+1)
            if board[i.xPos][i.yPos+1].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
                s = self.calcFieldScore(i.xPos-1, i.yPos)
            if board[i.xPos-1][i.yPos].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
                s = self.calcFieldScore(i.xPos, i.yPos-1)
            if board[i.xPos][i.yPos-1].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
                s = self.calcFieldScore(i.xPos+1, i.yPos+1)
            if board[i.xPos+1][i.yPos+1].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
                s = self.calcFieldScore(i.xPos-1, i.yPos-1)
            if board[i.xPos-1][i.yPos-1].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
                s = self.calcFieldScore(i.xPos-1, i.yPos+1)
            if board[i.xPos-1][i.yPos-1].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
                s = self.calcFieldScore(i.xPos+1, i.yPos-1)
            if board[i.xPos-1][i.yPos-1].owner == 0:
                if s > s_max:
                    s_max = s
                    s_coord[0] = i.xPos
                    s_coord[1] = i.yPos
            if s_max>c_max:
                c_max=s_max
                c_coord[0]=s_coord[0]
                c_coord[1]=s_coord[1]
        return c_coord
    def calcFieldScore(self, x, y):
        if board[x][y].food<=0:
            return 0
        else:
            return board[x][y].food+board[x][y].cult+board[x][y].gold
    def aquireField(self):
        coord=self.findNewField()
        if coord[0]!=0 and coord[1]!=0:
            self.Fields+=board[coord[0]][coord[1]]
        #make colors of aquired fields
        self.nextField*=2.6


# Generate And Draw Board With Fields
def genBoard(size):
    board = []
    print("generation")
    for j in range(0, size):
        print("row: "+str(j))
        row = []
        for i in range(0, size):
            print("cell:"+str(j)+","+str(i))
            address = str(j) + str(i)
            field = Field(fieldSize, fieldSize, j * fieldSize, i * fieldSize, address)
            row.append(field)
            print(address)
            allsprites = pg.sprite.RenderPlain(field)
            allsprites.update()
            # allsprites.draw(screen,(i*fieldSize,j*fieldSize,fieldSize,fieldSize))
            screen.blit(field.image, (j * fieldSize, i * fieldSize))
            pg.display.flip()
        board.append(row)
    return board


# Initialize Everything
pg.init()
screen = pg.display.set_mode((700, 700))
pg.display.set_caption("miniCiv")
pg.mouse.set_visible(1)

# Create The Backgound
background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

# Display The Background
screen.blit(background, (0, 0))
pg.display.flip()

# Make Objects
board = genBoard(size)
playerOne = Player("gracz1")

# Main Loop
clock = pg.time.Clock()
going = True
while going:
    clock.tick(75)
    # Handle Input Events
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                playerOne.updateAccount()
                print(playerOne.gold)
        elif event.type == pg.MOUSEBUTTONDOWN:
            mousePos = pg.mouse.get_pos()
            mpx = int(mousePos[0] // (500 / size))
            mpy = int(mousePos[1] // (500 / size))
            playerOne.developCity(mpx, mpy)
            board[mpx][mpy].updatePop(1)
            # allsprites=pg.sprite.RenderPlain(board[mpx][mpy])
            # allsprites.update()
            screen.blit(board[mpx][mpy].image, (mpx * fieldSize, mpy * fieldSize))
            # allsprites.draw(screen)
            pg.display.flip()
            print(mpx, mpy)
            print(playerOne.Cities[0].gold)
pg.quit()
