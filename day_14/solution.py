def parse_text():
    rules = {}
    with open("input.txt") as f:
        text = f.read().split('\n')
        template = text[0]
        rules = dict([tuple(line.split(" -> ")) for line in text[2:]])
        return template, rules


def insert_between_pattern(string, start, pattern, c):
    i_pos = string.find(pattern, start)
    if i_pos >= 0:
        string = string[:(i_pos + 1)] + c + string[(i_pos + 1):]
        start = i_pos + 2

    return string, start


def take_step(template, rules):
    start = 0
    while start < len(template) - 1:
        p = template[start:(start + 2)]
        if p in rules:
            template, start = insert_between_pattern(
                template, start, p, rules[p])
        else:
            start += 1
    return template


def take_steps(template, rules, steps):
    for i in range(steps):
        template = take_step(template, rules)
    return template


def calculate_res(template):
    quantities = [template.count(c) for c in list(set(template))]
    return max(quantities) - min(quantities)

# used naive approach of generating string for every step
# this did not work for part 2 (see solution2.py)
def main():
    template, rules = parse_text()
    new_template = take_steps(template, rules, 10)
    res = calculate_res(new_template)
    print(res)


if __name__ == "__main__":
    main()
