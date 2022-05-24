def count_increases(input):
    res = 0
    for x in range(1, len(input)):
        if input[x] > input[x - 1]:
            res += 1
    return res

def main():
    # split input.txt into list using newline delim
    with open("input.txt") as f:
        input = f.read().split('\n')

    # print result
    print(count_increases(input))


if __name__ == "__main__":
    main()