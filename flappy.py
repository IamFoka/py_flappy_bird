import sys, pygame
import loguru
import random

from bird import Bird
from pipe import Pipe

black = 0, 0, 0
white = 255, 255, 255

class Flappy:


    def __init__(self):
        pygame.init()

        self.size = self.width, self.height = 400, 545
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.tick_counter = 0

        self.bird_img = pygame.image.load("img/bluebird-downflap.png")
        self.pipe_img = pygame.image.load("img\pipe-red.png")
        self.birdrect = self.bird_img.get_rect()

        self.pipes = []

        self.start_game()

    def create_bird(self):
            self.bird = Bird(pygame.K_UP,
                self.width / 5,
                self.height / 2,
                self.bird_img.get_width(),
                self.bird_img.get_height())

    def move_bird(self):
        self.bird.move(self.height)

    def draw_bird(self):
        rotated_bird_img = pygame.transform.rotate(self.bird_img, self.bird.angle)
        self.screen.blit(rotated_bird_img, self.bird)

    def create_pipe(self):
        offsetCanos = 225
        y_random = random.randrange(-(self.pipe_img.get_height()/2) + offsetCanos + 30, (self.height - self.pipe_img.get_height()/2) - offsetCanos -30)
        y_top_pipe = y_random - offsetCanos
        y_bottom_pipe = y_random + offsetCanos

        print(f'y_random:{y_random}')
        print(f'y_top_pipe:{y_top_pipe}')
        print(f'y_bottom_pipe:{y_bottom_pipe}')
        print(f'tamanho da pipe = {self.pipe_img.get_height()}')

        top_pipe = Pipe(self.width - self.width/10,
            y_top_pipe,
            self.pipe_img.get_width(),
            self.pipe_img.get_height())

        bottom_pipe = Pipe(self.width - self.width/10,
            y_bottom_pipe,
            self.pipe_img.get_width(),
            self.pipe_img.get_height())

        self.pipes.append({
            "top_pipe": top_pipe,
            "bottom_pipe": bottom_pipe,
        })

    def move_pipes(self):
        for pipe_pair in self.pipes:
            pipe_pair["top_pipe"].move(self.width)
            pipe_pair["bottom_pipe"].move(self.width)

    def draw_pipes(self):
        for pipe_pair in self.pipes:
            rotated_pipe_img = pygame.transform.rotate(self.pipe_img, 180)
            self.screen.blit(rotated_pipe_img, pipe_pair["top_pipe"])
            self.screen.blit(self.pipe_img, pipe_pair["bottom_pipe"])


    def game_loop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            if self.tick_counter == 60:
                self.tick_counter = 0
                self.create_pipe()

            self.tick_counter += 1

            self.move_bird()
            self.move_pipes()

            self.screen.fill(white)
            self.draw_bird()
            self.draw_pipes()

            pygame.display.flip()
            self.clock.tick(60)

    def start_game(self):
        self.create_pipe()

        self.create_bird()






if __name__ == "__main__":
    flappy = Flappy()
    flappy.game_loop()
