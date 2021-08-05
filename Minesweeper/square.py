import pygame
from .constants import BLUE, CROSS, EXPLOSION, NUMBER_FONT, SQUARE_SIZE, BOMB, RED, BLACK, GRAY, FLAG


class Square():
    PADDING = 1
    OUTLINE = 2

    def __init__(self, row, col, bomb):
        self.row = row
        self.col = col
        self.bomb = bomb
        self.filled = True
        self.number = 0
        self.flag = False
        self.flagged_bombs = 0
        self.surrounding_flags = 0
        self.cross = False
    
        self.x, self.y = 0, 0
        self.calc_pos()
    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def unfill(self):
        self.filled = False

    
    def draw(self, win):
        
        outline_length = SQUARE_SIZE - (self.OUTLINE)
        padding_length = SQUARE_SIZE - ((self.PADDING+self.OUTLINE))

        x, y = self.col*SQUARE_SIZE, self.row*SQUARE_SIZE
        
        pygame.draw.rect(win, GRAY, (x + self.OUTLINE, y + self.OUTLINE, outline_length, outline_length))
        pygame.draw.rect(win, BLUE, (x + self.PADDING+ self.OUTLINE, y + self.PADDING+ self.OUTLINE, padding_length, padding_length))
        
    def draw_bomb(self, win):
        win.blit(BOMB, (self.x - BOMB.get_width()//2, self.y - BOMB.get_height()//2))
    
    def draw_flag(self, win):
        win.blit(FLAG, (self.x - FLAG.get_width()//2, self.y - FLAG.get_height()//2))
    
    def draw_explosion(self, win):
        win.blit(EXPLOSION, (self.x - EXPLOSION.get_width()//2, self.y - EXPLOSION.get_height()//2))
        
    def draw_number(self, win):
        text = NUMBER_FONT.render(str(self.number), True, BLACK)
        win.blit(text, (self.x - text.get_width()//2, self.y - text.get_height()//2))
    
    def draw_cross(self, win):
        win.blit(CROSS, (self.x - CROSS.get_width()//2, self.y - CROSS.get_height()//2))


    def addBombCount(self):
        if not self.bomb:
            self.flagged_bombs += 1
            self.number += 1
    
    def add_flag(self):
        self.flag = True


    
