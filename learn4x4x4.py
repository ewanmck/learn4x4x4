#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import sys
import random
import pprint

#used for console log
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

#class definition for postion object
class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

#class definition for board objects used for games and q table
class Board:
    def __init__(self):
    	self.board = [[[None for x in range(4)] for y in range(4)] for z in range(4)]
        self.x_positions = []
        self.o_positions = []

    def print_board(self):
    	pprint.pprint(self.board)

#function used to print a properly formated q table
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

    #variables used to change weights of offensive vs defensive play
    offensive = 1
    defensive = 2

    if player is "X":
        player_positions = board.x_positions
        opp_positions = board.o_positions
    else:
        player_positions = board.o_positions
        opp_positions = board.x_positions

    for current_position in player_positions:
        if current_position.x == position.x and current_position.y == position.y:
            reward_sum += offensive
        if current_position.x == position.x and current_position.z == position.z:
            reward_sum += offensive
        if current_position.y == position.y and current_position.z == position.z:
            reward_sum += offensive

    for current_position in opp_positions:
        if current_position.x == position.x and current_position.y == position.y:
            reward_sum += defensive
        if current_position.x == position.x and current_position.z == position.z:
            reward_sum += defensive
        if current_position.y == position.y and current_position.z == position.z:
            reward_sum += defensive

    return reward_sum

#used to find terminal state of a board
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

#finds the position containing the maximum reward given a current board state
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

#finds the max q value in the current table
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

#used to initialize q table with 0's
def set_num_tables(board):
    for z in range (4):
        for y in range(4):
            for x in range(4):
                board.board[x][y][z] = 0

#randomly selects a position given a acceptence rate, the board, and current position
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

#take in trial counts as arguments
trialsCount = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]

#initialize table for q counts
q_count = Board()
set_num_tables(q_count)

#parameters for alpha, discount, and exploration rates
alpha = .7
exploration_rate = .7
discount = .2

#loop until the highest trial count is reached
#loops through games to update values in the q table to aid learning process
for trials in range(trialsCount[2]):
    #print out the q table at each argument given
    if trials == trialsCount[0] or trials == trialsCount[1]:
        print_floats(q_count)
        #used to make the trial counter work
        print("eat this")

    #initialize board state and important parameters prior to game start
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

                        #variables set to shorten formulas
                        position = Position(x,y,z)
                        max_q_prime = find_max_reward(board, "X")
                        max_q_prime_val = q_count.board[max_q_prime.x][max_q_prime.y][max_q_prime.z]

                        #set previous q if it exists
                        prev_q = 0
                        if last_pos_X.x is not None:
                            prev_q = q_count.board[last_pos_X.x][last_pos_X.y][last_pos_X.z]

                        #q count set for the current board position given board state
                        q_count.board[x][y][z] = (1 - alpha) *  q_count.board[x][y][z] + alpha * (find_rewards(board, "X", position) + discount * max_q_prime_val - prev_q)

        #position selected given max q and exploration rate, then set in board and added to list
        set_position_X = random_selector(board, find_max_q(board, "X"), exploration_rate)
        board.board[set_position_X.x][set_position_X.y][set_position_X.z] = "X"
        board.x_positions.append(set_position_X)
        last_pos_X = set_position_X

        if find_terminal(board, "X") or find_terminal(board, "O"):
            break

        #same formula as above used for the opponent
        for z in range (4):
            for y in range(4):
                for x in range(4):
                    if board.board[x][y][z] is None:
                        position = Position(x,y,z)
                        max_q_prime = find_max_reward(board, "O")
                        max_q_prime_val = q_count.board[max_q_prime.x][max_q_prime.y][max_q_prime.z]

                        prev_q = 0
                        if last_pos_O.x is not None:
                            prev_q = q_count.board[last_pos_O.x][last_pos_O.y][last_pos_O.z]

                        q_count.board[x][y][z] = (1 - alpha) *  q_count.board[x][y][z] + alpha * (find_rewards(board, "O", position) + discount * max_q_prime_val - prev_q)

        set_position_O = random_selector(board, find_max_q(board, "O"), exploration_rate)
        board.board[set_position_O.x][set_position_O.y][set_position_O.z] = "O"
        board.o_positions.append(set_position_O)
        last_pos_O = set_position_O

    #exploration rate lowered as trials increase
    exploration_rate = exploration_rate / (1 + .01)

    #trials counter printed
    trials_counter = str(trials) + '/' + str(trialsCount[2])
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)
    print(trials_counter)

#prints q count at the end of loop
print_floats(q_count)

