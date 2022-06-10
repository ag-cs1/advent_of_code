from math import prod


versions = []


def parse_text():
    with open("input.txt") as f:
        hex_value = f.read()
        return str(bin(int(hex_value, base=16)))[2:].zfill(len(hex_value) * 4)


def parse_bin_literal(bin_str):
    bin_lit = ""
    while True:
        bits, bin_str = parse_segment(bin_str, 5)
        bin_lit += bits[1:]
        if bits[0] == '0':
            break
    return int(bin_lit, 2), bin_str


def parse_segment(bin_str, len):
    return bin_str[:len], bin_str[len:]


def parse_operator(bin_str):
    len_type_id, bin_str = parse_segment(bin_str, 1)
    values = []
    if len_type_id == '0':
        length, bin_str = parse_segment(bin_str, 15)
        sub_bit_str, bin_str = parse_segment(bin_str, int(length, 2))
        while len(sub_bit_str) > 0:
            value, sub_bit_str = parse_packet(sub_bit_str)
            values.append(value)
    else:
        length, bin_str = parse_segment(bin_str, 11)
        for i in range(int(length, 2)):
            value, bin_str = parse_packet(bin_str)
            values.append(value)
    return values, bin_str


def parse_packet(bin_str):
    version, bin_str = parse_segment(bin_str, 3)
    type_id, bin_str = parse_segment(bin_str, 3)
    type_id = int(type_id, 2)
    versions.append(int(version, 2))
    if type_id == 4:
        return parse_bin_literal(bin_str)
    else:
        values, bin_str = parse_operator(bin_str)
        res = calculate_operation(values, type_id)
        return res, bin_str


def calculate_operation(values, type):
    if type == 0:
        res = sum(values)
    elif type == 1:
        res = prod(values)
    elif type == 2:
        res = min(values)
    elif type == 3:
        res = max(values)
    elif type == 5:
        res = (lambda x, y: 1 if x > y else 0)(values[0], values[1])
    elif type == 6:
        res = (lambda x, y: 1 if x < y else 0)(values[0], values[1])
    elif type == 7:
        res = (lambda x, y: 1 if x == y else 0)(values[0], values[1])
    return res


def main():
    bin_str = parse_text()
    res, _ = parse_packet(bin_str)

    # part 1
    print(sum(versions))

    # part 2
    print(res)


if __name__ == "__main__":
    main()
