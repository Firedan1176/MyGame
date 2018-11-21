# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

import pygame

class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except (pygame.error, message):
            print("Unable to load spritesheet image:", filename)
            raise (SystemExit, message)
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

sprites = {
    "none" : 0,
    "todo" : 63,
    "black" : 68,
    "ui" : {
        "highlight" : 8,
        "select" : 9,
        "target" : 10,
        "health_1" : 11,
        "health_2" : 12,
        "health_3" : 13,
        "health_4" : 14,
        "health_5" : 15,
        "q_large" : 21,
        "circle" : 24,
        "exclamation" : 34,
        "num_0" : 42,
        "num_1" : 43,
        "num_2" : 44,
        "num_3" : 45,
        "num_4" : 46,
        "num_5" : 47,
        "num_6" : 48,
        "num_7" : 49,
        "num_8" : 50,
        "num_9" : 51,
        "q_low" : 61,
        "q_upp" : 62,
        "x1" : 64,
        "x2" : 65,
        "highlight2" : 66,
        },
    "misc" : {
        
        },
    "ground" : {
        "grass" : {

            },
        "dirt" : {

            },
        "sand" : {

            },
        "rock" : {

            },
        "stone" : {

            }
        },
    "wall" : {

        },
    "icon" : {

        },
    "pickup" : {

        }
    
    }
