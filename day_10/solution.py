symbols = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

corrupt_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

incomplete_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def parse_text():
    with open("input.txt") as f:
        return f.read().split("\n")


# used in part 1
def find_incorrect_symbol(str):
    stack = []
    for sym in str[:]:
        if sym in symbols:
            stack.append(sym)
        else:
            if sym == symbols[stack[-1]]:
                stack.pop()
            else:
                return sym
    return ''


# used in part 2
def auto_complete(str):
    stack = []
    for sym in str[:]:
        if sym in symbols:
            stack.append(sym)
        else:
            if sym == symbols[stack[-1]]:
                stack.pop()
            else:
                return ""

    completion = []
    while len(stack) > 0:
        completion.append(symbols[stack.pop()])
    return completion


# used in part 2
def calc_complete_scores(str):
    total = 0
    for s in str[:]:
        total *= 5
        total += incomplete_points[s]
    return total


def main():
    # part 1
    lines = parse_text()
    wrong_symbols = list(
        filter(lambda x: x != "", [find_incorrect_symbol(line) for line in lines]))
    total = sum([corrupt_points[sym] for sym in wrong_symbols])
    print(total)

    # part 2
    completions = list(
        filter(lambda x: x != "", [auto_complete(line) for line in lines]))
    scores = [calc_complete_scores(com) for com in completions]
    res = sorted(scores)[int(len(scores) / 2)]
    print(res)


if __name__ == "__main__":
    main()
