num_to_string = {}
string_to_num = {}


def parse_text():
    with open("input.txt") as f:
        parsed = []
        lines = f.read().split("\n")
        for line in lines:
            split = line.split(" | ")
            parsed.append([[''.join(sorted(entry)) for entry in split[0].split(" ")], [
                          ''.join(sorted(entry)) for entry in split[1].split(" ")]])
        return parsed


def find_unique_numbers(input):
    remaining = {}
    for i in input:
        if len(i) == 2:
            num_to_string[1] = i
            string_to_num[i] = '1'
        elif len(i) == 3:
            num_to_string[7] = i
            string_to_num[i] = '7'
        elif len(i) == 4:
            num_to_string[4] = i
            string_to_num[i] = '4'
        elif len(i) == 7:
            num_to_string[8] = i
            string_to_num[i] = '8'
        else:
            remaining[i] = [0] * 2
    return remaining


def compare(str, remaining, i):
    for key in remaining:
        for s in str[:]:
            if s in key:
                remaining[key][i] += 1
    return remaining


def check_remaining(remaining):
    for key in remaining:
        if remaining[key] == [4, 2]:
            string_to_num[key] = '9'
        elif remaining[key] == [2, 1]:
            string_to_num[key] = '2'
        elif remaining[key] == [3, 1]:
            if len(key) == 6:
                string_to_num[key] = '6'
            else:
                string_to_num[key] = '5'
        elif remaining[key] == [3, 2]:
            if len(key) == 6:
                string_to_num[key] = '0'
            else:
                string_to_num[key] = '3'


def solve(remaining, output):
    remaining = compare(num_to_string[4], remaining, 0)
    remaining = compare(num_to_string[1], remaining, 1)
    check_remaining(remaining)
    return find_output(output)


def find_output(output):
    res = ""
    for o in output:
        res += string_to_num[o]
    return int(res)


def main():
    res = 0
    entries = parse_text()
    for entry in entries:
        num_to_string = {}
        string_to_num = {}
        remaining = find_unique_numbers(entry[0])
        res += solve(remaining, entry[1])
    print(res)


if __name__ == "__main__":
    main()
