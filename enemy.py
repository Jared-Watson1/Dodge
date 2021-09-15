import pygame
import random

WIDTH, HEIGHT = 700, 700
FPS: int = 60


class Enemy:
    def __init__(self, player):
        self.player = player
        self.enemy = pygame.image.load("assets/enemy.png")
        self.rect = self.enemy.get_rect()
        spawnSide = random.randint(1, 4)
        if spawnSide == 1:  # top
            self.rect.x = random.randint(0, WIDTH)
            self.rect.y = 0 - self.rect.height
        elif spawnSide == 2:  # right
            self.rect.x = WIDTH + self.rect.width
            self.rect.y = random.randint(0, HEIGHT)
        elif spawnSide == 3:  # bottom
            self.rect.x = random.randint(0, WIDTH)
            self.rect.y = HEIGHT + self.rect.height
        elif spawnSide == 4:  # left
            self.rect.x = 0 - self.rect.width
            self.rect.y = random.randint(0, HEIGHT)

        playerX = player.rect.x
        playerY = player.rect.y
        enemyX = self.rect.x
        enemyY = self.rect.y

        self.velx = (playerX - enemyX) / FPS
        self.vely = (playerY - enemyY) / FPS

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
