# Challenge https://adventofcode.com/2025/day/

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "puzzle_input.txt")

def read_input():
    with open(file_path, 'r') as f:
        return [tuple(map(int, line.strip().split(','))) for line in f if line.strip()]

def calculate_area(angle, opposite_angle):
    base = abs(angle[0]-opposite_angle[0]) + 1
    height = abs(angle[1]-opposite_angle[1]) + 1
    return base * height

def get_perimeter(angle, opposite_angle):
    perimeter = []

    another_angle = [angle[0], opposite_angle[1]]
    another_opposite_angle = [opposite_angle[0], angle[1]]

    empty_spaces_horizontal = abs(angle[0] - opposite_angle[0]) - 1
    empty_spaces_vertical = abs(angle[1] - opposite_angle[1]) - 1
    
    horizontal_start = min(angle[0], opposite_angle[0])
    horizontal_end = max(angle[0], opposite_angle[0])
    vertical_start = min(angle[1], opposite_angle[1])
    vertical_end = max(angle[1], opposite_angle[1])

    if empty_spaces_horizontal >= 0 or empty_spaces_vertical >= 0:
        perimeter.append(another_angle)
        perimeter.append(another_opposite_angle)
    
    if empty_spaces_horizontal > 0:
        for row in range(1, empty_spaces_horizontal + 1):
            perimeter.append([horizontal_start + row, angle[1]])
            perimeter.append([horizontal_start + row, opposite_angle[1]])

    if empty_spaces_vertical > 0:
        for row in range(1, empty_spaces_vertical + 1):
            perimeter.append([angle[0], vertical_start + row])
            perimeter.append([opposite_angle[0], vertical_start + row])

    return perimeter

def is_point_in_perimeter(point, angle, another_angle, opposite_angle, another_opposite_angle):
    if point[0] < min([angle[0], another_angle[0], opposite_angle[0], another_opposite_angle[0]]):
        return False
    
    if point[0] > max([angle[0], another_angle[0], opposite_angle[0], another_opposite_angle[0]]):
        return False
    
    if point[1] < min([angle[1], another_angle[1], opposite_angle[1], another_opposite_angle[1]]):
        return False
    
    if point[1] > max([angle[1], another_angle[1], opposite_angle[1], another_opposite_angle[1]]):
        return False
    
    return True

def tiles_validation(valid_tile1, valid_tile2, tile1, tile2):
    if tile1[0] < min(valid_tile1[0], valid_tile2[0]):
        return False
    
    if tile1[0] > max(valid_tile1[0], valid_tile2[0]):
        return False
    
    if tile2[0] < min(valid_tile1[0], valid_tile2[0]):
        return False
    
    if tile2[0] > max(valid_tile1[0], valid_tile2[0]):
        return False
    
    if tile1[1] < min(valid_tile1[1], valid_tile2[1]):
        return False
    
    if tile1[1] > max(valid_tile1[1], valid_tile2[1]):
        return False
    
    if tile2[1] < min(valid_tile1[1], valid_tile2[1]):
        return False
    
    if tile2[1] > max(valid_tile1[1], valid_tile2[1]):
        return False
    
    return True


def part_1(tiles):

    areas = []
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            tile1 = tiles[i]
            tile2 = tiles[j]
            area = calculate_area(tile1, tile2)
            areas.append((tile1, tile2, area))

    areas.sort(key=lambda x: x[2])
    
    return areas

    
def part_2(tiles_red):
    tiles_green = []
    
    for i in range(len(tiles_red)):
        tile_red = tiles_red[i]
        
        if i == len(tiles_red) - 1:
            next_tile_red = tiles_red[0]
        else:
            next_tile_red = tiles_red[i + 1]

        green_tiles_horizontal = max(0, abs(tile_red[0] - next_tile_red[0]) - 1)
        green_tiles_vertical = max(0, abs(tile_red[1] - next_tile_red[1]) - 1)
        
        horizontal_start = min(tile_red[0], next_tile_red[0])
        vertical_start = min(tile_red[1], next_tile_red[1])

        for col in range(1, green_tiles_horizontal + 1):
            tiles_green.append([horizontal_start + col, tile_red[1]])

        for row in range(1, green_tiles_vertical + 1):
            tiles_green.append([tile_red[0], vertical_start + row])

    areas = []
    for i in range(len(tiles_red)):
        for j in range(i + 1, len(tiles_red)):
            tile1 = tiles_red[i]
            tile2 = tiles_red[j]

            # print(f'considering {tile1} and {tile2}')

            is_valid_area = False
            for k in range(len(tiles_red)):
                valid_tile1 = tiles_red[k]
                
                if k == len(tiles_red) - 1:
                    valid_tile2 = tiles_red[0]
                else:
                    valid_tile2 = tiles_red[k + 1]

                    print(f'considering {tile1} and {tile2} in {valid_tile1},{valid_tile2} the result is {tiles_validation(valid_tile1, valid_tile2, tile1, tile2)}')

                    if tiles_validation(valid_tile1, valid_tile2, tile1, tile2):
                        is_valid_area = True
                        break
            
            if not is_valid_area:
                print(f'skipping {tile1} and {tile2}')
                continue
            
            print(f'adding {tile1} and {tile2}')
            area = calculate_area(tile1, tile2)
            areas.append((tile1, tile2, area))

    areas.sort(key=lambda x: x[2])

    return areas

if __name__ == "__main__":
    sequences = read_input()
    sequences = [[3, 4], [3, 6], [7, 6], [7, 2], [6, 2], [6, 4]]
    print(f'tiles {sequences}')
    # print("Part 1:")
    # areas = part_1(sequences)
    # print(f'areas {areas}')
    print("Part 2:")
    areas = part_2(sequences)
    print(f'areas {areas}')
    
