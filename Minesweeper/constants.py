from typing import Collection
import pygame
from pygame.locals import *

pygame.init()

BORDER_WIDTH = 5
SCORE_WIDTH = 250
WIDTH, HEIGHT = 1000, 1000

ROWS, COLS = 10, 10
BOMB_NUM = 15
SQUARE_SIZE = WIDTH//COLS

# rgd
RED = (255, 0, 0)
ORANGE = (200, 100, 50)
YELLOW = (255, 255, 0)
GREEN = (0, 204, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
TRANS = (1, 1, 1)

### Images
BOMB = pygame.transform.scale(pygame.image.load(str(r'Minesweeper\assets\bomb.png')), (55, 55))
FLAG = pygame.transform.scale(pygame.image.load(str(r'Minesweeper\assets\flag.png')), (55, 55))
EXPLOSION = pygame.transform.scale(pygame.image.load(str(r'Minesweeper\assets\explosion.png')), (75, 75))
CROSS = pygame.transform.scale(pygame.image.load(str(r'Minesweeper\assets\cross.png')), (55, 55))
GO_BACK_ARROW = pygame.transform.scale(pygame.image.load(str(r'Minesweeper\assets\go_back_arrow.png')), (40, 40))

### Sounds
EXPLOSION_SOUND = pygame.mixer.Sound(str(r'Minesweeper\assets\explosion.wav'))
FLAG_DOWN_SOUND = pygame.mixer.Sound(str(r'Minesweeper\assets\flag_down.wav'))
FLAG_UP_SOUND = pygame.mixer.Sound(str(r'Minesweeper\assets\flag_up.wav'))
WINNING_SOUND = pygame.mixer.Sound(str(r'Minesweeper\assets\winning_sound.wav'))

pygame.init()
NUMBER_FONT = pygame.font.SysFont('arial', 50)
TEXT_FONT = pygame.font.SysFont('arial', 30)

LEFT = 1
RIGHT = 3