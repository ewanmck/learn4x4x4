#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import sys
import pprint

class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Board:
    def __init__(self):
    	self.board = [[[None for x in range(4)] for y in range(4)] for z in range(4)]
        self.x_positions = []
        self.y_positions = []

    def print_board(self):
    	pprint.pprint(self.board)


#sums up rewards of making a move in a position on the board
def find_rewards(board, player, position):
    reward_sum = 0
    player_positions = []
    if player is "X":
        player_positions = board.x_positions
    else:
        player_positions = board.x_positions

    for current_positions in player_positions:
        if current_positions.x == position.x:
            reward_sum += 1
        if current_positions.y == position.y:
            reward_sum += 1
        if current_positions.z == position.z:
            reward_sum += 1

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


trialsCount = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]

#counts of rewards for each position and times position is reached
q_count = Board()
n_count = Board()
set_num_tables(q_count)
set_num_tables(n_count)

alpha = .7
discount = .7
for x in range(trialsCount[2]):
    if x is trialsCount[0] or x is trialsCount[1] or x is trialsCount[2]:
        q_count.print_board()
    board = Board()
    player_1 = "X"
    player_2 = "O"
    while not find_terminal(board, "X") or not find_terminal(board, "O"):
        for z in range (4):
            for y in range(4):
                for x in range(4):
                    if board.board[x][y][z] is None:
                        position = Position(x,y,z)
                        max_q_prime = find_max_reward(board, "X")
                        n_count.board[x][y][z] = n_count.board[x][y][z] + 1
                        q_count.board[x][y][z] = q_count.board[x][y][z] + alpha * n_count.board[x][y][z] * (find_rewards(board, "X", position) + discount * q_count.board[max_q_prime.x][max_q_prime.y][max_q_prime.z] - q_count.board[x][y][z])
        set_position_X = find_max_q(board, "X")
        board.board[set_position_X.x][set_position_X.y][set_position_X.z] = "X"
        q_count.print_board()
        if find_terminal(board, "X") or find_terminal(board, "O"):
            break
        for z in range (4):
            for y in range(4):
                for x in range(4):
                    if board.board[x][y][z] is None:
                        position = Position(x,y,z)
                        max_q_prime = find_max_reward(board, "O")
                        n_count.board[x][y][z] = n_count.board[x][y][z] + 1
                        q_count.board[x][y][z] = q_count.board[x][y][z] + alpha * n_count.board[x][y][z] * (find_rewards(board, "O", position) + discount * q_count.board[max_q_prime.x][max_q_prime.y][max_q_prime.z] - q_count.board[x][y][z])
        set_position_O = find_max_q(board, "O")
        board.board[set_position_O.x][set_position_O.y][set_position_O.z] = "O"
        q_count.print_board()
    board.print_board()
q_count.print_board()
