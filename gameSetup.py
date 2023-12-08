import os
import pygame as pg

from Board import Board
from Player import Player

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

MAIN_DIR = os.path.split(os.path.abspath(__file__))[0]
DATA_DIR = os.path.join(MAIN_DIR, "data")
SIZE = 10
FIELD_SIZE = int(500 / SIZE)

# Initialize pygame
pg.init()
screen = pg.display.set_mode((700, 700))
pg.display.set_caption("miniCiv")
pg.mouse.set_visible(1)

# Create the background
background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

# Display the background
screen.blit(background, (0, 0))
pg.display.flip()

# Initialize objects
board = Board(SIZE)
playerOne = Player("gracz1")