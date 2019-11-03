#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import sys
import pprint

class Position:
    def __init__(self, x, y, z):
        this.x = x;
        this.y = y;
        this.z = z;

class Board:
    def __init__(self):
    	self.board = [[[None for x in range(4)] for y in range(4)] for z in range(4)]
        self.x_positions = []
        self.y_positions = []

    def print_board(self):
    	pprint.pprint(self.board)


#sums up rewards of making a move in a position on the board
def find_rewards(board, player, position):
    reward_sum = 0;
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

trialsCount = [sys.argv[1], sys.argv[2], sys.argv[3]];

