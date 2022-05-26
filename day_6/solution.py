def get_init_list():
    with open("input.txt") as f:
        return list(map(lambda x: int(x), f.read().split(',')))


def populate_occur_list(fish):
    occur_list = [0] * 9
    for f in fish:
        occur_list[f] += 1
    return occur_list


def simulate_days(occur_list, days):
    for i in range(0, days):
        reproducing = occur_list[0]
        occur_list = occur_list[1:] + occur_list[:1]
        occur_list[6] += reproducing
    return sum(occur_list)


def main():
    fish = get_init_list()

    #PART 1
    occur_list = populate_occur_list(fish)
    res = simulate_days(occur_list, 80)
    print(res)

    #PART 2
    occur_list = populate_occur_list(fish)
    res = simulate_days(occur_list, 256)
    print(res)




if __name__ == "__main__":
    main()
