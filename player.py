import pygame

WIDTH, HEIGHT = 700, 700


class Player:
    def __init__(self):
        self.player = pygame.image.load("assets/player.png")
        self.rect = self.player.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2
        self.velx = 5
        self.vely = 5
        self.health = 3

    def moveUp(self):
        if self.rect.y > 0:
            self.rect.y -= self.vely

    def moveDown(self):
        if self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += self.vely

    def moveRight(self):
        if self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.velx

    def moveLeft(self):
        if self.rect.x > 0:
            self.rect.x -= self.velx

    def playerDie(self):
        self.rect.x = 5000  # move off the screen
        self.rect.y = 5000

    def playerReset(self):
        self.health = 3
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2
        self.velx = self.vely = 5
