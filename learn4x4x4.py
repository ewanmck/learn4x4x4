#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import sys
import pprint

#class Tile:
#	def __init__(self, state):
#		self.state = state;
#	
#	def get_state(self):
#		return self.state
#	
#	def set_state(self, newState):
#		self.state = newState

class Board:
	def __init__(self):
		self.board = [[[None for x in range(4)] for y in range(4)] for z in range(4)]				

	def print_board(self):
		pprint.pprint(self.board)
		

trialsCount = [sys.argv[1], sys.argv[2], sys.argv[3]];

# for x in trialsCount:
#	print(x)

# testTile = Tile("X")
# print(testTile.state)
# testTile.set_state("O")
# print(testTile.state)
# testTile2 = Tile(None)
# print(testTile2.state)
testBoard = Board()
testBoard.print_board()
