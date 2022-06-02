

from math import prod


def parse_text():
    with open("input.txt") as f:
        return [list(line) for line in f.read().split("\n")]


def check_adj(i, j, grid):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '9' or grid[i][j] == 'X':
        return 0
    else:
        grid[i][j] = 'X'
        return 1 + check_adj(i, j - 1, grid) + check_adj(i, j + 1, grid) + check_adj(i - 1, j, grid) + check_adj(i + 1, j, grid)


def find_basins(grid):
    basins = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '9' and grid[i][j] != 'X':
                basins.append(check_adj(i, j, grid))
    return basins


def main():
    points = parse_text()
    basins = find_basins(points)
    res = prod(sorted(basins, reverse=True)[:3])
    print(res)


if __name__ == '__main__':
    main()
