# Challenge https://adventofcode.com/2025/day/3

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "puzzle_input.txt")

def read_input():
    with open(file_path, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [list(line) for line in lines]
    return lines

def write_matrix(matrix, filename):
    with open(filename, "w") as f:
        for row in matrix:
            f.write("".join(x for x in row) + "\n")

def get_rolls_around(matrix, row_num, col_num):
    total_row = len(matrix)
    total_col = len(matrix[0])
    
    rolls = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            row_to_check = row_num + i
            col_to_check = col_num + j

            if row_num + i < 0 or row_num + i > total_row - 1:
                continue

            if col_num + j < 0 or col_num + j > total_col - 1:
                continue
            
            if matrix[row_to_check][col_to_check] == '@':
                rolls += 1
    
    return rolls

def get_available_rolls(matrix):
    total_row = len(matrix)
    total_col = len(matrix[0])
    
    rolls_available = []
    for i in range(0, total_row):
        for j in range(0, total_col):
             if matrix[i][j] == '@':
                rolls_around = get_rolls_around(matrix, i, j)
                if rolls_around < 4:
                    rolls_available.append([i, j])
    return rolls_available

def part_1(matrix):
    return get_available_rolls(matrix)

    
def part_2(matrix):
    rolls_removed = []

    while True:
        rolls_available = get_available_rolls(matrix)

        if len(rolls_available) == 0:
            break
        
        for roll in rolls_available:
            matrix[roll[0]][roll[1]] = '.'
            rolls_removed.append(roll)
        
        print(f'removed {len(rolls_available)} rolls')

    
    write_matrix(matrix, os.path.join(BASE_DIR, "puzzle_output.txt"))
    return rolls_removed

if __name__ == "__main__":
    matrix = read_input()
    print("Part 1:")
    rolls_available = part_1(matrix)
    print(f'rolls available: {len(rolls_available)}')
    print("Part 2:")
    rolls_available = part_2(matrix)
    print(f'rolls available: {len(rolls_available)}')
    
