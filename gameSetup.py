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
NO_FIELDS_PER_ROW = 10
SCREEN_SIZE = 500
FIELD_SIZE = int(SCREEN_SIZE / NO_FIELDS_PER_ROW)

# Initialize pygame
pg.init()
screen = pg.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pg.display.set_caption("mini-civ")
pg.mouse.set_visible(1)

# Create the background
background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

# Display the background
screen.blit(background, (0, 0))
pg.display.flip()

# Initialize objects
board = Board(NO_FIELDS_PER_ROW)
playerOne = Player("gracz1")