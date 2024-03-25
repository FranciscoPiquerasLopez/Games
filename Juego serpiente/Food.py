import pygame
import random

class Food:
    def __init__(self, size, screen_width, screen_height):
        self.size = size
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pos = self.generate_position()

    def generate_position(self):
        x = random.randrange(0, self.screen_width - self.size, self.size)
        y = random.randrange(0, self.screen_height - self.size, self.size)
        return x, y

    def draw(self, screen):
        pygame.draw.rect(screen, "RED", (self.pos[0], self.pos[1], self.size, self.size))