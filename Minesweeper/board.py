from Minesweeper.score import Score
import pygame
from .constants import BLACK, BOMB, BOMB_NUM, EXPLOSION, EXPLOSION_SOUND, GRAY, ROWS, COLS, SQUARE_SIZE, WHITE, WINNING_SOUND
from .square import Square
import random

class Board:
    def __init__(self, difficulty):
        self.winner = False
        if difficulty[0] == "EASY":
            self.ROWS = 10
            self.COLS = 10
            self.BOMB_NUM = difficulty[1]
        elif difficulty[0] == "MEDIUM":
            self.ROWS = 10
            self.COLS = 10
            self.BOMB_NUM = difficulty[1]
        elif difficulty[0] == "HARD":
            self.ROWS = 10
            self.COLS = 10
            self.BOMB_NUM = difficulty[1]
        elif difficulty[0] == "CUSTOM":
            self.ROWS = 10
            self.COLS = 10
            self.BOMB_NUM = difficulty[1]

        self.play_winning_sound = 0
        

        self.board = []
        self.flags_left = self.BOMB_NUM
        self.bombs_left = self.BOMB_NUM
        self.tiles_left = (self.ROWS * self.COLS) - self.BOMB_NUM
        self.bomb_locs = {}
        self.create_board()
        self.score = Score(self)
        
    def draw_squares(self, win):
        pass

    def get_surrounding_squares(self, row, col):
        # Store surrounding squares
        surrounding_squares = []
        if row > 0:
            surrounding_squares.append(self.board[row-1][col]) # Lower middle
            if col > 0:
                surrounding_squares.append(self.board[row-1][col-1]) # Lower left
            if col+1 < self.COLS:
                surrounding_squares.append(self.board[row-1][col+1]) # Lower right
        if row+1 < self.ROWS:
            surrounding_squares.append(self.board[row+1][col]) # Upper middle
            if col > 0:
                surrounding_squares.append(self.board[row+1][col-1]) # Upper left
            if col+1 < self.COLS:
                surrounding_squares.append(self.board[row+1][col+1]) # Upper right
        if col > 0:
            surrounding_squares.append(self.board[row][col-1]) # Center left
        if col+1 < self.COLS:
            surrounding_squares.append(self.board[row][col+1]) # Center right
        
        return surrounding_squares


    def create_bombs_locs(self):
        while len(self.bomb_locs) < self.BOMB_NUM:
            loc = random.randint(0, self.ROWS-1), random.randint(0, self.COLS-1)
            if loc not in self.bomb_locs:
                self.bomb_locs[loc] = 1
            

    def create_board(self):
        self.create_bombs_locs()
        bomb_bool = False
        for row in range(self.ROWS):
            for col in range(self.COLS):
                self.board.append([])

                loc = row, col
                if loc in self.bomb_locs.keys():
                    bomb_bool = True
                
                self.board[row].append(Square(row, col, bomb_bool))
                bomb_bool = False

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.board[row][col].bomb:
                    self.addPlusOneToAdjacentCells(row, col)
    
    def draw(self, win):
        self.draw_squares(win)
        if self.bombs_left == 0 and self.tiles_left == 0:
            if self.play_winning_sound == 0:
                WINNING_SOUND.play()
            self.play_winning_sound += 1
            self.score.draw_winning_screen(win)
            self.winner = True
        else:
            self.score.draw_running_timer(win)
            self.score.draw_score(win)
        for row in range(self.ROWS):
            for col in range(self.COLS):
                ### DRAW GRID LINES

                # Horizontal Lines
                x_1, y_1 = row*SQUARE_SIZE, col*SQUARE_SIZE 
                x_2, y_2 = (row+1)*SQUARE_SIZE, col*SQUARE_SIZE
                pygame.draw.lines(win, GRAY, False, [(x_1, y_1),(x_2, y_2)], width = 2)

                # Vertical Lines
                x_1, y_1 = row*SQUARE_SIZE, col*SQUARE_SIZE 
                x_2, y_2 = row*SQUARE_SIZE, (col+1)*SQUARE_SIZE
                pygame.draw.lines(win, GRAY, False, [(x_1, y_1),(x_2, y_2)], width = 2)
        
                square = self.board[row][col]
                if square.filled:
                    square.draw(win)
                    if square.flag:
                        square.draw_flag(win)
                else:
                    if square.bomb:
                        square.draw_bomb(win)
                    else:
                        square.draw_number(win)
                if square.cross:
                    square.draw_cross(win)
                        
        # Horizontal Lines
        x_1, y_1 = self.ROWS*SQUARE_SIZE, self.COLS*SQUARE_SIZE 
        x_2, y_2 = (self.ROWS+1)*SQUARE_SIZE, self.COLS*SQUARE_SIZE
        pygame.draw.lines(win, GRAY, False, [(self.ROWS*SQUARE_SIZE, 0),(self.ROWS*SQUARE_SIZE, self.COLS*SQUARE_SIZE)], width = 2)

        # Vertical Lines
        x_1, y_1 = row*SQUARE_SIZE, col*SQUARE_SIZE, 
        x_2, y_2 = row*SQUARE_SIZE, (col+1)*SQUARE_SIZE
        pygame.draw.lines(win, GRAY, False, [(0, self.COLS*SQUARE_SIZE),(self.ROWS*SQUARE_SIZE, self.COLS*SQUARE_SIZE)], width = 2)

    def show_bombs_and_numbers(self,win, r, c):
        square = self.board[r][c]
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.board[row][col].bomb and not self.board[row][col].flag:
                    self.board[row][col].unfill()
                elif not self.board[row][col].bomb and self.board[row][col].flag:
                    self.board[row][col].bomb = True
                    self.board[row][col].cross = True
                    self.board[row][col].unfill()
        
        self.draw(win)
        square.draw_explosion(win)
        EXPLOSION_SOUND.play()
        square.bomb = False
    
    def unfill(self, square):
        if square.filled == True:
            self.tiles_left -= 1
            square.unfill()

    def subtract_correct_flags(self, row, col):
        surrounding = self.get_surrounding_squares(row, col)
        for square in surrounding:
            square.flagged_bombs -= 1
    
    def add_correct_flags(self, row, col):
        surrounding = self.get_surrounding_squares(row, col)
        for square in surrounding:
            square.flagged_bombs += 1
    
    def subtract_all_flags(self, row, col):
        surrounding = self.get_surrounding_squares(row, col)
        for square in surrounding:
            square.surrounding_flags -= 1
    
    def add_all_flags(self, row, col):
        surrounding = self.get_surrounding_squares(row, col)
        for square in surrounding:
            square.surrounding_flags += 1

    def remove(self, row, col, from_click):
        if row < 0 or row > self.ROWS-1 or col < 0 or col > self.COLS-1:
            return True
        square = self.board[row][col]
        if square.bomb:
            return False
        if square.flag:
            return True
        if square.number != 0:
            self.unfill(square)
        elif from_click:
            self.remove_zeros(row, col)
        return True

    def remove_zeros(self, row, col):
        if row < 0 or row > self.ROWS-1 or col < 0 or col > self.COLS-1:
            return
        square = self.board[row][col]
        if square.flag:
            return

        if square.number == 0 and square.filled:
            self.unfill(square)
            self.remove_zeros(row+1, col-1)
            self.remove_zeros(row+1, col)
            self.remove_zeros(row+1, col+1)
            self.remove_zeros(row, col+1)
            self.remove_zeros(row-1, col+1)
            self.remove_zeros(row-1, col)
            self.remove_zeros(row-1, col-1)
            self.remove_zeros(row, col-1)
            return
        
        self.unfill(square)
        return
    
    def remove_surrounding_squares(self, row, col):
        failed_squares = [[0,0]]

        if not self.remove(row+1, col-1, True): failed_squares.append([row+1, col-1])
        if not self.remove(row+1, col, True): failed_squares.append([row+1,col])
        if not self.remove(row+1, col+1, True): failed_squares.append([row+1,col+1])
        if not self.remove(row, col+1, True): failed_squares.append([row,col+1])
        if not self.remove(row-1, col+1, True): failed_squares.append([row-1,col+1])
        if not self.remove(row-1, col, True): failed_squares.append([row-1,col])
        if not self.remove(row-1, col-1, True): failed_squares.append([row-1,col-1])
        if not self.remove(row, col-1, True): failed_squares.append([row,col-1])

        if len(failed_squares) > 1:
            return False, (failed_squares[1][0], failed_squares[1][1])
            # if self.board[failed_squares[1][0]][failed_squares[1][1]].flag:
                
            # else:
            #     return False, (failed_squares[2][0], failed_squares[2][1])
        return True, (failed_squares[0][0], failed_squares[0][1])
    
    def get_square(self, row, col):
        return self.board[row][col]
    
    def addPlusOneToAdjacentCells(self, row, col):
        surrounding = self.get_surrounding_squares(row, col)
        for square in surrounding:
            square.addBombCount()

