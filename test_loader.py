import loader
import os

tiles, entities = loader.load("test")

for x in tiles: print("Tile:", x)
for x in entities: print("Entity:", x)
