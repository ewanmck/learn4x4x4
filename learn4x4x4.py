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
                assumption = true
                if board.board[x][y][z] != player:
                    assumption = false
                if assumption
                    return true


    #find across columns
    for z in range(4):
        for x in range(4):
            for y in range(4):
                assumption = true
                if board.board[x][y][z] != player:
                    assumption = false
                if assumption:
                    return true

    #find across verticals
    for x in range(4):
        for y in range(4):
            for z in range(4):
                assumption = true
                if board.board[x][y][z] != player:
                    assumption = false
                if assumption:
                    return true

    #find across 2D diagonals
    for z in range(4):
        for x in range(4):
            assumption = true
            if board.board[x][x][z] != player:
                assumption = false
            if assumption:
                return true
        for x in range(4):
            assumption = true
            if board.board[4-x][x][z] != player:
                assumption = false
            if assumption:
                return true

    #find across 3D diagonals
    for x in range(4):
        assumption = true
        if board.board[x][x][x] != player
            assumption = false
        if assumption:
            return true

    for x in range(4):
        assumption = true
        if board.board[x][x][4-x] != player
            assumption = false
        if assumption:
            return true

    for x in range(4):
        assumption = true
        if board.board[x][4-x][x] != player
            assumption = false
        if assumption:
            return true

    for x in range (4):
        assumption = true
        if board.board[x][4-x][4-x] != player
            assumption = false
        if assumption:
            return true

    #return false if none of the above cases were true
    return false


trialsCount = [sys.argv[1], sys.argv[2], sys.argv[3]]

