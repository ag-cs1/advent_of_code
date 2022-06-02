

def parse_text():
    with open("input.txt") as f:
        return [list(line) for line in f.read().split("\n")]


def check_low(grid, low_points, r_index, c_index):
    low = True
    value = grid[r_index][c_index]
    # check top
    if r_index > 0:
        if grid[r_index - 1][c_index] <= value:
            low = False
    # check bottom
    if r_index < (len(grid) - 1):
        if grid[r_index + 1][c_index] <= value:
            low = False
    # check left
    if c_index > 0:
        if grid[r_index][c_index - 1] <= value:
            low = False
    # check right
    if c_index < (len(grid[r_index]) - 1):
        if grid[r_index][c_index + 1] <= value:
            low = False

    if low:
        low_points.append(value)

    return low_points


def find_low_points(grid):
    low_points = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            low_points = check_low(grid, low_points, i, j)
    return low_points


def main():
    points = parse_text()
    low_points = find_low_points(points)
    res = sum([int(value) + 1 for value in low_points])

    print(res)


if __name__ == '__main__':
    main()
