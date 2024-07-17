import random
import pygame
import math

pygame.init()
# create a screen
screen = pygame.display.set_mode((880, 668))

# Title and icon
pygame.display.set_caption("Aatank hi Aatank")
icon = pygame.image.load('monster.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('background.jpg')

# Player Image
PlayerImg = pygame.image.load('me.png')
playerX = 418
playerY = 600
playerX_change = 0
playerY_change = 0

# Enemy Image
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 830))
    enemyY.append(random.randint(5, 50))
    enemyX_change.append(0.4)
    enemyY_change.append(0.4)

# Hammer
hammerImg = pygame.image.load('hamm.png')
hammerX = playerX
hammerY = playerY
hammerX_change = playerX_change
hammerY_change = playerY_change
hammer_state = "ready"

# Blood
bloodImg = pygame.image.load('blood.png')
bloodX = -150
bloodY = -150

# Game over
gameoverImg = pygame.image.load('gameover.png')
gameoverX = -1000
gameoverY = -1000

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 36)
textX = 15
textY = 15


# Player movement

def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (0, 255, 200))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(PlayerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y,))


def hammer(x, y):
    screen.blit(hammerImg, (x + 10, y + 15))


def blood(x, y):
    screen.blit(bloodImg, (x, y))


def gameover(x, y):
    screen.blit(gameoverImg, (x, y))


# Game loop
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (-60, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Key controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.6
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.6
            if event.key == pygame.K_UP:
                playerY_change = -0.4
                hammerY_change = -0.4
            if event.key == pygame.K_DOWN:
                playerY_change = 0.4
                hammerY_change = 0.4
            if event.key == pygame.K_SPACE:
                hammerX = playerX
                hammerY_change = -3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                hammerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
                hammerY_change = 0
    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 830:
        playerX = 830
    elif playerY <= 340:
        playerY = 340
        hammerY = playerY
        if pygame.K_SPACE:
            hammerX = playerX
            hammerY_change = -3
    elif playerY >= 600:
        playerY = 600
        hammerY = playerY
        if pygame.K_SPACE:
            hammerX = playerX
            hammerY_change = -3
    hammerX += hammerX_change
    if hammerY <= 0:
        hammerY = playerY
        hammerX = playerX_change
        hammerY_change = 0
    hammerY += hammerY_change

    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        enemyY[i] += enemyY_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.4
        elif enemyX[i] >= 820:
            enemyX_change[i] = -0.4
        elif enemyY[i] <= 5:
            enemyY_change[i] = 0.4
        elif enemyY[i] >= 600:
            enemyY_change[i] = -0.4

        if math.sqrt(math.pow((enemyX[i] - hammerX), 2) + math.pow((enemyY[i] - hammerY), 2)) <= 40:
            hammerX = playerX
            hammerY = playerY
            hammerY_change = 0
            bloodX = enemyX[i] - 30
            bloodY = enemyY[i]
            score_value += 1
            enemyX[i] = random.randint(0, 830)
            enemyY[i] = random.randint(5, 50)

        enemy(enemyX[i], enemyY[i], i)

        if math.sqrt(math.pow((enemyX[i] - playerX), 2) + math.pow((enemyY[i] - playerY), 2)) <= 50:
            hammerY_change = 0
            hammerX_change = 0
            enemyX_change[i] = 0
            enemyY_change[i] = 0
            playerY_change = 0
            playerX_change = 0
            gameoverX = 80
            gameoverY = 90

    blood(bloodX, bloodY)
    hammer(playerX, hammerY)
    player(playerX, playerY)
    enemy(enemyX[i], enemyY[i], i)
    gameover(gameoverX, gameoverY)
    show_score(textX, textY)
    pygame.display.update()
