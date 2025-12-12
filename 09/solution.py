# Challenge https://adventofcode.com/2025/day/

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "puzzle_input.txt")

def read_input():
    with open(file_path, 'r') as f:
        return [tuple(map(int, line.strip().split(','))) for line in f if line.strip()]
    
def normalize_input(input):
    min_x = min(tile[0] for tile in input)
    min_y = min(tile[1] for tile in input)

    return [[tile[0] - min_x, tile[1] - min_y] for tile in input]

def calculate_area(angle, opposite_angle):
    base = abs(angle[0]-opposite_angle[0]) + 1
    height = abs(angle[1]-opposite_angle[1]) + 1
    return base * height

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

    # Fill the edge gaps
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

    polygon_perimeter = tiles_red + tiles_green
    perimeter_set = set(map(tuple, polygon_perimeter))

    # Loop over couples of red tiles: 
    #   - construct the rectangle
    #   - check that every point inside the ractangle lays inside the polygon: go left/right from the point and count how many times a border is hit. If odd, the point is inside. Do the same for up/down
    
    grid_boundary_x = (min(tile[0] for tile in tiles_red), max(tile[0] for tile in tiles_red))
    grid_boundary_y = (min(tile[1] for tile in tiles_red), max(tile[1] for tile in tiles_red))

    areas = []
    for i in range(len(tiles_red)):
        for j in range(i + 1, len(tiles_red)):
            tile1 = tiles_red[i]
            tile2 = tiles_red[j]

            # for easiness, I'll skip all the segment-like rectangles
            if tile1[0] == tile2[0] or tile1[1] == tile2[1]:
                continue

            print(f'considering {tile1} and {tile2}')

            x_points = (min(tile1[0], tile2[0]) + 1, max(tile1[0], tile2[0]) - 1) 
            y_points = (min(tile1[1], tile2[1]) + 1, max(tile1[1], tile2[1]) - 1) 

            is_valid_area = True
            for x, y in [(x, y) for x in x_points for y in y_points]:
                
                polygon_borders = 0
                for look_x_right in range(x + 1, grid_boundary_x[1] + 1):
                    # print('evaluating', [look_x_right, y], 'in', perimeter_reacheable_x)
                    if (look_x_right, y) in perimeter_set:
                        polygon_borders += 1
                if polygon_borders % 2 == 0:
                    is_valid_area = False
                    break

                polygon_borders = 0
                for look_y_up in range(y + 1, grid_boundary_y[1] + 1):
                    if (x, look_y_up) in perimeter_set:
                        polygon_borders += 1
                if polygon_borders % 2 == 0:
                    is_valid_area = False
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
    # sequences = [[3, 4], [3, 6], [7, 6], [7, 2], [6, 2], [6, 4]]
    print(f'tiles {sequences}')
    # print("Part 1:")
    # areas = part_1(sequences)
    # print(f'areas {areas}')
    print("Part 2:")
    areas = part_2(sequences)
    print(f'areas {areas}')
    
