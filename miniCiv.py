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
size=10
fieldSize=int(500/size)
class Field(pg.sprite.Sprite):
    def __init__(self, width, height, xPos, yPos, address):
        pg.sprite.Sprite.__init__(self)
        self.width=width
        self.height=height
        self.xPos=xPos
        self.yPos=yPos
        self.address=address
        self.image=pg.Surface([width-1,height-1])
        self.image.fill([126,126,126])
        self.rect=self.image.get_rect()
        self.food=randint(0, 9)
        self.gold=randint(0, 9)
        self.cult=randint(0, 9)
        print(width)
        self.owner=0 #0-no owner, 1-owner without city, 2-owner with city
        if pg.font:
            font = pg.font.Font(None, int(width/1.38))
            text = font.render(str(self.food), 0, [0, 255, 0])
            textpos = text.get_rect(centerx=6)
            self.image.blit(text, textpos)
            text = font.render(str(self.gold), 0, [255, 255, 0])
            textpos = text.get_rect(centerx=self.image.get_width()-8)
            self.image.blit(text, textpos)
            text = font.render(str(self.cult), 0, [255, 0, 0])
            textpos = text.get_rect(centery=self.image.get_height()-8)
            self.image.blit(text, textpos)
    def updatePop(self,pop):
        if pg.font:
            font = pg.font.Font(None, int(self.width/1.38)*2)
            text = font.render(str(pop), 0, [64, 64, 64])
            textpos = text.get_rect(centerx=int(self.image.get_width()/2), centery=int(self.image.get_height()/2))
            self.image.blit(text, textpos)
    def updateResources(self,nfood,ngold,ncult):
            print("updateRes")
class Player():
    def __init__(self, name):
        self.name=name
        self.Cities=[]
        self.gold=0
    def developCity(self,x,y):
        self.Cities.append(City(x,y))
    def updateAccount(self): # on nezt turn
        s=0
        for i in self.Cities:
            i.updateResources()
            s+=i.gold
        self.gold+=s
class City():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.pop=1
        self.food=0
        self.gold=0
        self.cult=0
        #print("gold",board[x][y].gold)
        self.firstField=board[x][y]
        #print(self.firstField)
        self.Fields=[board[x][y]]
    def getFoodIncome(self):
        s=0
        for i in self.Fields:
            s+=i.food
        return s
    def getGoldIncome(self):
        s=0
        for i in self.Fields:
            s+=i.gold
        return s
    def getCultIncome(self):
        s=0
        for i in self.Fields:
            s+=i.cult
        return s
    def updateResources(self): # on nezt turn
        #print("food inc:",self.getFoodIncome())
        #print(self.getGoldIncome())
        #print(self.getCultIncome())
        self.food+=self.getFoodIncome()
        self.gold+=self.getGoldIncome()
        self.cult+=self.getCultIncome()
        
    
# Generate And Draw Board With Fields
def genBoard(size):
    board=[]
    for j in range(0,size):
        row=[]
        for i in range(0,size):
            address=str(i)+str(j)
            field=Field(fieldSize,fieldSize,i*fieldSize,j*fieldSize,address)
            row.append(field)
            print(address)
            allsprites=pg.sprite.RenderPlain(field)
            allsprites.update()
            #allsprites.draw(screen,(i*fieldSize,j*fieldSize,fieldSize,fieldSize))
            screen.blit(field.image, (i*fieldSize, j*fieldSize))
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
board=genBoard(size)
playerOne=Player("gracz1")

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
            mousePos=pg.mouse.get_pos()
            mpx=int(mousePos[0]//(500/size))
            mpy=int(mousePos[1]//(500/size))
            playerOne.developCity(mpx,mpy)
            board[mpx][mpy].updatePop(1)
            #allsprites=pg.sprite.RenderPlain(board[mpx][mpy])
            #allsprites.update()
            screen.blit(board[mpx][mpy].image, (mpx*fieldSize, mpy*fieldSize))
            #allsprites.draw(screen)
            pg.display.flip()
            print(mpx,mpy)
            print(playerOne.Cities[0].gold)
pg.quit()
