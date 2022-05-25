def parse_text():
    # split input.txt into list using newline delim
    with open("input.txt") as f:
        return f.read().splitlines()

# creates nested list [[0,0],[0,0]...]
# each element represents position of gamma/epsilon str
def create_occur_list(input):
    occur = []
    for i in input[:]:
        occur.append([0,0])

    return occur

# update nested list with occurences of 0s and 1s
def update_occurences(input, occur):
    for x in range(0, len(input)):
        if input[x] == "0":
            occur[x][0] += 1
        elif input[x] == "1":
            occur[x][1] += 1
    return occur

def get_gamma_epsilon(input, occur):
    gamma = ""
    epsilon = ""

    for i in input:
        occur = update_occurences(i, occur)

    for o in occur:
        if o[0] > o[1]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return gamma, epsilon


def main():
    bin_nums = parse_text()
    occur = create_occur_list(bin_nums[0])
    gamma, epsilon = get_gamma_epsilon(bin_nums, occur)
    print(int(gamma, 2) * int(epsilon, 2))



if __name__ == "__main__":
    main()