# Challenge https://adventofcode.com/2025/day/1

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "puzzle_input.txt")

def read_input():
    with open(file_path, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

DIAL_START = 50
TURNING_POINT = 100

def move_dial(current_position, direction, steps):
    if steps > TURNING_POINT:
        steps = steps % TURNING_POINT
    if direction == 'L':
        if current_position - steps < 0:
            current_position = current_position - steps + TURNING_POINT
        else:
            current_position = current_position - steps
    elif direction == 'R':
        if current_position + steps >= TURNING_POINT:
            current_position = current_position + steps - TURNING_POINT
        else:
            current_position = current_position + steps
    return current_position

def main():
    rotations = read_input()
    
    dial_position = DIAL_START
    print(f"Starting position: {dial_position}")

    dial_position_zero_cnt = 0

    for rotation in rotations:
        dial_position = move_dial(dial_position, rotation[0], int(rotation[1:]))
        if dial_position == 0:
            dial_position_zero_cnt += 1
        print(f"Moved {rotation}, new position: {dial_position}")

    print(f"Dial position was zero {dial_position_zero_cnt} times")

if __name__ == "__main__":
    main()