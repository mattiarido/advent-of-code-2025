# Challenge https://adventofcode.com/2025/day/7

import os
import random


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

def inject_beam(sequences):
    start_pos = [i for i, pos in enumerate(sequences[0]) if pos == 'S'][0]
    print(start_pos)
    sequences[1][start_pos] = '|'

    for i, line in enumerate(sequences):
        if i == 0 or i == len(sequences) - 1:
            continue

        for j, char in enumerate(line):
            
            if char == '|':
                
                if sequences[i + 1][j] == '^':

                    sequences[i + 1][j - 1] = '|'
                    sequences[i + 1][j + 1] = '|'
                
                else:
                    sequences[i + 1][j] = '|'
    
    return sequences

def part_1(sequences):
    splits = 0
    for i, line in enumerate(sequences):
        for j, char in enumerate(line):
            if char == '^' and sequences[i - 1][j] == '|':
                splits += 1
    return splits

    
def part_2(sequences):
    start_pos = [i for i, pos in enumerate(sequences[0]) if pos == 'S'][0]
    beamer_rates = {start_pos: 1}

    for i, line in enumerate(sequences):
        
        if i == 0 or i == len(sequences) - 1:
            continue

        new_beamer_rates = {}

        for j, char in enumerate(line): 
            if char == '|':
                positions_to_count = set([j])

                if j > 1 and sequences[i][j - 1] == '^':
                    positions_to_count.add(j - 1)

                if j + 1 < len(sequences[i]) and sequences[i][j + 1] == '^':
                    positions_to_count.add(j + 1)

                beamer_rate = 0
                for pos in positions_to_count:
                    beamer_rate += beamer_rates.get(pos, 0) 

                new_beamer_rates[j] = beamer_rate
        
        print(f'new rates: {new_beamer_rates}')
        beamer_rates = new_beamer_rates
    

    return beamer_rates

if __name__ == "__main__":
    sequences = read_input()
    print("Part 1:")
    sequences = inject_beam(sequences)
    write_matrix(sequences, '07/puzzle_output.txt')
    splitters = part_1(sequences)
    print(f'splitters {splitters}')
    print("Part 2:")
    beamer_rates = part_2(sequences)
    print(f'possible choices {beamer_rates}')
    print(f'number possible choices {sum([v for k, v in beamer_rates.items()])}')
    
