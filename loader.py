import os

currentDir = os.getcwd()

def save(mapName, contents):
    fout = open(currentDir + "\\" + mapName + ".map", 'w')
    fout.write(contents)
    fout.close()
    return "Map saved"

def load(mapName):
    fin = open(currentDir + "\\" + mapName + ".map", 'r')
    contents = fin.readlines()
    fin.close()

    tilemapsize = 16 #default

    #Find settings for tilemap
    for line in contents:
        parts = line.split()
        if len(parts) == 0: continue
        if parts[0] == "size":
            print(line)
            tilemapsize = int(parts[1])
        elif parts[0] == "tiles":
            break
            
    #Define empty tileset
    tiles = list([0, x, y] for y in range(tilemapsize) for x in range(tilemapsize))
    entities = []

    #Default tile value of 0
    tile = []
    for line in contents:
        parts = line.split()
        if len(parts) == 0 or line[0] == '#': continue
        elif parts[0] == "select":
            tile = list(int(parts[x + 1]) for x in range(len(parts) - 1))
        elif parts[0] == "fill":
            import random
            coords = parts[1].split(',')
            for i, k in enumerate(coords): coords[i] = int(k)
            for y in range(coords[3] - coords[1] + 1):
                for x in range(coords[2] - coords[0] + 1):
                    tiles[((y + coords[1]) * tilemapsize) + (x + coords[0])] = (tile[random.randint(0, len(tile) - 1)], x + coords[0], y + coords[1])
        elif parts[0] == "drop":
            coords = parts[1].split(',')
            entities.append((tile, int(coords[0]), int(coords[1])))
        else: print("Unknown command:", parts[0])   
    return tiles, entities
