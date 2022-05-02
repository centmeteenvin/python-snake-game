import snake.snake as snk
import os
from time import sleep
from keyboard import is_pressed
def printTocmd(game):
    output = ""
    for i in range(game.gridSize[0]):
        for j in range(game.gridSize[1]):
            value = game.grid[i][j].state
            if value == -1:
                output += "A"
            elif value == 0:
                output += "."
            else:
                output += str(value)
            output += " "
        output += "\n"
    print(output)

def clear():
    os.system("cls")

def main():
    game = snk.Game((20,20), 10)
    lastdirection = "right"
    while not game.lost:
        if is_pressed("right") and game.update("right") != -1:
            lastdirection = "right"
        elif is_pressed("left") and game.update("left") != -1:
            lastdirection = "left"
        elif is_pressed("down") and game.update("down") != -1:
            lastdirection = "down"
        elif is_pressed("up") and game.update("up") != -1:
            lastdirection = "up"
        else: game.update(lastdirection)
        clear()
        printTocmd(game)
        print(game.snake.alive)
        sleep(1)
    input()

if __name__ == "__main__":
    main()