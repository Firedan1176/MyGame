import sys
import pygame
from pygame.locals import *
import spritesheet
import loader
import mymath

TILESIZE = 32
MAPWIDTH = 16
MAPHEIGHT = 16

pygame.init()

display = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))
pygame.display.set_caption("My Edit")

ss_xsize = 64
ss_ysize = 48
ss = spritesheet.spritesheet('spritesheet_magenta.png')
images = ss.images_at(((x * TILESIZE, y * TILESIZE, 32, 32) for y in range(48) for x in range(64)), colorkey = (255, 0, 255))

tiles = ["0", "1"]
entities = []

class Cursor:
    position = (0, 0)
    selected = 0
    active = True

    highlightRect = images[spritesheet.sprites["ui"]["highlight"]]
    
    def __init__(self, startPosition = (0, 0)):
        self.position = startPosition
        
    def draw(self):
        display.blit(self.highlightRect, (self.position[0] * TILESIZE, self.position[1] * TILESIZE))

    def move(self, delta):
        self.position = (mymath.clamp(self.position[0] + delta[0], 0, MAPWIDTH - 1), mymath.clamp(self.position[1] + delta[1], 0, MAPHEIGHT - 1))
        print(self.position)

    def mousemove(self, pos):
        if self.active:
            self.position = (int(pos[0] / TILESIZE), int(pos[1] / TILESIZE))

    def tileselect(self, index):
        self.selected = index

    def tileset(self):
        settile(self.position, self.selected)

    def tileadd(self):
        print("Adding tiles not yet supported")
        pass
    

def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Closing game...")
            pygame.quit()
            print("Game closed.")
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                cursor.move((1, 0))
            if event.key == K_LEFT:
                cursor.move((-1, 0))
            if event.key == K_UP:
                cursor.move((0, -1))
            if event.key == K_DOWN:
                cursor.move((0, 1))
            if event.key == K_RETURN:
                cursor.tileset()
#        if event.type == MOUSEMOTION:
#            cursor.mousemove(pygame.mouse.get_pos())

def init():
    global tiles
    tiles = list((x, y) for y in range(MAPHEIGHT) for x in range(MAPWIDTH))

def draw():
    display.fill((0,0,0))
    for _tile in tiles:
        print(_tile)
        display.blit(images[_tile[0]], (_tile[2] * TILESIZE, _tile[1] * TILESIZE))
    cursor.draw()
    pygame.display.update()


def settile(coords, index):
    tiles[coords[1] * MAPHEIGHT + coords[0]] = (coords[0], coords[1], index)



clock = pygame.time.Clock()
cursor = Cursor((8, 8))

init()

while True:
    update()
    draw()

    clock.tick(30)

