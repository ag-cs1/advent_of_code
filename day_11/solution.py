def parse_text():
    with open("input.txt") as f:
        return [list(map(int, list(line))) for line in f.read().split("\n")]


def increase_energy(i, j, grid, flashes):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return 0
    grid[i][j] += 1
    if grid[i][j] == 10:
        flashes[(i,j)] = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                increase_energy(x, y, grid, flashes)
    

def take_step(grid):
    flashes = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            increase_energy(i, j, grid, flashes)
    return [[0 if x > 9 else x for x in row] for row in grid], len(flashes)


#only used in part 1
def take_steps(grid, steps):
    total = 0
    for s in range(steps):
        grid, curr_total = take_step(grid)
        total += curr_total
    return total


#only used in part 2
def take_steps_until_sync(grid):
    flashes = 0
    steps = 0
    while flashes < (len(grid) * len(grid[0])):
        grid, flashes = take_step(grid)
        steps += 1
    return steps


def main():
    #part 1
    grid = parse_text()
    total = take_steps(grid, 100)
    print(total)

    #part 2
    grid = parse_text()
    res = take_steps_until_sync(grid)
    print(res)


if __name__ == "__main__":
    main()
