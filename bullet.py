import pygame

FPS = 60
WIDTH, HEIGHT = 700, 700
pygame.init()


class Bullet:
    def __init__(self, user):
        self.user = user
        # self.xFinal = xFinal
        # self.yFinal = yFinal
        self.image = pygame.Surface((4, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = user.rect.x + (user.rect.width // 2)
        self.rect.y = user.rect.y + (user.rect.height // 2)
        self.ammo = 5
        self.velx = 0
        self.vely = 0
        self.sound = pygame.mixer.Sound("assets/laser.mp3")

        # self.velx = ((self.xFinal - self.rect.x) / FPS) + self.velocity  --> If you want to aim with your mouse
        # self.vely = ((self.yFinal - self.rect.y) / FPS) + self.velocity

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

    def shootLeft(self):
        self.velx = -20
        self.vely = 0
        self.sound.play()

    def shootRight(self):
        self.velx = 20
        self.vely = 0
        self.sound.play()

    def shootUp(self):
        self.velx = 0
        self.vely = -20
        self.sound.play()

    def shootDown(self):
        self.velx = 0
        self.vely = 20
        self.sound.play()


