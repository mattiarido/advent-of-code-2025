# Challenge https://adventofcode.com/2025/day/3

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "puzzle_input.txt")

def read_input():
    with open(file_path, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def part_1(sequences):
    max_joltages = []
    
    for seq in sequences:
        print(f"Sequence: {seq}")
        max_first_digit = max(int(digit) for digit in seq)
        print(f"Max first digit: {max_first_digit}")
        if seq[-1] == str(max_first_digit):
            print(f"Max digit is at the end of the sequence. removing to find higher digit.")
            max_first_digit = max(int(digit) for digit in seq[:-1])
            print(f"New max first digit: {max_first_digit}")

        for i, digit in enumerate(seq):
            if int(digit) == max_first_digit:
                rest_of_sequence = seq[i+1:]
                max_second_digit = max(int(d) for d in rest_of_sequence) if rest_of_sequence else None
                print(f"Max digit after position {i}: {max_second_digit}")
                break

        max_joltage = str(max_first_digit) + str(max_second_digit)
        max_joltages.append(max_joltage)
    return max_joltages

def get_maximum_and_right_seq(seq):
    max_digit = max(int(digit) for digit in seq)
    if seq[-1] == str(max_digit):
            print(f"Max digit is at the end of the sequence. removing to find higher digit.")
            max_digit = max(int(digit) for digit in seq[:-1])
            print(f"New max first digit: {max_digit}")

    for i, digit in enumerate(seq):
            if int(digit) == max_digit:
                break

    return max_digit, seq[i+1:]

    
def part_2(sequences):
    max_joltages = []
    
    for seq in sequences:
        print(f"Sequence: {seq}")
        
        max_digits = []
        digit_count = 0
        while digit_count < 12:
            max_digit, seq = get_maximum_and_right_seq(seq)
            max_digits.append(max_digit)
            digit_count += 1
        
        max_joltage = ''.join(str(d) for d in max_digits)
        max_joltages.append(max_joltage)
        return max_joltages

if __name__ == "__main__":
    sequences = read_input()
    print("Part 1:")
    max_joltages = part_1(sequences)
    print('sum of max joltages:', sum(int(joltage) for joltage in max_joltages))
    print("Part 2:")
    max_joltages = part_2(sequences)
    print('sum of max joltages:', sum(int(joltage) for joltage in max_joltages))
    
