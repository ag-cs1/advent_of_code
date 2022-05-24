commands_dict = {
        "forward": 0,
        "up": 0,
        "down": 0
    }

def parse_text():
    # split input.txt into list using newline delim
    with open("input.txt") as f:
        return f.read().splitlines()

def get_location(input):
    # 0th is pos, 1st is depth
    location = [0,0]

    for i in input:
        command = i.split(' ')
        commands_dict[command[0]] += int(command[1])

    location[0] = commands_dict["forward"]
    location[1] = commands_dict["down"] - commands_dict["up"]
    return location
    
#part 1
def main():
    commands = parse_text()
    location = get_location(commands)
    print(location[0] * location[1])


if __name__ == "__main__":
    main()