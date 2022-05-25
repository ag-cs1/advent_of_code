from space import Space, Board

### parsing functions ###
def get_text():
     with open("input.txt") as f:
        return f.read().split('\n')

def parse_input(input):
    drawn_nums = input[0].split(',')
    boards = get_boards(input)
    return drawn_nums, boards

def get_boards(input):
    boards = []
    curr_board = Board()
    for i in range(1, len(input)):
        if not input[i]:
            if(curr_board.grid):
                boards.append(curr_board)
            curr_board = Board()
        else:
            curr_board.grid.append(create_row(input[i], curr_board))
    boards.append(curr_board)
    return boards

def create_row(row_input, board):
    values = row_input.split(' ')
    row = []
    for v in values:
        if (v.isnumeric()):
            row.append(Space(int(v)))
            board.total += int(v)
    return row


### bingo functions ###

def check_row(row):
    for space in row:
        if not space.marked:
            return False
    return True

def check_column(column):
    for space in column:
        if not space.marked:
            return False
    return True

def check_for_row_completion(board):
    completed = False
    for row in board.grid:
        if check_row(row):
            return True
    return False

def check_for_column_completion(board):
    for i in range(0, len(board.grid)):
        if check_column([row[i] for row in board.grid]):
            return True
    return False


def mark_all_boards(num, boards):
    found_winner = False
    winning_board = None
    win_ind = []
    for i in range(0, len(boards)):
        boards[i], found_winner = mark_board(num, boards[i])
        if found_winner:
            winning_board = boards[i]
            win_ind.append(i)
    boards = ([v for i, v in enumerate(boards) if i not in win_ind])
    return boards, winning_board

def mark_board(num, board):
    for i in range(0, len(board.grid)):
        for j in range(0, len(board.grid[i])):
            value = board.grid[i][j].value
            if int(num) == value:
                board.grid[i][j].marked = True
                board.total -= int(num)
    return board, check_for_row_completion(board) or check_for_column_completion(board)

def play_bingo(nums, boards):
    winning_board = None
    winning_total = 0
    for num in nums:
        boards, winning_board = mark_all_boards(num, boards)
        if winning_board:
            winning_total = int(num) * winning_board.total
            winning_board = None
    return winning_total

# driver
def main():
    #PART 1
    input = get_text()
    drawn_nums, boards = parse_input(input)
    print(play_bingo(drawn_nums, boards))

if __name__ == "__main__":
    main()
