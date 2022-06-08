import sys


def parse_text():
    with open("input.txt") as f:
        grid = [list(map(int, list(line))) for line in f.read().split("\n")]
        return grid


def update_graph(v1, v2, grid, graph):
    if v2[0] in range(0, len(grid)) and v2[1] in range(0, len(grid[v2[0]])):
        if v1 not in graph:
            graph[v1] = {}
        graph[v1][v2] = grid[v2[0]][v2[1]]
        if v2 not in graph:
            graph[v2] = {}
        graph[v2][v1] = grid[v1[0]][v1[1]]


def connect_vertices(grid, graph):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
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
    counter = 0
    while len(spt_set) < len(graph):
        u = get_min_distance(distances, spt_set)
        spt_set.add(u)
        for adj_v in graph[u]:
            if (distances[u] + graph[u][adj_v]) < distances[adj_v]:
                distances[adj_v] = distances[u] + graph[u][adj_v]
        counter += 1
    return(distances[end])


def main():
    grid = parse_text()
    graph = {}
    connect_vertices(grid, graph)
    res = dijkstras((0, 0), (len(grid)-1, len(grid[0])-1), graph)
    print(res)


if __name__ == "__main__":
    main()
