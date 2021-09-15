import pygame
from button import Button
WIDTH, HEIGHT = 700, 700
SCORE_FONT = pygame.font.SysFont('comicsans', 40)
GAME_OVER_FONT = pygame.font.SysFont('comicsans', 100)
PLAY_AGAIN_FONT = pygame.font.SysFont('comicsans', 45)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RESET_VALUE = 300
pygame.font.init()


class Hud:
    def __init__(self, window):
        self.window = window
        self.color = (0, 255, 0)
        self.healthLength = RESET_VALUE
        self.increment = self.healthLength / 3
        self.score = 0

        with open("highscore.txt") as data:
            self.highscore = int(data.read())

    def drawHealthBar(self):
        pygame.draw.rect(self.window, self.color, (10, HEIGHT - 20, self.healthLength, 10))

    def loseHealth(self):
        self.healthLength -= self.increment

    def drawScore(self):
        scoreText = SCORE_FONT.render(f"Score: {self.score}", True, WHITE)
        self.window.blit(scoreText, (10, 10))

        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", 'w') as data:
                data.write(str(self.highscore))

        highscoreText = SCORE_FONT.render(f"High Score: {self.highscore}", True, WHITE)
        self.window.blit(highscoreText, (WIDTH - highscoreText.get_width() - 10, 10))

    def startScreen(self, position):
        startBtn = Button(BLACK, 0, 0, WIDTH, HEIGHT, text="Click anything to start!")
        startBtn.drawButton(self.window, 90, outline=WHITE)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if startBtn.isOver(position):
                    return True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def gameOver(self, position, player, bullets, enemiesList, powerUpsList):
        enemiesList.clear()
        powerUpsList.clear()
        gameOverBtn = Button(BLACK, 0, 0, WIDTH, HEIGHT, text="Game Over! Click anything to play again!")
        gameOverBtn.drawButton(self.window, 50)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if gameOverBtn.isOver(position):
                    player.playerReset()
                    self.score = 0
                    self.healthLength = RESET_VALUE
                    player.health = 3
                    bullets.clear()
                    return True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
