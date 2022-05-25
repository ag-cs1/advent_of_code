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