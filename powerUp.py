import pygame
import random

RESET_VALUE = 300


class PowerUp:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.healthCube = pygame.image.load('assets/health.png')
        self.width = self.height = int(self.healthCube.get_width() / 2) - 10
        self.healthCube = pygame.transform.scale(self.healthCube, (self.width, self.height))
        self.speedCube = pygame.image.load('assets/speed.png')
        self.speedCube = pygame.transform.scale(self.speedCube, (self.width - 2, self.height - 2))
        self.rect = self.healthCube.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.type = None

    def spawnCube(self, window):
        chanceHealth = random.randint(1, 5)
        chanceSpeed = random.randint(1, 5)
        if chanceHealth == 1:
            window.blit(self.healthCube, (self.x, self.y))
            self.type = 'health'
            return True
        elif chanceSpeed == 1:
            window.blit(self.speedCube, (self.x, self.y))
            self.type = 'speed'
            return True

    def drawCube(self, window):
        if self.type == 'health':
            window.blit(self.healthCube, (self.x, self.y))
        if self.type == 'speed':
            window.blit(self.speedCube, (self.x, self.y))

    def healthPowerUp(self, health, player):
        if health.healthLength < RESET_VALUE:
            health.healthLength += health.increment
            player.health += 1

    def speedPowerUp(self, player):
        if player.velx < 15:
            player.velx += 0.5
            player.vely += 0.5

