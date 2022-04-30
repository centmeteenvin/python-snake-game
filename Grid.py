from random import randint

class Grid():
    def __init__(self, rows, columns, amount):
        self.__size = (rows, columns)
        self.snake = Snake(self.__size)
        self.apple = Apple(self.snake, self.__size, amount)
        self.grid = self.createGrid()
        self.score = len(self.snake.pos) - 5

    def createGrid(self):
        grid = list()
        for i in range(self.__size[0]):
            grid.append(list())
            for j in range(self.__size[1]):
                grid[i].append(Cell(i, j))
        for pos in self.snake.pos:
            grid[pos[0]][pos[1]].state = 1
        for pos in self.apple.pos:
            grid[pos[0]][pos[1]].state = 2
        return grid
    def printGrid(self):
        output = ""
        for i in range(self.__size[0]):
            output += "\n"
            for j in range(self.__size[1]):
                if self.grid[i][j].state == 0:
                    output +=  ". "
                elif self.grid[i][j].state == 1:
                    output += "# "
                else:
                    output += "O "
        output += "\n" + str(self.score)
        print(output)
    def update(self, key):
        self.snake.update(self.grid, self.apple, key)
        for row in self.grid:
            for cell in row:
                if cell.pos in self.snake.pos :
                    cell.state = 1
                elif cell.pos in self.apple.pos:
                    cell.state = 2
                else:
                    cell.state = 0
        self.score = len(self.snake.pos) - 5

class Cell():
    def __init__(self, x, y):
        #state 0: empty, state 1: snake, state 2:apple
        self.state = 0
        self.pos = (x, y)

    def __repr__(self):
        return "Cell"

class Snake():
    def __init__(self, gridsize):
        self.pos = self.createSnake(gridsize)
        self.dir = "right"
        self.alive = True
    def createSnake(self, gridsize):
        pos = list()
        for i in range(5):
            tpos = (int(gridsize[1]/2), int(gridsize[0]/2) -2 + i)
            pos.append(tpos)
        return pos
    def update(self, grid, apple, key):
        if self.nextpos(grid, key) != self.pos[len(self.pos)-2]:
            self.dir = key
        nextpos = (self.nextpos(grid, self.dir))
        if nextpos in self.pos:
            self.alive = False
        self.pos.append(nextpos)
        haseaten = False
        for i in range(len(apple.pos)):

            if nextpos == apple.pos[i]:
                haseaten = True
                newpos = (randint(0, len(grid) - 1), randint(0, len(grid[0]) - 1))
                while newpos in self.pos:
                    newpos = (randint(0, len(grid) - 1), randint(0, len(grid[0]) - 1))
                apple.pos[i] = newpos
        if haseaten == False:
            self.pos.pop(0)
    def nextpos(self, grid, dir):
        head = self.pos[len(self.pos)-1]
        if dir == "right":
            return (head[0], (head[1]+1)%len(grid[0]))
        if dir == "left":
            return (head[0], (head[1] - 1) % len(grid[0]))
        if dir == "up":
            return ((head[0] - 1) % len(grid), head[1])
        if dir == "down":
            return ((head[0] + 1) % len(grid), head[1])

class Apple():
    def __init__(self, snake, gridsize, amount):
        self.pos = self.createapples(snake, gridsize, amount)

    def createapples(self, snake, gridsize, amount):
        pos = list()
        for i in range(amount):
            newpos = (randint(0, gridsize[0]-1), randint(0, gridsize[1] - 1))
            while newpos in pos or newpos in snake.pos:
                newpos = (randint(0, gridsize[0] - 1), randint(0, gridsize[1] - 1))
            pos.append(newpos)
        return pos


def main():
    cell = Cell( 1, 1)
    grid = Grid(20, 20, 10)
    grid.printGrid()
    while input() != "q":
        grid.update("right")
        grid.printGrid()
    return None

if __name__ == "__main__":
    main()