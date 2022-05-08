import pygame
from graphics import *
from snake import snake
from keyboard import is_pressed
from time import sleep
from pygame import *
import sys

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (235, 64, 52)
GREEN = (0, 204, 0)
SCREENSIZE = (400,400)
class Game():
    def __init__(self):
        self.fps = 30
        self.tickrate = 3
        self.game = snake.Game((20,20), 10)
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.done = False
        self.timer = 0
        self.direction = "right"

    def mainLoop(self):
        dt = 0
        self.clock.tick()
        while not self.done:
            self.eventLoop()
            self.getDirection()
            self.update(dt)
            self.draw()
            #self.screen.fill(BLACK)
            #pygame.display.update()
            dt = self.clock.tick(self.fps)

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    def update(self, dt):
        self.timer += dt
        while self.timer >= 1000/(self.tickrate):
            self.timer -= 1000/self.tickrate
            self.game.update(self.direction)
            self.done = self.game.lost

    def draw(self):
        self.screen.fill(BLACK)
        rectSize = SCREENSIZE[0]/ self.game.gridSize[0], SCREENSIZE[1] / self.game.gridSize[1]
        for i, row in enumerate(self.game.grid):
            for j, cell in enumerate(row):
                cellRect = pygame.Rect((j * rectSize[0], i * rectSize[1]), rectSize)
                if cell.state == 0:
                    color = WHITE
                if cell.state == -1:
                    color = RED
                if cell.state > 0:
                    color = GREEN[0], self.snakeColor(cell) , GREEN[2]
                pygame.draw.rect(self.screen, color, cellRect, width=0)
        pygame.display.update()

    def getDirection(self):
        for key in ["right", "left", "down", "up"]:
            if is_pressed(key):
                self.direction = key

    def snakeColor(self, cell):
        #print(cell.state/self.game.snake.length)
        return int((cell.state)/self.game.snake.length*128) +127


def main():
    pygame.init()
    pygame.display.set_caption("Snake")
    pygame.display.set_mode(SCREENSIZE)
    Game().mainLoop()
    pygame.quit()
    sys.exit()







if __name__ == "__main__":
    main()
