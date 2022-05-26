from turtle import distance


def parse_text():
    with open("input.txt") as f:
        return list(map(lambda x: int(x), f.read().split(',')))


def part_1(crabs):
    sums = []
    for i in range(max(crabs)):
        sums.append(sum([abs(i - c) for c in crabs]))
    print(min(sums))


def part_2(crabs):
    sums = []
    for i in range(max(crabs)):
        sums.append(sum([(abs(i - c) * (abs(i - c) + 1))/2 for c in crabs]))
    print(min(sums))


def main():
    crabs = parse_text()
    part_1(crabs)
    part_2(crabs)


if __name__ == "__main__":
    main()
