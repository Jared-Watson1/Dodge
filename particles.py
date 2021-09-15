import pygame
import random

WIDTH, HEIGHT = 700, 700


class Particle:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.xvel = random.randrange(-10, 10)
        self.yvel = random.randrange(-10, 10)
        self.lifetime = 0
        self.number = number
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, window):
        self.lifetime += 1
        if self.lifetime < random.randint(5, self.number):
            self.x += self.xvel
            self.y += self.yvel
            pygame.draw.circle(window, self.color, (self.x, self.y), random.randint(1, 10))