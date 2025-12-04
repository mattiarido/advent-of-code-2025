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
    if num_len % n == 0:
        segments = [num[i: i + n] for i in range(0, num_len, n)]
        if all(segment == segments[0] for segment in segments):
            print(f"Found matching number: {num}")
            return True
    return False

def part_1(sequences):
    repeating_numbers = []

    for seq in sequences:
        for num in parse_sequence(seq):
            is_rep = is_repeating_twice(num)
            if is_rep:
                repeating_numbers.append(num)
    print(f"Total repeating numbers twice found: {len(repeating_numbers)}")
    print(f'sum: {sum(int(num) for num in repeating_numbers)}')

def part_2(sequences):
    repeating_numbers = []

    for seq in sequences:
        for num in parse_sequence(seq):
            i = 1
            while i <= len(num) // 2:
                is_rep = is_repeating_n_times(num, i)
                if is_rep:
                    repeating_numbers.append(num)
                    break
                i += 1
    print(f"Total repeating numbers any times found: {len(repeating_numbers)}")
    print(f'sum: {sum(int(num) for num in repeating_numbers)}')    

if __name__ == "__main__":
    sequences = read_input()
    print("Part 1:")
    part_1(sequences)
    print("\nPart 2:")
    part_2(sequences)
