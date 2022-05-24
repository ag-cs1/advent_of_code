def parse_text():
    # split input.txt into list using newline delim
    with open("input.txt") as f:
        return f.read().splitlines()

def get_location(input):
    # 0th is pos, 1st is depth
    location = [0,0]
    aim = 0

    for i in input:
        command = i.split(' ')
        if command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])
        elif command[0] == "forward":
            location[0] += int(command[1])
            location[1] += int(command[1]) * aim

    return location
  
def main():
    #PART 1
    commands = parse_text()
    location = get_location(commands)
    print(location[0] * location[1])


if __name__ == "__main__":
    main()