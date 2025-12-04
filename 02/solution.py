# Challenge https://adventofcode.com/2025/day/2

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "puzzle_input.txt")

def read_input():
    with open(file_path, 'r') as f:
        lines = f.read().split(',')
    return lines

def parse_sequence(sequence):
    start, end = map(int, sequence.split('-'))
    interval = list(range(start, end + 1))
    return [str(num) for num in interval]

def is_repeating_twice(num):
    num_len = len(num)
    if num_len % 2 == 0:
        half = num_len // 2
        first_half = num[:half]
        second_half = num[half:]
        if first_half == second_half:
            print(f"Found matching number: {num}")
            return True
    return False

def is_repeating_n_times(num, n):
    num_len = len(num)
    if num_len % 2 == 0:
        half = num_len // 2
        first_half = num[:half]
        second_half = num[half:]
        if first_half == second_half:
            print(f"Found matching number: {num}")
            repeating_numbers.append(num)

if __name__ == "__main__":
    sequences = read_input()

    repeating_numbers = []

    for seq in sequences:
        for num in parse_sequence(seq):
            is_rep = is_repeating_twice(num)
            if is_rep:
                repeating_numbers.append(num)
    
    print(f"Total repeating numbers found: {len(repeating_numbers)}")
    print(f'sum: {sum(int(num) for num in repeating_numbers)}')