from turtle import distance


def parse_text():
    with open("input.txt") as f:
        return list(map(lambda x: int(x), f.read().split(',')))


def populate_init_distance(crabs):
    distances = [0] * (max(crabs) + 1)
    for crab in crabs:
        distances[crab] += 1
    return distances


def rotate_distance(distances, center):
    add = distances[0:center]
    for i in range(0, center):
        distances = distances[1:len(distances)] + [0]

    for i in range(0, len(add)):
        distances[center] += add[i]
        center -= 1

    return distances


def populate_all_distances(init_distance):
    distances = []
    distances.append(init_distance)
    for i in range(1, len(init_distance)):
        distances.append(rotate_distance(init_distance, i))
    return distances


def calculate_fuel_cost(distance_list):
    sum = 0
    for i in range(0, len(distance_list)):
        sum += (i * distance_list[i])
    return sum


def get_min_fuel_cost(distances):
    fuel_costs = list(map(calculate_fuel_cost, distances))
    return min(fuel_costs)


def main():
    crabs = parse_text()
    init_distance = populate_init_distance(crabs)
    distances = populate_all_distances(init_distance)
    min = get_min_fuel_cost(distances)
    print(min)

    #distances = distances[1:] + distances[:1]


if __name__ == "__main__":
    main()
