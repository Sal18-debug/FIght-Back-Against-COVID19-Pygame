
import pygame
import random
import math
from pygame import mixer

# initiate
pygame.init()

# create screen
screen = pygame.display.set_mode((720, 450))

# background
background = pygame.image.load("background.png")

#misc
score = 0
font = pygame.font.Font('GillSansMTBold.ttf', 32)

scoreX = 12
scoreY = 12


def showScore(x, y):
    theScore = font.render("Score: " + str(score), True, (50, 162, 225))
    screen.blit(theScore, (x, y))


#game over
gameOver = pygame.image.load("gameOver.png")

#success
success = pygame.image.load('success.png')

#lives
lives = 3


def showLives(x, y):
    theLives = font.render("Lives: " + str(lives), True, (50, 162, 225))
    screen.blit(theLives, (x, y))


# character
charX = 350
charY = 592
charXchange = 5
charYchange = 5

charIdleFront = pygame.image.load("character/characterIdleFront.png")

left = False
right = False
front = False
back = False

direction = ""

#virus
virusImg = []
virusXchange = []
virusYchange = []
virusX = []
virusY = []
numVirus = 4

for v in range(numVirus):
    virusImg.append(pygame.image.load('virus.png'))
    virusX.append(random.randint(0, 600))
    virusY.append(random.randint(0, 250))
    virusXchange.append(random.randint(1,3))
    virusYchange.append(random.randint(1,3))

nbrVirus = 0

# functions
def redrawGameWindow():
    global walkCount
    global direction
    global virusImg
    global nbrVirus
    global virusX
    global virusY
    global lives
    global live1
    global live2
    global live3

    screen.blit(background, (0, 0))
    screen.blit(charIdleFront, (charX, charY))

    for v in range(numVirus):
        virus(virusX[v], virusY[v], v)

    showScore(scoreX, scoreY)

    showLives(580, 8)

    pygame.display.update()


def virus(x, y, v):
    screen.blit(virusImg[v], (x, y))

def isCollision(x, y, vaccineX, vaccineY):
    distance = math.sqrt((math.pow(x - vaccineX, 2)) +
                         (math.pow(y - vaccineY, 2)))
    if distance < 27:
        return True

def showGameOver():
    screen.blit(gameOver, (0, 0))
    pygame.display.update()


def showSuccess():
    screen.blit(success, (0, 0))
    pygame.display.update()


#screens
running = True
lives = 3

while running:

    for event in pygame.event.get():
        #quit
        if event.type == pygame.QUIT:
            running = False

        #keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                charYchange = -5
            if event.key == pygame.K_DOWN:
                charYchange = 5
            if event.key == pygame.K_LEFT:
                charXchange = -5
            if event.key == pygame.K_RIGHT:
                charXchange = 5
        else:
            charXchange = 0
            charYchange = 0

    #collision
    for v in range(numVirus):
        virusY[v] += virusYchange[v]
        if virusY[v] <= 0:
            virusYchange[v] = - virusYchange[v]
        elif virusY[v] >= 400:
            virusYchange[v] = -virusYchange[v]

        virusX[v] += virusXchange[v]
        if virusX[v] <= 0:
            virusXchange[v] = - virusXchange[v]
        elif virusX[v] >= 600:
            virusXchange[v] = -virusXchange[v]
        collision = isCollision(virusX[v], virusY[v], charX, charY)


        if collision:
            lives -= 1
            #print(score_value)
            virusX[v] = random.randint(0, 700)
            virusY[v] = random.randint(0, 250)

        virus(virusX[v], virusY[v], v)

    if score == 20:
        showSuccess()
        pygame.display.update()
        break

    if lives == 0:
        showGameOver()
        pygame.display.update()
        break

    #movement
    charX += charXchange
    charY += charYchange

    #border
    if charX <= 0:
        charX = 0

    if charX >= 592:
        charX = 592

    if charY <= 0:
        charY = 0

    if charY >= 322:
        charY = 322

    redrawGameWindow()

    pygame.display.update()
