import os
import Grid
from time import sleep
from keyboard import is_pressed
def clear():
    os.system("cls")

def createGrid():
    return Grid.Grid(20,20, 10)
def main():
    grid = createGrid()
    grid.printGrid()
    lastkey = "right"
    playing = True
    while playing:
        if is_pressed("right"):
            lastkey = "right"
            grid.update("right")
        elif is_pressed("left"):
            lastkey = "left"
            grid.update("left")
        elif is_pressed("up"):
            lastkey = "up"
            grid.update("up")
        elif is_pressed("down"):
            lastkey = "down"
            grid.update("down")
        elif is_pressed("escape"):
            playing = False
        else: grid.update(lastkey)
        clear()
        grid.printGrid()
        if grid.snake.alive == False:
            playing = False
        sleep(0.75)
    #grid.update
    #draw()
if __name__ == "__main__":
    main()
