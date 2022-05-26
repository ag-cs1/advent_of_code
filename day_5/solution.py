import numpy as np


def get_text():
    with open("input.txt") as f:
        return f.read().split('\n')


def line_to_coord(line):
    coord = line.split(" -> ")
    return [coord[0].split(","), coord[1].split(",")]


def create_grid(lines):
    max_x = 0
    max_y = 0
    for line in lines:
        max_x = max(max_x, int(line[0][0]), int(line[1][0]))
        max_y = max(max_y, int(line[0][1]), int(line[1][1]))
    return np.zeros((max_y + 1, max_x + 1), dtype=int)


def plot_diagonal_line(x1, y1, x2, y2, grid):
    if y1 < y2:
        start_point, end_point = (x1, y1), (x2, y2)
    else:
        start_point, end_point = (x2, y2), (x1, y1)
    dir = -1 if start_point[0] > end_point[0] else 1

    curr_x = int(start_point[0])
    for y in range(start_point[1], end_point[1] + 1):
        grid[y,  curr_x] += 1
        curr_x += dir
    return grid


def populate_grid_no_diagonal(lines, grid):
    for line in list(lines):
        x1, y1, x2, y2 = int(line[0][0]), int(
            line[0][1]), int(line[1][0]), int(line[1][1])
        if (x1 == x2):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[y, x1] += 1
        if (y1 == y2):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1, x] += 1
    return grid


def populate_grid_diagonal(lines, grid):
    for line in list(lines):
        x1, y1, x2, y2 = int(line[0][0]), int(
            line[0][1]), int(line[1][0]), int(line[1][1])
        if (x1 == x2):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[y, x1] += 1
        if (y1 == y2):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1, x] += 1
        elif (x1 != x2 and y1 != y2):
            grid = plot_diagonal_line(x1, y1, x2, y2, grid)
    return grid


def find_intersections(grid):
    num_points = 0
    for x in grid:
        for y in x:
            if y > 1:
                num_points += 1
    return num_points


def main():
    lines = []
    lines = list(map(line_to_coord, get_text()))

    # part 1
    grid = create_grid(lines)
    grid = populate_grid_no_diagonal(lines, grid)
    num_points = find_intersections(grid)
    print(num_points)

    # part 2
    grid = create_grid(lines)
    grid = populate_grid_diagonal(lines, grid)
    num_points = find_intersections(grid)
    print(num_points)


if __name__ == "__main__":
    main()
