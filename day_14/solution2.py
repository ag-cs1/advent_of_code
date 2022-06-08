def parse_text():
    rules = {}
    with open("input.txt") as f:
        text = f.read().split('\n')
        template = text[0]
        rules = dict([tuple(line.split(" -> ")) for line in text[2:]])
        return template, rules


def find_initial_pairs_chars(template):
    chars = {c: template.count(c) for c in list(set(template))}
    pairs = {}
    for i in range(len(template) - 1):
        pair = template[i:(i + 2)]
        if pair not in pairs:
            pairs[pair] = 0
        pairs[pair] += 1
    return chars, pairs


def take_step(chars, pairs, rules):
    for p, c in list(pairs.items()):
        new_char = rules[p]
        if new_char not in chars:
            chars[new_char] = 0
        chars[new_char] += c
        pairs[p] -= c
        if (p[0] + new_char) not in pairs:
            pairs[p[0] + new_char] = 0
        pairs[p[0] + new_char] += c
        if (new_char + p[1]) not in pairs:
            pairs[new_char + p[1]] = 0
        pairs[new_char + p[1]] += c


def take_steps(chars, pairs, rules, steps):
    for _ in range(steps):
        take_step(chars, pairs, rules)
    return max(chars.values()) - min(chars.values())


# PART 2
# used reddit for hint on this one
# tracked only pairs and char count for each step
def main():
    template, rules = parse_text()
    chars, pairs = find_initial_pairs_chars(template)
    res = take_steps(chars, pairs, rules, 40)

    print(res)


if __name__ == "__main__":
    main()
