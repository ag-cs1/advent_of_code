class Space():
    def __init__(self, value):
        self.value = value
        self.marked = False

    def print_space(self):
        print(str(self.value) + " " + str(self.marked))

class Board():
    def __init__(self):
        self.total = 0
        self.grid = []

    def print_board(self):
        print("Print Board:")
        for row in self.grid:
            for space in row:
                print(str(space.value) + " " + str(space.marked), end=" ")
            print()