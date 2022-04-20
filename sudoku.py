import random
import numpy as np
import os


class Solution:
    def gen_sudoku(self):
        matrix = [[0 for i in range(9)] for i in range(9)]
        matrix = np.array(matrix)

        # Creating the first row in the matrix
        r1 = [i for i in range(1, 10)]
        random.shuffle(r1)
        matrix[0] = r1

        # creating rest of the matrix
        for i in range(1, 9):
            if i in [1, 2, 4, 5, 7, 8]:
                matrix[i] = list(matrix[i - 1][3:]) + list(matrix[i - 1][0:3])
            if i in [3, 6]:
                matrix[i] = list(matrix[i - 1][1:]) + list(matrix[i - 1][0:1])
        return matrix

    def generate_box(self, matrix):
        m = matrix.copy()
        line = "-" * 34
        for i in range(9):
            if i == 0 or i == 3 or i == 6:
                print(line)
            nums = f": {m[i, 0]}  {m[i, 1]}  {m[i, 2]}  " \
                   f": {m[i, 3]}  {m[i, 4]}  {m[i, 5]}  " \
                   f": {m[i, 6]}  {m[i, 7]}  {m[i, 8]}  :"
            print(nums)
            if i == 8:
                print(line)

    def generate_puzzle(self, matrix):
        modif_m = matrix.copy()
        deleted = [7, 7, 4, 4, 4, 3, 3, 2, 2]
        random.shuffle(deleted)
        for i in range(len(modif_m)):
            lst = []
            for j in range(deleted[i]):
                while True:
                    n = random.randint(0, 8)
                    if n not in lst:
                        lst.append(n)
                        break
                        
            for k in lst:
                modif_m[i, k] = 0
        return modif_m


def start_game(puzz_matrix, completed_matrix):
    puzzle = puzz_matrix
    objs = Solution
    objs.generate_box(puzzle, puzzle)
    while 0 in puzzle:
        try:
            print("Enter row, column number (0-8) and also the actual number (1-9) to enter (like 1, 2, 3 format (0, 0, 0) to quit the game): ")
            i, j, n = map(int, input().split(","))
        except:
            continue
        if i == 0 and j == 0 and n == 0:
            print("Program Terminated Successfully")
            break
        if puzzle[i, j] != 0:
            print("Please chose a different number")
            continue
        if i not in range(9) or j not in range(9):
            print("Please enter correct row/column number")
            continue
        if n not in range(1, 10):
            print("Number out of range!")
            continue
        if completed_matrix[i, j] != n:
            print(f"answer is {completed_matrix[i,j]}")
            print("Incorrect number")
            continue
        else:
            puzzle[i, j] = n
        os.system("cls")
        objs.generate_box(puzzle, puzzle)
    else:
        print("Congratulations!")
        print("You solved the puzzle")



obj = Solution()
complete_matrix = obj.gen_sudoku()
puzzle_matrix = obj.generate_puzzle(complete_matrix)
# Starting the game
start_game(puzzle_matrix, complete_matrix)
