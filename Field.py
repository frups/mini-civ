import pygame as pg
from random import randint


class Field(pg.sprite.Sprite):
    def __init__(self, width, height, x_pos, y_pos, address):
        pg.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.xPos = x_pos
        self.yPos = y_pos
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
            texts = text.get_rect(centerx=6)
            self.image.blit(text, texts)
            text = font.render(str(self.gold), 0, [255, 255, 0])
            texts = text.get_rect(centerx=self.image.get_width() - 8)
            self.image.blit(text, texts)
            text = font.render(str(self.cult), 0, [255, 0, 0])
            texts = text.get_rect(centery=self.image.get_height() - 8)
            self.image.blit(text, texts)

    def update_pop(self, pop):
        if pg.font:
            font = pg.font.Font(None, int(self.width / 1.38) * 2)
            text = font.render(str(pop), 0, [64, 64, 64])
            texts = text.get_rect(centerx=int(self.image.get_width() / 2), centery=int(self.image.get_height() / 2))
            self.image.blit(text, texts)

    def update_resources(self, nfood, ngold, ncult):
        print("updateRes")
