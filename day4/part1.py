with open("input.txt", "r") as f:
    inputs = f.read().split("\n\n")
    numbers = [int(num) for num in inputs[0].split(",")]
    boards = []
    for board_raw in inputs[1:]:
        board_processed = []
        for line in board_raw.split("\n"):
            if not line:
                continue
            board_processed.append([[int(num), False] for num in line.split(" ") if num])
        boards.append(board_processed)

def get_board_columns(board):
    columns = []
    for i in range(len(board[0])):
        columns.append([row[i] for row in board])
    
    return columns

def check_winners(input_boards):
    copied_boards = input_boards.copy()
    for iboard, board in enumerate(copied_boards):
        row_cols = board + get_board_columns(board)
        for line in row_cols:
            winning = all(marked for marked in [elem[1] for elem in line])
            if winning:
                return iboard

def mark_boards(input_boards, num):
    copied_boards = input_boards.copy()
    for board in copied_boards:
        for line in board:
            for elem in line:
                if elem[0] == num:
                    elem[1] = True

    return copied_boards

def sum_unmarked_fields(board):
    retsum = 0
    for line in board:
        for elem in line:
            if not elem[1]:
                retsum += elem[0]

    return retsum

for num in numbers:
    boards = mark_boards(boards, num)
    winner = check_winners(boards)

    if winner is not None:
        unmarked_sum = sum_unmarked_fields(boards[winner])
        print(unmarked_sum * num)
        break

