def add_to_graph(key, value, graph):
    if key != 'end' and value != 'start':
        if key in graph:
            if value not in graph[key]:
                graph[key].append(value)
        else:
            graph[key] = [value]


def parse_text():
    graph = {}
    with open("input.txt") as f:
        for line in f.read().split("\n"):
            caves = line.split('-')
            add_to_graph(caves[0], caves[1], graph)
            add_to_graph(caves[1], caves[0], graph)
    return graph

# only used in part 1
def traverse_path(start, end, graph, paths, path, small_caves):
    if not path:
        path = [start]
    if start != end:
        for dest in graph[start]:
            if not(dest in path and dest in small_caves):
                new_path = path.copy()
                new_path.append(dest)
                paths.append(new_path)
                traverse_path(new_path[-1], end, graph,
                              paths, new_path, small_caves)


# only used in part 2
def can_be_added(path, dest, small_caves):
    if dest in small_caves:
        cave_count = [[], [], []]
        for c in small_caves:
            cave_count[path.count(c)].append(c)
        return (len(cave_count[2]) == 0) or (dest in cave_count[0])
    return True


# only used in part 2
def traverse_path_p2(start, end, graph, paths, path, small_caves):
    if not path:
        path = [start]
    if start != end:
        for dest in graph[start]:
            if can_be_added(path, dest, small_caves):
                new_path = path.copy()
                new_path.append(dest)
                paths.append(new_path)
                traverse_path_p2(new_path[-1], end,
                                 graph, paths, new_path, small_caves)


def main():
    graph = parse_text()
    small_caves = list(filter(lambda x: x != 'start' and x !=
                              'end' and x.islower(), [key for key in graph]))

    #part 1
    paths = []
    traverse_path('start', 'end', graph, paths, [], small_caves)
    res = (list(filter(lambda x: x[0] == 'start' and x[-1] == 'end', paths)))
    print(len(res))

    #part 2
    paths = []
    traverse_path_p2('start', 'end', graph, paths, [], small_caves)
    res = (list(filter(lambda x: x[0] == 'start' and x[-1] == 'end', paths)))
    print(len(res))


if __name__ == "__main__":
    main()
