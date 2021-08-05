import time
import pygame
from .constants import BOMB_NUM, RED, SQUARE_SIZE, TEXT_FONT, WHITE, WIDTH, SCORE_WIDTH, HEIGHT, BLACK


class Score:
    def __init__(self, board):
        self.board = board
        self.startTime = time.time()
        self.endTime = 0
        
    def draw_score(self, win):
        score_label = '%s'%self.board.flags_left
        text = TEXT_FONT.render(str(score_label), True, BLACK)
        win.blit(text, (WIDTH + (SCORE_WIDTH//2) - (text.get_width()//2), 100))
    
        if self.board.BOMB_NUM == 69:
            text = TEXT_FONT.render(str("Nice..."), True, BLACK)
            win.blit(text, (WIDTH + (SCORE_WIDTH//2) - text.get_width()//2, 350))

        elif self.board.BOMB_NUM == 100:
            text = TEXT_FONT.render(str("Goodluck..."), True, BLACK)
            win.blit(text, (WIDTH + (SCORE_WIDTH//2) - text.get_width()//2, 350))
    
    def draw_running_timer(self, win):
        self.endTime = time.time() - self.startTime
        time_label = '%s'%int(time.time() - self.startTime)
        text = TEXT_FONT.render(str(time_label), True, BLACK)
        win.blit(text, (WIDTH + (SCORE_WIDTH//2) - (text.get_width()//2), 150))
    
    def draw_winning_screen(self, win):
        win_label = 'You won!'
        text = TEXT_FONT.render(str(win_label), True, BLACK)
        win.blit(text, (WIDTH + (SCORE_WIDTH//2) - text.get_width()//2, 100))

        time_label = 'in %s seconds'%int(self.endTime)
        text = TEXT_FONT.render(str(time_label), True, BLACK)
        win.blit(text, (WIDTH + (SCORE_WIDTH//2) - (text.get_width()//2), 150))




