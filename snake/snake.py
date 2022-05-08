from random import randint
from time import sleep
class Game():
    def __init__(self, gridSize = (10, 10), numberOfApples = 3):
        self.gridSize = gridSize
        self.snake = Snake(gridSize)
        self.apples = Apple(gridSize, numberOfApples, self.snake)
        self.grid = self.__createGrid(gridSize, self.snake.pos, self.apples.pos)
        self.lost = not self.snake.alive
    
    def __createGrid(self, gridSize, snakePos, applesPos):
        grid = list()
        for i in range(gridSize[0]):
            grid.append(list())
            for j in range(gridSize[1]):
                grid[i].append(Cell((i,j), snakePos, applesPos))
        return grid

    def update(self, direction):
        self.snake.update(self.gridSize, direction,self.apples)
        self.grid = self.__createGrid(self.gridSize, self.snake.pos, self.apples.pos)
        self.lost = not self.snake.alive


class Snake():
    #the Snake object contains an array of positions with the head on index 0
    def __init__(self, gridSize):
        self.alive = True
        self.pos = self.__createSnake(gridSize)
        self.length = len(self.pos)
        self.direction =  "right"
    def __createSnake(self, gridSize):
        pos = list()
        for i in range(5):
            #pos is an list of tuples: (ypos, xpos)
            pos.append(
                ( int(gridSize[0]/2) - 1,
                  int(gridSize[1]/2) +1 - i )
            )
        return pos

    def update(self, gridSize, direction, apples):
        head = self.pos[0]
        nextHead = self.pos[1]
        while nextHead == self.pos[1]:
            if direction == "right":
                nextHead = (head[0], (head[1] + 1) % gridSize[1])
            elif direction == "left":
                nextHead = (head[0], (head[1] - 1) % gridSize[1])
            elif direction == "up":
                nextHead = ((head[0]-1) % gridSize[0], head[1])
            elif direction == "down":
                nextHead = ((head[0] + 1) % gridSize[0], head[1])
            if nextHead == self.pos[1]:
                direction = self.direction
        self.direction = direction
        if nextHead in self.pos:
            self.alive = False
        self.pos.insert(0, nextHead)
        if nextHead in apples.pos:
            i = 0
            while nextHead != apples.pos[i]:
                i += 1
            prohibitedPos = self.pos + apples.pos
            apples.pos[i] = apples.generateApplePositions(gridSize, 1, prohibitedPos)[0]
            self.length = len(self.pos)
        else:
            self.pos.pop(len(self.pos)-1)


class Apple():
    #Apple is the object that contains all coordinates of the apples
    def __init__(self, gridSize, numberOfApples, snake):
        self.pos = self.generateApplePositions(gridSize, numberOfApples, snake.pos)

    def generateApplePositions(self, gridSize, numberOfapples, prohibitedPositions):
        pos = list()
        for i in range(numberOfapples):
            potentialPos = (randint(0, gridSize[0]-1), randint(0, gridSize[0]-1))
            while potentialPos in prohibitedPositions:
                potentialPos = (randint(0, gridSize[0] - 1), randint(0, gridSize[0] - 1))
            pos.append(potentialPos)
        return pos

class Cell():
    def __init__(self, pos, snakePos, applePos):
        self.pos = pos
        #state -1: apple, state 0: empty, state bigger than 0 is snake, the number indicates the age
        self.state = self.__getState(snakePos, applePos)

    def __getState(self, snakePos, applePos):
        if self.pos in snakePos or self.pos in applePos:
            if self.pos in snakePos:
                i = 0
                while self.pos != snakePos[i]:
                    i += 1
                return i + 1
            else:
                return -1
        else: return 0

if __name__ == "__main__":
    game = Game((10,10), 3)
    while True:
        game.update("left")
        sleep(1)