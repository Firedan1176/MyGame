import sys
import pygame
from pygame.locals import *
import spritesheet
import loader

TILESIZE = 32
MAPWIDTH = 16
MAPHEIGHT = 16

class Player:
    xPos = 0
    yPos = 0
    xVel = 0
    yVel = 0
    SPEED = 3
    def __init__(self, X = 0, Y = 0):
        self.xPos = X
        self.yPos = Y

pygame.init()

display = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))
pygame.display.set_caption("My Game")

ss_xsize = 64
ss_ysize = 48
ss = spritesheet.spritesheet('spritesheet_magenta.png')
images = ss.images_at(((x * TILESIZE, y * TILESIZE, 32, 32) for y in range(48) for x in range(64)), colorkey = (255, 0, 255))

clock = pygame.time.Clock()

tiles = []
entities = []
player = Player(0, 0)

tiles, entities = loader.load("test")

for i, k in spritesheet.sprites.items():
    x = k
    while isinstance(x, dict):
        x = x.items()
    print(x)
        

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Closing game...")
            pygame.quit()
            print("Game closed.")
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                player.xVel = 1
            if event.key == K_LEFT:
                player.xVel = -1
            if event.key == K_UP:
                player.yVel = -1
            if event.key == K_DOWN:
                player.yVel = 1
        if event.type == KEYUP:
            if event.key == K_RIGHT or event.key == K_LEFT:
                player.xVel = 0
            if event.key == K_UP or event.key == K_DOWN:
                player.yVel = 0

    player.xPos += player.xVel * player.SPEED
    player.yPos += player.yVel * player.SPEED
    
    for _tile in tiles:
        display.blit(images[_tile[0]], (_tile[2] * TILESIZE, _tile[1] * TILESIZE))
    display.blit(images[128], (player.xPos, player.yPos))

    pygame.display.update()
    clock.tick(30)
