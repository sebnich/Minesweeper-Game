
import pygame, math, sys
from .constants import BLACK, GRAY, ORANGE, TRANS, WHITE

class Slider():
    def __init__(self, name, win, val, maxi, mini, pos, dim):
        self.win = win
        self.val = val  # start value
        self.maxi = maxi  # maximum at slider position right
        self.mini = mini  # minimum at slider position left
        self.xpos = pos[0]  # x-location on screen
        self.ypos = pos[1]
        self.width = dim[0]
        self.height = dim[1]
        self.surf = pygame.surface.Surface((self.width, self.height))
        self.hit = False  # the hit attribute indicates slider movement due to mouse interaction

        font = pygame.font.SysFont("Verdana", 12)
        self.txt_surf = font.render(name, 1, BLACK)
        self.txt_rect = self.txt_surf.get_rect(center=(50, 15))

        # Static graphics - slider background #
        self.surf.fill((100, 100, 100))
        pygame.draw.rect(self.surf, GRAY, [0, 0, self.width, self.height], 3)
        # pygame.draw.rect(self.surf, ORANGE, [10, 10, 80, 10], 0)
        pygame.draw.rect(self.surf, WHITE, [int(self.width*.1), self.height//2-2.5, int(self.width-(2*self.width*.1)), 5], 0)

        self.surf.blit(self.txt_surf, self.txt_rect)  # this surface never changes

        # dynamic graphics - button surface #
        self.button_surf = pygame.surface.Surface((20, 20))
        self.button_surf.fill(TRANS)
        self.button_surf.set_colorkey(TRANS)
        pygame.draw.circle(self.button_surf, BLACK, (10, 10), 6, 0)
        pygame.draw.circle(self.button_surf, ORANGE, (10, 10), 4, 0)

    def draw(self):
        """ Combination of static and dynamic graphics in a copy of
    the basic slide surface
    """
        # static
        surf = self.surf.copy()

        # dynamic
        pos = (int(self.width*.1)+int((self.val-self.mini)/(self.maxi-self.mini)*int(self.width-(2*self.width*.1))), (self.height//2 - 2.5)+3)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.xpos, self.ypos)  # move of button box to correct screen position

        # screen
        self.win.blit(surf, (self.xpos, self.ypos))

    def move(self):
        """
    The dynamic part; reacts to movement of the slider button.
    """
        self.val = (pygame.mouse.get_pos()[0] - self.xpos - int(self.width*.1)) / int(self.width-(2*self.width*.1)) * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi

# window = pygame.display.set_mode((1000,1000))
# window.fill(WHITE)
# s = Slider("Yes", window, 100, 100, 50, 50)
# clock = pygame.time.Clock()
# FPS = 60
# run = True
# while run:
#     click = False
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#         elif event.type == KEYDOWN:
#             if event.key == K_ESCAPE:
#                 pygame.quit()
#         elif event.type == MOUSEBUTTONDOWN:
#             pos = pygame.mouse.get_pos()
#             if event.button == LEFT:
#                 click = True
#             if s.button_rect.collidepoint(pos):
#                 s.hit = True
#         elif event.type == pygame.MOUSEBUTTONUP:
#                 s.hit = False
    
#     window.fill(BLACK)
#     if s.hit:
#         s.move()
#     s.draw()

#     pygame.display.update()
#     clock.tick(FPS)