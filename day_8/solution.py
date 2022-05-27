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
