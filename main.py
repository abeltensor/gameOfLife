import random
import time
import os

class Game():
    def __init__(self, row, col, delay, generation, alive="*", dead="."):
        self.row = row
        self.col = col
        self.delay = delay
        self.generation = generation
        self.alive = alive
        self.dead = dead

    def rGrid(self, array):
        with open("grid.txt", "r") as file:
            for line in file:
                temp = []
                for i in range (len(line)-1):
                    if line[i] == "*":
                        temp.append(i)
                    elif line[i] == ".":
                        temp.append(0)
                array += [temp]
            print(array)

            for i in range(len(array)):
                for j in range (len(array[0])):
                    if (i == 0 or j == 0 or (i == len(array) - 1) or (j == len(array[0]) - 1)):
                        array[i][j] = -1

    def iGrid(self, array):
        for i in range(self.row):
            singleRow = []
            for j in range(self.col):
                if (i == 0 or j == 0 or (i == self.row - 1) or (j == self.col - 1)):
                    singleRow.append(-1)
                else:
                    ran = random.randint(0, 3)
                    if ran == 0:
                        singleRow.append(1)
                    else:
                        singleRow.append(0)
            array.append(singleRow)

    def startSim(self, cGen):
        nextGen = []
        self.iGrid(nextGen)
        for gen in range(self.generation):
            self.printGen(cGen, gen)
            self.processNextGen(cGen, nextGen)
            time.sleep(self.delay)
            cGen, nextGen = nextGen, cGen
        input("Finished. Press any key to exit")

    def processNextGen(self, cGen, nextGen):
        for i in range(1, self.row-1):
            for j in range(1, self.col-1):
                nextGen[i][j] = self.processNeighbors(i, j, cGen)

    def processNeighbors(self, x, y, cGen):
        neighborCount = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if not (i == x and j == y):
                    if cGen[i][j] != -1:
                        neighborCount += cGen[i][j]
        if cGen[x][y] == 1 and neighborCount < 2:
            return 0
        if cGen[x][y] == 1 and neighborCount > 3:
            return 0
        if cGen[x][y] == 0 and neighborCount == 3:
            return 1
        else:
            return cGen[x][y]
    def printGen(self, cGen, gen):
        os.system("cls")
        print("Conway's game of life simulation. Generation : " + str(gen + 1))
        for i in range(self.row):
            for j in range(self.col):
                if cGen[i][j] == -1:
                    print("#", end=" ")
                elif cGen[i][j] == 1:
                    print(self.alive, end=" ")
                elif cGen[i][j] == 0:
                    print(self.dead, end=" ")
            print("\n")


if __name__ == '__main__':
    print("Select choice : ")
    print("1: Read initial grid from file 'grid.txt'")
    print("2: Generate random grind of size 11X40")

    choice = int(input("Option: "))
    if choice == 1:
        simParams = {
            "row": 5,
            "col": 10,
            "delay": 0.1,
            "generation": 2,
            "dead": " "
        }
        simulation = Game(**simParams)
        thisGen = []
        simulation.rGrid(thisGen)
        simulation.startSim(thisGen)
    elif choice == 2:
        simParams = {
            "row": 22,
            "col": 62,
            "delay": 0.1,
            "generation": 100,
            "dead": " "
        }
        simulation = Game(**simParams)
        cur_gen = []
        simulation.iGrid(cur_gen)
        simulation.startSim(cur_gen)
