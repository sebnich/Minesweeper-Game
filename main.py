from Minesweeper.pause import Pause
from types import WrapperDescriptorType
from typing import MutableMapping

from pygame import constants
from Minesweeper.score import Score
import pygame
from pygame import draw
from pygame.constants import KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN, QUIT, RESIZABLE
from Minesweeper.constants import BLACK, BLUE, FLAG_DOWN_SOUND, FLAG_UP_SOUND, GO_BACK_ARROW, GREEN, LEFT, RED, RIGHT, SCORE_WIDTH, SQUARE_SIZE, TEXT_FONT, WHITE, WIDTH, HEIGHT, YELLOW
from Minesweeper.game import Game
import time
from Minesweeper.slider import Slider

FPS = 60
pygame.init()

WIN = pygame.display.set_mode((WIDTH+SCORE_WIDTH, HEIGHT), RESIZABLE)
WIN.fill(WHITE)
pygame.display.set_caption('Minesweeper')

# Music
PAUSE = Pause()

MUSIC = True
SOUND = True

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def draw_text_on_button(text, font, color, surface, button):
    x = button.x + button.w//2
    y = button.y + button.h//2
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main_menu():
    run = True
    clock = pygame.time.Clock()
    click = False

    while run:
        
        FULL_WIDTH = WIDTH + SCORE_WIDTH
        WIN.fill(WHITE)
        pygame.draw.rect(WIN, BLACK, (0, 0, FULL_WIDTH, HEIGHT))
        pygame.draw.rect(WIN, WHITE, (10, 10, FULL_WIDTH-20, HEIGHT-20))

        clock.tick(FPS)
        titleText = pygame.font.SysFont("arial",75)
        draw_text('Minesweeper!', titleText, BLACK, WIN, FULL_WIDTH//2, HEIGHT//2 - 100)

        mx, my = pygame.mouse.get_pos()
 
        new_game_button = pygame.Rect(FULL_WIDTH//2 - 100, HEIGHT//2 - 25, 200, 50)
        options_button = pygame.Rect(FULL_WIDTH//2 - 100, HEIGHT//2 + 35, 200, 50)

        if new_game_button.collidepoint((mx, my)):
            if click:
                choose_difficulty()
        
        if options_button.collidepoint((mx, my)):
            if click:
                options()

        pygame.draw.rect(WIN, RED, new_game_button)
        pygame.draw.rect(WIN, RED, options_button)

        smallText = pygame.font.SysFont("arial",20)
        draw_text_on_button('New Game',smallText, BLACK, WIN, new_game_button)
        draw_text_on_button('Options',smallText, BLACK, WIN, options_button)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == LEFT:
                    click = True
 
        pygame.display.update()
        clock.tick(60)

def options():
    run = True
    clock = pygame.time.Clock()
    click = False
    global MUSIC
    global SOUND

    while run:
        
        FULL_WIDTH = WIDTH + SCORE_WIDTH
        WIN.fill(WHITE)
        pygame.draw.rect(WIN, BLACK, (0, 0, FULL_WIDTH, HEIGHT))
        pygame.draw.rect(WIN, WHITE, (10, 10, FULL_WIDTH-20, HEIGHT-20))

        clock.tick(FPS)
        titleText = pygame.font.SysFont("arial",60)
        draw_text('Music or Nah', titleText, BLACK, WIN, FULL_WIDTH//2, HEIGHT//2 - 100)

        mx, my = pygame.mouse.get_pos()
 
        music_toggle = pygame.Rect(FULL_WIDTH//2 + 40, HEIGHT//2 - 25, 30, 30)
        game_sound_toggle = pygame.Rect(FULL_WIDTH//2 + 40, HEIGHT//2 + 35, 30, 30)
        back_button = pygame.Rect(40, 40, 50, 50)
        WIN.blit(GO_BACK_ARROW, (back_button.x, back_button.y))

        pygame.draw.rect(WIN, BLACK, music_toggle)
        pygame.draw.rect(WIN, BLACK, game_sound_toggle)

        d = 3
        pygame.draw.rect(WIN, WHITE, (music_toggle.x+d, music_toggle.y+d, \
            music_toggle.width-(2*d), music_toggle.height-(2*d)))
        pygame.draw.rect(WIN, WHITE, (game_sound_toggle.x+d, game_sound_toggle.y+d, \
            game_sound_toggle.width-(2*d), game_sound_toggle.height-(2*d)))

        if music_toggle.collidepoint((mx, my)):
            if click:
                MUSIC = not MUSIC
                PAUSE.toggle()          
        
        if game_sound_toggle.collidepoint((mx, my)):
            if click:
                SOUND = not SOUND
        
        if back_button.collidepoint((mx, my)):
            if click:
                main_menu()

        smallText = pygame.font.SysFont("arial",20)
        if MUSIC:
            pygame.draw.rect(WIN, WHITE, (music_toggle.x+d, music_toggle.y+d, \
            music_toggle.width-(2*d), music_toggle.height-(2*d)))
        else:
            draw_text('X',smallText, BLACK, WIN, music_toggle.x+music_toggle.w//2, music_toggle.y+music_toggle.h//2)
            draw_text("Oh you don't like my trombone playing? That's fine...",smallText, BLACK, WIN, music_toggle.x, music_toggle.y+music_toggle.h//2+ 150)
        if SOUND:
            pygame.draw.rect(WIN, WHITE, (game_sound_toggle.x+d, game_sound_toggle.y+d, \
            game_sound_toggle.width-(2*d), game_sound_toggle.height-(2*d)))
        else:
            draw_text('X',smallText, BLACK, WIN, game_sound_toggle.x+game_sound_toggle.w//2, game_sound_toggle.y+game_sound_toggle.h//2)

        
        draw_text('Music',smallText, BLACK, WIN, FULL_WIDTH//2, HEIGHT//2 - 10)
        draw_text('Sound',smallText, BLACK, WIN, FULL_WIDTH//2, HEIGHT//2 + 50)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == LEFT:
                    click = True
 
        pygame.display.update()
        clock.tick(60)

        
def choose_difficulty():
    run = True
    clock = pygame.time.Clock()
    click = False
    custom_slider = Slider("", WIN, 0, 100, 0, [WIDTH//2 - 150, HEIGHT//2 + 120], [300, 30])

    while run:
        
        pygame.draw.rect(WIN, BLACK, (0, 0, WIDTH, HEIGHT))
        pygame.draw.rect(WIN, WHITE, (10, 10, WIDTH-20, HEIGHT-20))

        ### SCORE BOARD
        pygame.draw.rect(WIN, BLACK, (WIDTH+10, 0, SCORE_WIDTH - 20, HEIGHT))
        pygame.draw.rect(WIN, WHITE, (WIDTH+20, 10, SCORE_WIDTH - 40, HEIGHT - 20))
        draw_text('Minesweeper',TEXT_FONT,BLACK,WIN, WIDTH + (SCORE_WIDTH//2), 50)

        clock.tick(FPS)
        titleText = pygame.font.SysFont("arial",45)
        draw_text('Choose Difficulty', titleText, BLACK, WIN, WIDTH//2, HEIGHT//2 - 200)

        mx, my = pygame.mouse.get_pos()
 
        easy_button = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 - 145, 300, 50)
        medium_button = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 - 85, 300, 50)
        hard_button = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 - 25, 300, 50)
        custom_button = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 + 60, 300, 50)

        back_button = pygame.Rect(40, 40, 50, 50)
        WIN.blit(GO_BACK_ARROW, (back_button.x, back_button.y))

        if easy_button.collidepoint((mx, my)):
            if click:
                game(["EASY",10])
        if medium_button.collidepoint((mx, my)):
            if click:
                game(["MEDIUM",20])
        if hard_button.collidepoint((mx, my)):
            if click:
                game(["HARD",30])
        if custom_button.collidepoint((mx, my)):
            if click:
                game(["CUSTOM",int(custom_slider.val)])
        if back_button.collidepoint((mx, my)):
            if click:
                main_menu()

        pygame.draw.rect(WIN, GREEN, easy_button)
        pygame.draw.rect(WIN, YELLOW, medium_button)
        pygame.draw.rect(WIN, RED, hard_button)
        pygame.draw.rect(WIN, (0, 100, 255), custom_button)
        
        smallText = pygame.font.SysFont("arial",20)
        draw_text_on_button('Easy --> 10x10 : 10 Mines',smallText, BLACK, WIN, easy_button)
        draw_text_on_button('Normal --> 10x10 : 20 Mines ',smallText, BLACK, WIN, medium_button)
        draw_text_on_button('Hard --> 10x10 : 30 Mines',smallText, BLACK, WIN, hard_button)
        draw_text_on_button('Custom --> 10x10 : %s Mines'%int(custom_slider.val),smallText, BLACK, WIN, custom_button)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == LEFT:
                    click = True
                pos = pygame.mouse.get_pos()
                if custom_slider.button_rect.collidepoint(pos):
                    custom_slider.hit = True
            elif event.type == pygame.MOUSEBUTTONUP:
                custom_slider.hit = False

        if custom_slider.hit:
            custom_slider.move()
        custom_slider.draw()
 
        pygame.display.update()
        clock.tick(FPS)

def game(difficulty):
    
    run = True
    clock = pygame.time.Clock()
    minesweeper_game = Game(WIN, difficulty)
    click = False

    while run:
        WIN.fill(WHITE)
        clock.tick(FPS)

        ### SCORE BOARD
        pygame.draw.rect(WIN, BLACK, (WIDTH+10, 0, SCORE_WIDTH - 20, HEIGHT))
        pygame.draw.rect(WIN, WHITE, (WIDTH+20, 10, SCORE_WIDTH - 40, HEIGHT - 20))

        draw_text('Minesweeper',TEXT_FONT,BLACK,WIN, WIDTH + (SCORE_WIDTH//2), 50)

        mx, my = pygame.mouse.get_pos()

        smallText = pygame.font.SysFont("arial",20)
        button_1 = pygame.Rect(WIDTH + (SCORE_WIDTH//2) - 100, 200, 200, 50)
        button_2 = pygame.Rect(WIDTH + (SCORE_WIDTH//2) - 100, 260, 200, 50)
        
        if button_1.collidepoint((mx, my)):
            if click:
                game(difficulty)
        if button_2.collidepoint((mx, my)):
            if click:
                main_menu()

        pygame.draw.rect(WIN, RED, button_1)
        pygame.draw.rect(WIN, RED, button_2)

        draw_text('Restart',smallText, BLACK, WIN, button_1.x + button_1.w//2, button_1.y + button_1.h//2)
        draw_text('Main Menu',smallText, BLACK, WIN, button_2.x + button_2.w//2, button_2.y + button_2.h//2)
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)

                if minesweeper_game.board.winner:
                    pass
                elif pos[0] < WIDTH:
                    [bomb_select, (row_bomb, col_bomb)] = minesweeper_game.select(row, col)
                    if not bomb_select:
                        minesweeper_game.show_bombs_and_numbers(row_bomb, col_bomb)
                        losing_screen(difficulty)
                click = True
                
                # elif minsweeper_game.winner():
                    
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if minesweeper_game.board.winner:
                    pass
                elif pos[0] < WIDTH:
                    if minesweeper_game.flag(row, col) and SOUND:
                        FLAG_DOWN_SOUND.play()
                    elif SOUND:
                        FLAG_UP_SOUND.play()
                    
                click = True
            
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    run = False

        minesweeper_game.update()

    pygame.quit()
    exit()

def losing_screen(difficulty):
    # WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, (WIDTH+10, 0, SCORE_WIDTH - 20, HEIGHT))
    pygame.draw.rect(WIN, WHITE, (WIDTH+20, 10, SCORE_WIDTH - 40, HEIGHT - 20))
    run = True
    clock = pygame.time.Clock()

    while run:

        clock.tick(FPS)
        draw_text('You lost...', TEXT_FONT, BLACK, WIN, WIDTH+SCORE_WIDTH//2, HEIGHT//2 - 100)

        mx, my = pygame.mouse.get_pos()
 
        play_again_button = pygame.Rect(WIDTH+SCORE_WIDTH//2 - 100, HEIGHT//2 - 25, 200, 50)
        change_difficulty_button = pygame.Rect(WIDTH+SCORE_WIDTH//2 - 100, HEIGHT//2 + 35, 200, 50)

        if play_again_button.collidepoint((mx, my)):
            if click:
                game(difficulty)
        if change_difficulty_button.collidepoint((mx, my)):
            if click:
                choose_difficulty()

        pygame.draw.rect(WIN, RED, play_again_button)
        pygame.draw.rect(WIN, RED, change_difficulty_button)

        smallText = pygame.font.SysFont("arial",20)
        draw_text_on_button('Play again?',smallText, BLACK, WIN, play_again_button)
        draw_text_on_button('Change difficulty?',smallText, BLACK, WIN, change_difficulty_button)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == LEFT:
                    click = True
 
        pygame.display.update()
        clock.tick(60)
        

main_menu()


