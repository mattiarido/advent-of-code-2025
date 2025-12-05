# Challenge https://adventofcode.com/2025/day/5

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "puzzle_input.txt")

def read_input():
    with open(file_path, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def get_bounds_from_interval(interval):
    for i, char in enumerate(interval):
        if char == '-':
            dash_pos = i
    lower_bound = interval[:dash_pos]
    upper_bound = interval[dash_pos + 1:] 
    return int(lower_bound), int(upper_bound)


def part_1(fresh_intervals, available_ingredients):
    fresh_ingredients = set()

    for ingr in available_ingredients:
        for interval in fresh_intervals:
            lower_bound, upper_bound = get_bounds_from_interval(interval)
            if int(ingr) >= int(lower_bound) and int(ingr) <= int(upper_bound):
                print(f'ingredient {ingr} between {lower_bound} and {upper_bound}')
                fresh_ingredients.add(ingr)
    
    return fresh_ingredients

def trim_interval(reference_interval, interval_to_trim):
    
    if reference_interval[0] == interval_to_trim[0]:
        trimmed_interval = (reference_interval[1] + 1, interval_to_trim[1])

    elif reference_interval[1] >= interval_to_trim[0]:
        trimmed_interval = (reference_interval[1] + 1, interval_to_trim[1])
    
    else:
        trimmed_interval = interval_to_trim
    
    if trimmed_interval[0] > trimmed_interval[1]:
        return -1, -1

    return trimmed_interval 
    
def part_2(fresh_intervals):
    consecutive_intervals = []

    for interval in fresh_intervals:
        interval = get_bounds_from_interval(interval)
        consecutive_intervals.append(interval)

    consecutive_intervals = sorted(consecutive_intervals, key=lambda x: (x[0], x[1]))

    print(consecutive_intervals)

    non_overlapping_intervals = []
    
    for interval in consecutive_intervals:
        print(f'got interval {interval}')

        if len(non_overlapping_intervals) == 0:
            non_overlapping_intervals.append(interval)
        
        to_add = True

        for prev_interval in non_overlapping_intervals:
            if interval == prev_interval:
                to_add = False
                break
            
            interval = trim_interval(prev_interval, interval)
            
            if interval == (-1, -1):
                to_add = False
                break
            
        print(f'after merge, got interval {interval}')
        if to_add:
            non_overlapping_intervals.append(interval)

    return non_overlapping_intervals

if __name__ == "__main__":
    sequences = read_input()

    for i, row in enumerate(sequences):
        if row == '':
            blank_line_pos = i
    fresh_intervals = sequences[:blank_line_pos]
    available_ingredients = sequences[blank_line_pos + 1:]

    print("Part 1:")
    fresh_ingredients = part_1(fresh_intervals, available_ingredients)
    print(f'fresh ingredients: {len(fresh_ingredients)}')
    print("Part 2:")
    fresh_ingredients_all = part_2(fresh_intervals)
    print(f'all fresh ingredients: {fresh_ingredients_all}')
    print(f'all fresh ingredients: {sum([inter[1] - inter[0] + 1 for inter in fresh_ingredients_all])}')

    
