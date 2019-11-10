#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import sys
import pprint

class Position:
    def __init__(self, x, y, z):
        this.x = x
        this.y = y
        this.z = z

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
    else
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
    for z in range(4):
        for y in range(4):
            for x in range(4):
                assumption = True
                if board.board[x][y][z] != player:
                    assumption = False
                if assumption
                    return True


    #find across columns
    for z in range(4):
        for x in range(4):
            for y in range(4):
                assumption = True
                if board.board[x][y][z] != player:
                    assumption = False
                if assumption:
                    return True

    #find across verticals
    for x in range(4):
        for y in range(4):
            for z in range(4):
                assumption = True
                if board.board[x][y][z] != player:
                    assumption = False
                if assumption:
                    return True

    #find across 2D diagonals
    for z in range(4):
        for x in range(4):
            assumption = True
            if board.board[x][x][z] != player:
                assumption = False
            if assumption:
                return True
        for x in range(4):
            assumption = True
            if board.board[4-x][x][z] != player:
                assumption = False
            if assumption:
                return True

    #find across 3D diagonals
    for x in range(4):
        assumption = True
        if board.board[x][x][x] != player
            assumption = False
        if assumption:
            return True

    for x in range(4):
        assumption = True
        if board.board[x][x][4-x] != player
            assumption = False
        if assumption:
            return True

    for x in range(4):
        assumption = True
        if board.board[x][4-x][x] != player
            assumption = False
        if assumption:
            return True

    for x in range (4):
        assumption = True
        if board.board[x][4-x][4-x] != player
            assumption = False
        if assumption:
            return True

    #return false if none of the above cases were true
    return False

def find_max_reward(board, player):
    position = Position(None, None, None)
    current_max_reward = 0
    for z in range (4):
        for y in range(4):
            for x in range(4):
                if board[x][y][z] is player:
                    current_position = Position(x, y, z)
                    if find_rewards(board, player, current_position) > current_max_reward:
                        current_max_reward = find_rewards(board, player, current_position)
                        position.x = x
                        position.y = y
                        position.z = z
    return position

def find_max_q(board, player):
    position = Position(None, None, None)
    current_max_q = 0
    for z in range (4):
        for y in range(4):
            for x in range(4):
                if board[x][y][z] is player:
                    current_position = Position(x, y, z)
                    if q_count[x][y][z] > current_max_q:
                        current_max_q = q_count[x][y][z]
                        position.x = x
                        position.y = y
                        position.z = z
    return position


trialsCount = [sys.argv[1], sys.argv[2], sys.argv[3]]

#counts of rewards for each position and times position is reached
q_count = Board()
n_count = Board()
alpha = .7
discount = .7
for x in range(trialsCount[2]):
    if x = trialsCount[0] or x = trialsCount[1] or x = trialsCount[2]:
        q_count.print()
    board = Board()
    player_1 = "X"
    player_2 = "O"
    while not find_terminal(board, "X") or not find_terminal(board, "O"):
        for z in range (4):
            for y in range(4):
                for x in range(4):
                    if board[x][y][z] not None:
                        position = Position(x,y,z)
                        max_q_prime = find_max_rewards(board, "X")
                        q_count[x][y][z] = q_count[x][y][z] + alpha * n_count[x][y][z] * (find_rewards(board, "X", position) + discount * q_count[max_q_prime.x][max_q_prime.y][max_q_prime.z] - q_count[x][y][z])
        set_position_X = find_max_q(board, "X")
        board[set_position_X.x][set_position_X.y][set_position_X.z] = "X"
        if find_terminal(board, "X") or find_terminal(board, "O"):
            break
        for z in range (4):
            for y in range(4):
                for x in range(4):
                    if board[x][y][z] not None:
                        position = Position(x,y,z)
                        max_q_prime = find_max_rewards(board, "O")
                        q_count[x][y][z] = q_count[x][y][z] + alpha * n_count[x][y][z] * (find_rewards(board, "O", position) + discount * q_count[max_q_prime.x][max_q_prime.y][max_q_prime.z] - q_count[x][y][z])
        set_position_O = find_max_q(board, "O")
        board[set_position_O.x][set_position_O.y][set_position_O.z] = "O"

q_count.print()
