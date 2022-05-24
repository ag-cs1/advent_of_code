def count_increases(input):
    res = 0
    for x in range(1, len(input)):
        if input[x] > input[x - 1]:
            res += 1
    return res

def get_windows(input):
    windows = []
    for x in  range(0, len(input) - 2):
        windows.append(int(input[x]) + int(input[x + 1]) + int(input[x + 2]))
    return windows

def split_text():
    # split input.txt into list using newline delim
    with open("input.txt") as f:
        return f.read().split('\n')

def main():
    #PART 1
    input = split_text()
    print(count_increases(input))

    #PART 2
    windows = get_windows(input)
    print(count_increases(windows))


if __name__ == "__main__":
    main()