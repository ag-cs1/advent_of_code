import numpy as np

# increase width of output to view letters in grid
np.set_printoptions(edgeitems=30, linewidth=100000,
                    formatter=dict(float=lambda x: "%.3g" % x))


def parse_text():
    with open("input.txt") as f:
        text = f.read()
        coord = [list(map(int, line.split(',')))
                 for line in text[0:text.find("fold") - 2].split("\n")]
        folds = [[entry[0][-1], int(entry[1])] for entry in [line.split('=')
                                                             for line in text[text.find("fold"):].split('\n')]]
        return coord, folds


def populate_grid(coord):
    coord = np.array(coord)
    maxs = coord.max(axis=0, keepdims=True)
    grid = np.zeros((maxs[0][1] + 1, maxs[0][0] + 1), int)
    for c in coord:
        grid[c[1]][c[0]] = '1'
    return grid


def fold_on_y(y, grid):
    fold_area, grid = grid[(y + 1):, :], grid[:y, :]

    total_dots, grid_row = 0, 0
    for row_index in range(len(fold_area) - 1, -1, -1):
        for col_index in range(len(fold_area[row_index])):
            if fold_area[row_index][col_index] == 1:
                grid[grid_row][col_index] = 1
            if grid[grid_row][col_index] > 0:
                total_dots += 1
        grid_row += 1
    return grid, total_dots


def fold_on_x(x, grid):
    fold_area, grid = grid[:, (x + 1):], grid[:, :x]

    total_dots = 0
    for row_index in range(len(fold_area)):
        grid_col = 0
        for col_index in range(len(fold_area[row_index]) - 1, -1, -1):
            if fold_area[row_index][col_index] == 1:
                grid[row_index][grid_col] = 1
            if grid[row_index][grid_col] > 0:
                total_dots += 1
            grid_col += 1
    return grid, total_dots


def make_folds(grid, folds, num):
    dots = 0
    for x in range(num):
        if folds[x][0] == 'x':
            grid, dots = fold_on_x(folds[x][1], grid)
        elif folds[x][0] == 'y':
            grid, dots = fold_on_y(folds[x][1], grid)
    return grid, dots


def main():
    coord, folds = parse_text()
    grid = populate_grid(coord)
    _, dots = make_folds(grid, folds, 1)
    print(dots)

    grid = populate_grid(coord)
    grid, _ = make_folds(grid, folds, len(folds))
    print(grid)


if __name__ == "__main__":
    main()
