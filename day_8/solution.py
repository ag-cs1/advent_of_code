# key = num of segments
# values = numbers with num of segments
segment_dict = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8],
}

number_dict = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}


def parse_text():
    with open("input.txt") as f:
        output_lists = [line.split(" | ")[1].split(" ") for line in f.read().split("\n")]
        output = []
        for l in output_lists:
            output += l
        return output

def main():
    output = parse_text()
    res = len(list(filter(lambda x: len(x) in [2, 3, 4, 7], output)))
    print(res)


if __name__ == "__main__":
    main()
