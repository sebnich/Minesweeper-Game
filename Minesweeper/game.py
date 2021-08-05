import pygame
from .constants import SQUARE_SIZE, WHITE, BLUE, GRAY
from Minesweeper.board import Board

class Game:
    def __init__(self, win, difficulty):
        self.win = win
        self.difficulty = difficulty
        self._init()
        

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def show_bombs_and_numbers(self, row, col):
        self.board.show_bombs_and_numbers(self.win, row, col)

    def _init(self):
        self.selected = None
        self.board = Board(self.difficulty)
        
    def reset(self):
        self._init()
    
    def select(self, row, col):
        square = self.board.get_square(row, col)
        if square.filled and not square.flag:
            self.selected = square
            if square.bomb:
                return False, (row, col)
            self.board.remove(row, col, True)
        elif not square.filled:
            if square.flagged_bombs == 0 and square.surrounding_flags == square.number:
                self.board.remove_surrounding_squares(row, col)
            elif square.surrounding_flags == square.number:
                bomb_select, (row_bomb, col_bomb) = self.board.remove_surrounding_squares(row, col)
                if not bomb_select:
                    return False, (row_bomb, col_bomb)
        return True, (row, col)
    
    def flag(self, row, col):
        square = self.board.get_square(row, col)
        if square.filled and square.flag:
            square.flag = False
            self.board.flags_left += 1
            self.board.subtract_all_flags(row, col)
            if square.bomb:
                self.board.bombs_left += 1
                self.board.add_correct_flags(row, col)
            return False
        elif square.filled and not self.board.flags_left == 0:
            square.add_flag()
            self.board.flags_left -= 1
            self.board.add_all_flags(row, col)
            if square.bomb:
                self.board.bombs_left -= 1
                self.board.subtract_correct_flags(row, col) # Iterate through surrounding squares and subtract 1 from flagged_bombs
                
            return True

    
    # def loser(self):
    #     WIN = pygame.display.set_mode((100, 100))
        

        


