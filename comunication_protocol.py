import random, sys


def were_play(danger_column, danger_line, y, x):
    oth_x = 0
    oth_y = 0
    hplay = False
    if danger_line > danger_column:
        while oth_x != function_obj.size:
            if function_obj.board[y][oth_x] == 2:
                if (oth_x - 1) >= 0 and function_obj.board[y][oth_x - 1] == 0:
                    function_obj.board[y][oth_x - 1] = 1
                    hplay = True
                    print(str(y) + "," + str(oth_x - 1))
                    sys.stdout.flush()
                    break
                elif (oth_x + 1) < function_obj.size and function_obj.board[y][oth_x + 1] == 0:
                    function_obj.board[y][oth_x + 1] = 1
                    hplay = True
                    print(str(y) + "," + str(oth_x + 1))
                    sys.stdout.flush()
                    break
            oth_x += 1
    elif danger_column > danger_line:
        while oth_x != function_obj.size:
            if function_obj.board[oth_y][x] == 2:
                if (oth_y - 1) >= 0 and function_obj.board[oth_y - 1][x] == 0:
                    function_obj.board[oth_y - 1][x] = 1
                    hplay = True
                    print(str(oth_y - 1) + "," + str(x))
                    sys.stdout.flush()
                    break
                elif (oth_y + 1) < function_obj.size and function_obj.board[oth_y + 1][x] == 0:
                    function_obj.board[oth_y + 1][x] = 1
                    hplay = True
                    print(str(oth_y + 1) + "," + str(x))
                    sys.stdout.flush()
                    break
            oth_y += 1
    if hplay == False:
        ia_algo_fill(function_obj.board)


def ia_algo_def(board):
    danger = 0
    nbsymb = 0
    value_dangerous_line = 0
    line_danger = 0
    value_dangerous_column = 0
    column_danger = 0
    y = 0
    x = 0

    ##LINE
    while y != function_obj.size:
        x = 0
        while x != function_obj.size:
            if function_obj.board[y][x] == 2:
                danger += 1
                nbsymb += 1
            if function_obj.board[y][x] == 1:
                danger -= 1
                nbsymb += 1
            x += 1
            if nbsymb < function_obj.size - 1 and danger >= value_dangerous_line:
                value_dangerous_line = danger
                line_danger = y
        danger = 0
        y += 1
    x = 0
    y = 0
    danger = 0
    nbsymb = 0
    ## COLUMN
    while x != function_obj.size:
        y = 0
        while y != function_obj.size:
            if function_obj.board[y][x] == 2:
                danger += 1
                nbsymb += 1
            if function_obj.board[y][x] == 1:
                danger -= 1
                nbsymb += 1
            y += 1
            if nbsymb < function_obj.size - 1 and danger > value_dangerous_column:
                value_dangerous_column = danger
                column_danger = x
        danger = 0
        x += 1
    if value_dangerous_column >= 2 or value_dangerous_line >= 2:
        were_play(value_dangerous_column, value_dangerous_line, line_danger, column_danger)
    else:
        ia_algo_fill(function_obj.board)


def play(y, x):
    if function_obj.board[y][x] != 0:
        play((random.randint(0, function_obj.size - 2)), (random.randint(0, function_obj.size - 2)))
    function_obj.board[y][x] = 1
    print(str(y) + "," + str(x))
    sys.stdout.flush()


def search_board():
    nb_of_one = 0
    y = 0
    while y != function_obj.size:
        x = 0
        while x != function_obj.size:
            if function_obj.board[y][x] == 1:
                nb_of_one += 1
            x += 1
        y += 1
    if nb_of_one >= 1:
        return True
    return False

def ia_algo_fill(board):
    y = 0
    done = False
    hplay = False
    something_board = search_board()
    if something_board == False:
        play((random.randint(0, function_obj.size - 2)), (random.randint(0, function_obj.size - 2)))
        done = True
    while done == False:
        while y != function_obj.size:
            x = 0
            while x != function_obj.size:
                if function_obj.board[y][x] == 1:
                    if (y - 1) >= 0 and function_obj.board[y - 1][x] == 0:
                        hplay = True
                        play(y - 1, x)
                        done = True
                        break
                    if (y + 1) < function_obj.size and function_obj.board[y + 1][x] == 0:
                        hplay = True
                        play(y + 1, x)
                        done = True
                        break
                    if (x - 1) >= 0 and function_obj.board[y][x - 1] == 0:
                        hplay = True
                        play(y, x - 1)
                        done = True
                        break
                    if (x + 1) < function_obj.size and function_obj.board[y][x + 1] == 0:
                        hplay = True
                        play(y, x + 1)
                        done = True
                        break
                x += 1
            if done == True:
                break
            y += 1

def create_map(size):
    board = [[0 for x in range(size)] for x in range(size)]
    return board


def ia_turn(board, pos_x, pos_y):
    if pos_x == -1 and pos_y == -1:
        pass
    ia_algo_def(board)


class Mandatory:

    def __init__(self):
        self.size = 19
        self.board = [[]]

    def start(self, size):
        self.size = size
        self.board = create_map(self.size)
        print("OK")
        sys.stdout.flush()

    def turn(self, pos_x, pos_y):
        if not self.board[0]:
            self.board = create_map(self.size)
        if pos_x < self.size and pos_y < self.size and self.board[pos_x][pos_y] != 0:
            print('ERROR - move not allowed !')
            sys.stdout.flush()
        else:
            self.board[pos_x][pos_y] = 2
            ia_turn(self.board, pos_x, pos_y)

    def begin(self):
        if not self.board[0]:
            self.board = create_map(self.size)
        ia_turn(self.board, -1, -1)

    def board(self):
        pass

    def info(self):
        pass

    def end(self):
        pass

    def about(self):
        print('name="pbrain-STRASBOURG-Marchal.Jonathan", version="1.0", author="Pitou & marcha_5", country="FR"')
        sys.stdout.flush()

    def restart(self):
        self.board = create_map(self.size)
        print('OK')
        sys.stdout.flush()

    function_list = [start, turn, begin, board, info, end, about, restart]


function_obj = Mandatory()
