def get_init_list():
    with open("input.txt") as f:
        return list(map(lambda x: int(x), f.read().split(',')))


def update_fish(fish):
    for i in range(0, len(fish)):
        if fish[i] > 0:
            fish[i] -= 1
        else:
            fish[i] = 6
            fish.append(8)
    return fish


# returns fish count after given num of days
def get_fish_count(fish, days):
    for i in range(0, days):
        fish = update_fish(fish)
    return len(fish)


def main():
    fish = get_init_list()
    num_fish = get_fish_count(fish, 80)
    print(num_fish)


if __name__ == "__main__":
    main()
