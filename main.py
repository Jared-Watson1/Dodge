import pygame
import random
from player import Player
from enemy import Enemy
from particles import Particle
from bullet import Bullet
from powerUp import PowerUp
pygame.font.init()
from hud import Hud

WIDTH, HEIGHT = 700, 700
DIMENSION = (WIDTH, HEIGHT)
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
AMMO = 5
NUMBER = 200
dead = False
EXPLOSION = pygame.mixer.Sound("assets/explosion.mp3")

window = pygame.display.set_mode(DIMENSION)
pygame.display.set_caption("Dodge!")

clock = pygame.time.Clock()
player = Player()
hud = Hud(window)
enemySpawnerTimer = 1
particles = []
gameRunning = True
gameStart = False


def draw(user, enemiesList, bullets, powerUps):
    global AMMO, gameStart, enemySpawnerTimer, dead
    window.fill(BLACK)
    position = pygame.mouse.get_pos()
    if gameStart:  # game loop
        window.blit(user.player, (user.rect.x, user.rect.y))
        hud.drawHealthBar()
        hud.drawScore()
        for enemy in enemiesList:
            window.blit(enemy.enemy, (enemy.rect.x, enemy.rect.y))
        for particle in particles:
            particle.draw(window)
        for bullet in bullets:
            pygame.draw.circle(window, (255, 0, 0), (bullet.rect.x, bullet.rect.y), 5)
        for powerUp in powerUps:
            powerUp.drawCube(window)
    else:  # start screen
        hud.startScreen(position)
        if hud.startScreen(position):
            gameStart = True
    if dead:  # display play again screen
        hud.gameOver(position, player, bullets, enemiesList, powerUps)
        if hud.gameOver(position, player, bullets, enemiesList, powerUps):
            AMMO, enemySpawnerTimer = 5, 1
            dead = False

    pygame.display.update()


def playerMove(user, keys):
    if keys[pygame.K_a]:
        user.moveLeft()
    if keys[pygame.K_d]:
        user.moveRight()
    if keys[pygame.K_w]:
        user.moveUp()
    if keys[pygame.K_s]:
        user.moveDown()


def shoot(event, bulletsList):
    if len(bulletsList) < AMMO:
        if event.key == pygame.K_UP:
            newBullet = Bullet(player)
            newBullet.shootUp()
            bulletsList.append(newBullet)
        elif event.key == pygame.K_DOWN:
            newBullet = Bullet(player)
            newBullet.shootDown()
            bulletsList.append(newBullet)
        elif event.key == pygame.K_LEFT:
            newBullet = Bullet(player)
            newBullet.shootLeft()
            bulletsList.append(newBullet)
        elif event.key == pygame.K_RIGHT:
            newBullet = Bullet(player)
            newBullet.shootRight()
            bulletsList.append(newBullet)


def handleEnemy(user, enemyList, score):
    global enemySpawnerTimer, NUMBER
    if enemySpawnerTimer == 0:
        enemy = Enemy(user)
        enemyList.append(enemy)
        enemySpawnerTimer = random.randint(30, NUMBER)
    else:
        enemySpawnerTimer -= 1
    if score % 10 == 0 and NUMBER > 50:
        NUMBER -= 15
    for enemy in enemyList:
        enemy.update()


def handleBullets(bullets):
    for bullet in bullets:
        bullet.update()
        if bullet.rect.x < 0 or bullet.rect.x > WIDTH or bullet.rect.y < 0 or bullet.rect.y > HEIGHT:
            bullets.remove(bullet)


def checkCollision(entity1, entity2):
    global gameRunning
    entity2x = entity2.rect.x
    entity2y = entity2.rect.y
    entity1x = entity1.rect.x
    entity1y = entity1.rect.y
    if entity2x < entity1x + entity1.rect.width and entity2x + entity2.rect.width > entity1x and entity2y < entity1y + \
            entity1.rect.height and entity2y + entity2.rect.height > entity1y:  # collision detected
        return True


def playerEnemyCollision(enemiesList, enemy):
    enemiesList.remove(enemy)
    player.health -= 1
    hud.loseHealth()
    EXPLOSION.play()
    for x in range(50):
        particles.append(Particle(enemy.rect.x, enemy.rect.y, 100))


def bulletEnemyCollision(enemiesList, enemy, powerUpsList, bulletsList, bullet):
    hud.score += 1
    EXPLOSION.play()
    powerUp = PowerUp(enemy.rect.x, enemy.rect.y)
    if powerUp.spawnCube(window):
        powerUp.spawnCube(window)
        powerUpsList.append(powerUp)
    try:
        enemiesList.remove(enemy)
        bulletsList.remove(bullet)
    except ValueError:
        bulletsList.remove(bullet)
    for x in range(10):
        particles.append(Particle(enemy.rect.x, enemy.rect.y, 50))


def checkIfDie():
    global AMMO, dead
    if player.health <= 0:
        AMMO = 0
        player.playerDie()
        dead = True


def main():
    global AMMO, gameStart
    bullets = []
    enemies = []
    powerUps = []
    while gameRunning:
        clock.tick(FPS)
        keysPressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if gameStart:
                if event.type == pygame.KEYDOWN:
                    shoot(event, bullets)

        if gameStart:
            playerMove(player, keysPressed)
            handleBullets(bullets)
            if not dead:
                handleEnemy(player, enemies, hud.score)
                for enemy in enemies:
                    if checkCollision(player, enemy):
                        playerEnemyCollision(enemies, enemy)
                    for bullet in bullets:
                        if checkCollision(enemy, bullet):
                            bulletEnemyCollision(enemies, enemy, powerUps, bullets, bullet)
                for powerUp in powerUps:
                    if checkCollision(player, powerUp):
                        if powerUp.type == 'health':
                            powerUp.healthPowerUp(hud, player)
                        elif powerUp.type == 'speed':
                            powerUp.speedPowerUp(player)
                        powerUps.remove(powerUp)
            checkIfDie()
        draw(player, enemies, bullets, powerUps)


if __name__ == '__main__':
    main()
