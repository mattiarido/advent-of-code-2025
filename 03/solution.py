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

def get_maximum_and_right_seq(seq, digits_to_find):
    if len(seq) < digits_to_find:
        raise ValueError(f'you are requesting more digits ({digits_to_find}) than available {seq}')

    if len(seq) == digits_to_find:
       print(f'seq {seq} is shorter than needed ({digits_to_find}), returning {seq[0]}')
       max_digit = seq[0]
       return max_digit, seq[1:]
    
    max_digit = max(int(digit) for digit in seq)
    if digits_to_find > 1:
        if str(max_digit) in seq[-digits_to_find:] and str(max_digit) not in seq[:-digits_to_find-1]:
                print(f"in sequence {seq} Max digit {max_digit} is at the end of the sequence. removing to find higher digit.")
                max_digit = max(int(digit) for digit in seq[:-digits_to_find+1])
                print(f"New max first digit: {max_digit}")

    for i, digit in enumerate(seq):
            if int(digit) == max_digit:
                break

    print(f'max digit {max_digit} found in position {i}')

    return max_digit, seq[i+1:]

    
def part_2(sequences):
    max_joltages = []
    
    for seq in sequences:
        print(f"Sequence: {seq}")
        
        max_digits = []
        digit_count = 0
        while digit_count < 12:
            print(f'sequence so far {seq}')
            print(f'looking for {digit_count+1}th digit')
            max_digit, seq = get_maximum_and_right_seq(seq, 12 - digit_count)
            max_digits.append(max_digit)
            digit_count += 1
            print(f'max {digit_count}th digit found: {max_digit}')
        
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
    
