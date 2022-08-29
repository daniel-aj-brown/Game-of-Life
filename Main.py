import pygame as pg
import numpy as np
import random

BLUE = (59, 127, 148)
YELLOW = (205, 159, 54)
DARKYELLOW = (169, 126, 26)

WORLDSIZE = 90
TILESIZE = 10

FPS = 10

class Engine:
    def __init__(self, width, height, fps):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = width, height
        self.FPS = fps
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()

        self.world = np.zeros((WORLDSIZE, WORLDSIZE))
        self.drawworld = self.world.copy()

        for i in range(1000):
            self.world[random.randint(0, WORLDSIZE-1)][random.randint(0, WORLDSIZE-1)] = 1

    def input(self):
        pass

    def update(self):
        for i in range(len(self.world)-2):
            for j in range(len(self.world[0])-2):
                count = 0
                # for each cell, count the number of alive cell surrounding it.
                for target in ((-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)):
                    if self.world[1+i+target[0]][1+j+target[1]] == 1:
                        count += 1
                # if the cell is alive and has 2 or 3 neighbours, the cell stays alive.
                if self.world[1+i][1+j] == 1 and 2 <= count  <= 3:
                    self.drawworld[1+i][1+j] = 1
                # If the cell is dead and has exactly 3 alive neighbours, the cell comes to life.
                elif self.world[1+i][1+j] == 0 and count == 3:
                    self.drawworld[1 + i][1 + j] = 1
                # Otherwise, the cell dies.
                else:
                    self.drawworld[1+i][1+j] = 0

        # Set the currently world tile map to draw world tile map for the next frame's calculation.
        self.world = self.drawworld.copy()

    def draw(self):
        self.screen.fill(BLUE)
        for c in range(len(self.drawworld)):
            for r in range(len(self.drawworld[0])):
                if self.drawworld[c][r] == 1:
                    pg.draw.rect(self.screen, YELLOW, (c*TILESIZE, r*TILESIZE, TILESIZE, TILESIZE))
                    pg.draw.rect(self.screen, DARKYELLOW, (c*TILESIZE, r*TILESIZE, TILESIZE, TILESIZE), 1)

    def run(self):
        while True:
            self.input()
            self.update()
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == "__main__":
    app = Engine(WORLDSIZE*TILESIZE, WORLDSIZE*TILESIZE, FPS)
    app.run()