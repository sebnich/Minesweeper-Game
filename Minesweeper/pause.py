import pygame


class Pause():

    def __init__(self):
        self.paused = pygame.mixer.music.get_busy()
        pygame.mixer.music.load('Minesweeper/assets/MorceauSymphonique.wav')
        pygame.mixer.music.set_volume(.1)
        pygame.mixer.music.play(-1)

    def toggle(self):
        if self.paused:
            pygame.mixer.music.unpause()
        if not self.paused:
            pygame.mixer.music.pause()
        self.paused = not self.paused