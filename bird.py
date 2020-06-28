import pygame

class Bird(pygame.Rect):
    def __init__(self, jump_key, *args, **kwargs):

        self.angle = 0
        self.max_speed = 15
        self.speed = self.max_speed
        self.jump_key = jump_key
        super().__init__(*args, **kwargs)

    def move(self, board_height):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.jump_key] and self.speed < 5:
            self.speed = self.max_speed

        if self.y - self.speed > 0 and self.y - self.speed < (board_height - board_height/10):
            self.y -= self.speed

        if self.speed >= -9:
            self.speed -= 1

        self.angle = (self.speed - (-10)) * (45 - (-90)) / (10 - (-10)) + (-90)
