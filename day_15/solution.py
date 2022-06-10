import sys
import numpy as np


def parse_text():
    with open("test2.txt") as f:
        temp_grid = [list(map(int, list(line))) for line in f.read().split("\n")]
        grid = np.zeros((5 * len(temp_grid), 5 * len(temp_grid[0])), dtype=int)
        grid[:len(temp_grid), :len(temp_grid[0])] = temp_grid
        return grid, temp_grid

def get_offset_grid(grid, o):
    new_grid = [[i+o if i+o<=9 else i+o-9 for i in row] for row in grid]
    print(new_grid)
    return new_grid

def update_graph(v1, v2, grid, graph):
    if v2[0] in range(0, len(grid)) and v2[1] in range(0, len(grid[v2[0]])):
        if v1 not in graph:
            graph[v1] = {}
        graph[v1][v2] = grid[v2[0]][v2[1]]
        if v2 not in graph:
            graph[v2] = {}
        graph[v2][v1] = grid[v1[0]][v1[1]]


def connect_vertices(grid, graph):
    for i in range(len(grid)/5):
        for j in range(len(grid[i])):
            print(f'{i},{j}')
            update_graph((i, j), (i-1, j), grid, graph)
            update_graph((i, j), (i, j-1), grid, graph)
            update_graph((i, j), (i+1, j), grid, graph)
            update_graph((i, j), (i, j+1), grid, graph)


def get_min_distance(distances, spt_set):
    min = sys.maxsize
    min_vertex = None
    for d in distances:
        if d not in spt_set and distances[d] < min:
            min = distances[d]
            min_vertex = d
    return min_vertex


def dijkstras(start, end, graph):
    spt_set = set()
    distances = {x: sys.maxsize for x in graph}
    distances[start] = 0
    while len(spt_set) < len(graph):
        u = get_min_distance(distances, spt_set)
        spt_set.add(u)
        for adj_v in graph[u]:
            if (distances[u] + graph[u][adj_v]) < distances[adj_v]:
                distances[adj_v] = distances[u] + graph[u][adj_v]
    return(distances[end])

def get_bigger_grid(big_grid, temp_grid):
    for i in range(1,5):
        get_offset_grid(temp_grid, i)


def main():
    grid, temp_grid = parse_text()
    new_grid = get_bigger_grid(grid, temp_grid)
    graph = {}
    #connect_vertices(grid, graph)
    #res = dijkstras((0, 0), (len(grid)-1, len(grid[0])-1), graph)
    #print(res)
    print(new_grid)


if __name__ == "__main__":
    main()
