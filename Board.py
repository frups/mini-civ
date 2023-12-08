import pygame as pg

import gameSetup
from Field import Field


class Board():
    def __init__(self, size):
        self.size = size
        self.plane = []
        self.gen_board()

    # Generate And Draw Board With Fields
    def gen_board(self):
        print("generation")
        for j in range(0, self.size):
            print("row: " + str(j))
            row = []
            for i in range(0, self.size):
                print("cell:" + str(j) + "," + str(i))
                address = str(j) + str(i)
                field = Field(gameSetup.FIELD_SIZE, gameSetup.FIELD_SIZE, j * gameSetup.FIELD_SIZE,
                              i * gameSetup.FIELD_SIZE, address)
                row.append(field)
                print(address)
                allsprites = pg.sprite.RenderPlain(field)
                allsprites.update()
                # allsprites.draw(screen,(i*fieldSize,j*fieldSize,fieldSize,fieldSize))
                gameSetup.screen.blit(field.image, (j * gameSetup.FIELD_SIZE, i * gameSetup.FIELD_SIZE))
                pg.display.flip()
            self.plane.append(row)

    def get_field(self,x,y):
        if(len(self.plane)>=x and len(self.plane[0])>=y):
            return self.plane[x][y]