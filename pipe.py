import pygame

class Pipe(pygame.Rect):
    def __init__(self, *args, **kwargs):
        self.speed = 5
        super().__init__(*args, **kwargs)

    def move(self, board_width):
        self.x -= self.speed
