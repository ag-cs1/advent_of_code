def parse_text():
    # split input.txt into list using newline delim
    with open("input.txt") as f:
        return f.read().splitlines()

# creates nested list [[0,0],[0,0]...]
# each element represents position of gamma/epsilon str
def init_occur_list(input):
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

def get_occur(input):
    occur = init_occur_list(input[0])
    
    for i in input:
        occur = update_occurences(i, occur)

    return occur

def get_gamma_epsilon(occur):
    gamma = ""
    epsilon = ""
    for o in occur:
        if o[0] > o[1]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return gamma, epsilon

def run_filter(pos, bit, nums):
    if len(nums) > 1:
        nums = list(filter(lambda x: x[pos] == bit, nums))
    return nums

def get_ox_co2(occur, bin_nums, greater_bit, lesser_bit):
    res = bin_nums
    occur_len = len(occur)
    for i in range(0, occur_len):
        if (occur[i][0] > occur[i][1]):
            res = run_filter(i, greater_bit, res)
        else:
            res = run_filter(i, lesser_bit, res)
        occur = get_occur(res)

    return res[0]

def main():
    bin_nums = parse_text()
    occur = get_occur(bin_nums)
    gamma, epsilon = get_gamma_epsilon(occur)
    print(int(gamma, 2) * int(epsilon, 2))

    #rename
    ox_gen= get_ox_co2(occur, bin_nums, "0", "1")
    co2_scrub = get_ox_co2(occur, bin_nums, "1", "0")
    print(int(ox_gen, 2) * int(co2_scrub, 2))



if __name__ == "__main__":
    main()