#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import sys
import random
import pprint

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Board:
    def __init__(self):
    	self.board = [[[None for x in range(4)] for y in range(4)] for z in range(4)]
        self.x_positions = []
        self.o_positions = []

    def print_board(self):
    	pprint.pprint(self.board)

def print_floats(board):

    string = ""
    for z in range(4):
        level_count = 'Level: ' + str(z)
        print(level_count)
        for y in range(4):
            string += '[ ' + str(board.board[0][y][z]) + ', ' + str(board.board[1][y][z]) + ', ' + str(board.board[2][y][z]) + ', ' + str(board.board[2][y][z]) + ']'
            print("[ %1.3f, %1.3f, %1.3f, %1.3f ]" % (board.board[0][y][z], board.board[1][y][z], board.board[2][y][z], board.board[3][y][z]))
            string = ""

#sums up rewards of making a move in a position on the board
def find_rewards(board, player, position):
    reward_sum = 0
    player_positions = []
    opp_positions = []
    if player is "X":
        player_positions = board.x_positions
        opp_positions = board.o_positions
    else:
        player_positions = board.o_positions
        opp_positions = board.x_positions

    for current_positions in player_positions:
        if current_positions.x == position.x:
            reward_sum += 1
        if current_positions.y == position.y:
            reward_sum += 1
        if current_positions.z == position.z:
            reward_sum += 1

    for current_positions in opp_positions:
        if current_positions.x == position.x:
            reward_sum += 2
        if current_positions.y == position.y:
            reward_sum += 2
        if current_positions.z == position.z:
            reward_sum += 2

    return reward_sum

def find_terminal(board, player):
    #find across rows
    assumption = True
    for z in range(4):
        for y in range(4):
            assumption = True
            for x in range(4):
                if board.board[x][y][z] != player:
                    assumption = False
            if assumption:
                return True

    #find across columns
    for z in range(4):
        for x in range(4):
            assumption = True
            for y in range(4):
                if board.board[x][y][z] != player:
                    assumption = False
            if assumption:
                return True


    #find across verticals
    assumption = True
    for x in range(4):
        for y in range(4):
            assumption = True
            for z in range(4):
                if board.board[x][y][z] != player:
                    assumption = False
            if assumption:
                return True


    #find across 2D diagonals
    assumption = True
    for z in range(4):
        assumption = True
        for x in range(4):
            if board.board[x][x][z] != player:
                assumption = False
        if assumption:
            return True

    assumption = True
    for z in range(4):
        assumption = True
        for x in range(4):
            if board.board[3-x][x][z] != player:
                assumption = False
        if assumption:
            return True

    #find across 3D diagonals
    assumption = True
    for x in range(4):
        if board.board[x][x][x] != player:
            assumption = False
    if assumption:
        return True

    assumption = True
    for x in range(4):
        if board.board[x][x][3-x] != player:
            assumption = False
    if assumption:
        return True

    assumption = True
    for x in range(4):
        if board.board[x][3-x][x] != player:
            assumption = False
    if assumption:
        return True

    assumption = True
    for x in range (4):
        if board.board[x][3-x][3-x] != player:
            assumption = False
    if assumption:
        return True

    assumption = True
    for x in range (4):
        for y in range (4):
            for z in range(4):
                if board.board[z][y][x] is None:
                    assumption = False
    if assumption:
        return True

    #return false if none of the above cases were true
    return False

def find_max_reward(board, player):
    position = Position(0, 0, 0)
    current_max_reward = 0
    for z in range (4):
        for y in range(4):
            for x in range(4):
                if board.board[x][y][z] is None:
                    current_position = Position(x, y, z)
                    if find_rewards(board, player, current_position) > current_max_reward:
                        current_max_reward = find_rewards(board, player, current_position)
                        position = current_position
    return position

def find_max_q(board, player):
    position = Position(0, 0, 0)
    current_max_q = 0
    for z in range (4):
        for y in range(4):
            for x in range(4):
                if board.board[x][y][z] is None:
                    current_position = Position(x, y, z)
                    if q_count.board[x][y][z] >= current_max_q:
                        current_max_q = q_count.board[x][y][z]
                        position = current_position
    return position

def set_num_tables(board):
    for z in range (4):
        for y in range(4):
            for x in range(4):
                board.board[x][y][z] = 0

def random_selector(board, position, alpha):
    rand = random.random()
    if (rand > alpha):
        return position
    else:
        x = random.randint(0,3)
        y = random.randint(0,3)
        z = random.randint(0,3)
        if board.board[x][y][z] is None:
            return Position(x,y,z)
        else:
            return random_selector(board, position, alpha)

trialsCount = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]

#counts of rewards for each position and times position is reached
q_count = Board()
n_count = Board()
set_num_tables(q_count)
set_num_tables(n_count)

alpha = .7
discount = .2
for trials in range(trialsCount[2]):
    if trials == trialsCount[0] or trials == trialsCount[1]:
        print_floats(q_count)
        board.print_board()
        print("eat this")
    board = Board()
    player_1 = "X"
    player_2 = "O"
    last_pos_X = Position(None, None, None)
    last_pos_O = Position(None, None, None)
    while not find_terminal(board, "X") or not find_terminal(board, "O"):
        for z in range (4):
            for y in range(4):
                for x in range(4):
                    if board.board[x][y][z] is None:
                        position = Position(x,y,z)
                        max_q_prime = find_max_reward(board, "X")
                        max_q_prime_val = q_count.board[max_q_prime.x][max_q_prime.y][max_q_prime.z]
                        n_count.board[x][y][z] = n_count.board[x][y][z] + 1

                        prev_q = 0
                        if last_pos_X.x is not None:
                            prev_q = q_count.board[last_pos_X.x][last_pos_X.y][last_pos_X.z]

                        q_count.board[x][y][z] = (1 - alpha) *  q_count.board[x][y][z] + alpha * (find_rewards(board, "X", position) + discount * max_q_prime_val - prev_q)

        set_position_X = random_selector(board, find_max_q(board, "X"), alpha)
        board.board[set_position_X.x][set_position_X.y][set_position_X.z] = "X"
        board.x_positions.append(set_position_X)
        last_pos_X = set_position_X

        if find_terminal(board, "X") or find_terminal(board, "O"):
            break

        for z in range (4):
            for y in range(4):
                for x in range(4):
                    if board.board[x][y][z] is None:
                        position = Position(x,y,z)
                        max_q_prime = find_max_reward(board, "O")
                        max_q_prime_val = q_count.board[max_q_prime.x][max_q_prime.y][max_q_prime.z]
                        n_count.board[x][y][z] = n_count.board[x][y][z] + 1

                        prev_q = 0
                        if last_pos_O.x is not None:
                            prev_q = q_count.board[last_pos_O.x][last_pos_O.y][last_pos_O.z]

                        q_count.board[x][y][z] = (1 - alpha) *  q_count.board[x][y][z] + alpha * (find_rewards(board, "O", position) + discount * max_q_prime_val - prev_q)

        set_position_O = random_selector(board, find_max_q(board, "O"), alpha)
        board.board[set_position_O.x][set_position_O.y][set_position_O.z] = "O"
        board.o_positions.append(set_position_O)
        last_pos_O = set_position_O
    alpha = alpha / (1 + .01)
    trials_counter = str(trials) + '/' + str(trialsCount[2])
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)
    print(trials_counter)
print_floats(q_count)
board.print_board()

