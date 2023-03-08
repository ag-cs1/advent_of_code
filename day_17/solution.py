def get_highest_point(vx, vy):
    return ((vx * (vx + 1))/2, (vy * (vy + 1))/2)

def main():
    print(get_highest_point(6,9))


if __name__ == "__main__":
    main()