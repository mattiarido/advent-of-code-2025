# Challenge https://adventofcode.com/2025/day/6

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "puzzle_input.txt")

def read_input():
    with open(file_path, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line.split() for line in lines]
    return lines

def read_input_cephalopodly():
    with open(file_path, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    return lines

def do_operations(numbers_to_operate, operations):
    results = []

    for j in range(len(numbers_to_operate)):
        numbers, operation = numbers_to_operate[j], operations[j]
        if operation == '+':
            sum_result = 0
            for number in numbers:
                sum_result += int(number)
            results.append(sum_result)

        if operation == '*':
            mul_result = 1
            for number in numbers:
                mul_result *= int(number)
            results.append(mul_result)
    return results

def part_1(sequences):
    
    operations = sequences[len(sequences) - 1]

    print(f'found {len(sequences) - 1} rows')
    print(f'number of operations upon {len(sequences[0])}')

    numbers_to_operate = [list() for i in range(len(sequences[0]))]

    for row in sequences[:len(sequences) - 1]:
        for i, num in enumerate(row):
            numbers_to_operate[i].append(num)
   
    return do_operations(numbers_to_operate, operations)

    
def part_2(sequences):
    operations = sequences[len(sequences) - 1]

    print(f'found {len(sequences) - 1} rows')

    operations_pos = [i for i, char in enumerate(operations) if char in ['+', '*']]

    numbers_to_operate = [list() for i in range(len(operations_pos))]

    for line in sequences[:len(sequences) - 1]:
        for i in range(len(operations_pos)):
            
            if i == len(operations_pos) - 1:
                numbers_to_operate[i].append(line[operations_pos[i]:])
            
            else:
                numbers_to_operate[i].append(line[operations_pos[i]: operations_pos[i + 1] - 1])

    numbers_to_operate_cephalopodly = [list() for i in range(len(operations_pos))]

    for j, numbers in enumerate(numbers_to_operate):
        numbers_to_operate_cephalopodly[j] = ['' for i in range(len(numbers[0]))]
        for number in numbers:
            for i, char in enumerate(number):
                
                numbers_to_operate_cephalopodly[j][i] += char
    
    return do_operations(numbers_to_operate_cephalopodly, operations.split())


if __name__ == "__main__":
    sequences = read_input()
    print("Part 1:")
    results = part_1(sequences)
    print(f'results {results}')
    print(f'number of operations {len(results)}')
    print(f'grand total {sum(results)}')
    print("Part 2:")
    sequences = read_input_cephalopodly()
    results = part_2(sequences)
    print(f'results {results}')
    print(f'number of operations {len(results)}')
    print(f'grand total {sum(results)}')
    
    
