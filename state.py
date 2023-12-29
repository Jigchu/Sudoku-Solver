from __future__ import annotations

class State:
	def __init__(self, board: list[list[int]]):
		self.board = board
		self.size = 9
		self.init_instance()
	
	def init_instance(self):
		self.next_moves = self.get_next_moves()
		self.invalid = not self.is_valid()
		self.solved = len(self.next_moves) == 0 

	def fill_cell(self, location: tuple[int, int], number: int):
		self.board[location[0]][location[1]] = number
		self.init_instance()
	
	def clear_cell(self, location: tuple[int, int]):
		self.board[location[0]][location[1]] = 0
		self.init_instance()

	def autofill(self):
		filled = []
		for cell, moves in self.next_moves.items():
			if len(moves) == 1:
				self.fill_cell(cell, moves[0])
				filled.append(cell)
		self.init_instance()
		return filled

	def blank_cells(self):
		locations = []
		for x, row in enumerate(self.board):
			for y, number in enumerate(row):
				if number == 0:
					locations.append((x, y))
		return locations

	def get_next_moves(self):
		next_moves = {}
		blank_cells = self.blank_cells()
		for cell in blank_cells:
			moves = [i for i in range(1, 10)]
			for number in self.board[cell[0]]:			# Check row
				try:
					moves.remove(number)
				except ValueError:
					pass
			for i in range(len(self.board)):			# Check column
				try:
					moves.remove(self.board[i][cell[1]])
				except ValueError:
					pass
			grid_x = (cell[0] // 3) * 3					# Check 3x3 grid
			grid_y = (cell[1] // 3) * 3
			for x in range(grid_x, grid_x+3):
				for y in range(grid_y, grid_y+3):
					try:
						moves.remove(self.board[x][y])
					except ValueError:
						pass
			next_moves[cell] = moves

		return next_moves
	
	def is_valid(self):
		x_moves = [[i for i in range(1, 10)] for j in range(self.size)]
		y_moves = [[i for i in range(1, 10)] for j in range(self.size)]
		grid_moves = [[i for i in range(1, 10)] for j in range((self.size//3)**2)]

		for x, row in enumerate(self.board):
			for y, number in enumerate(row):
				if number != 0:
					try:
						x_moves[x].remove(number)
						y_moves[y].remove(number)
						grid_x = (x // 3) * 3
						grid_y = (y // 3)
						grid_moves[grid_x+grid_y].remove(number) 		# Works wtf am I doing?
					except ValueError:
						return False
		
		return True

	@classmethod
	def compare(cls, s1: State, s2: State):
		difference = []
		for x in range(s1.size):
			for y in range(s1.size):
				if s1.board[x][y] != s2.board[x][y]:
					difference.append((x, y))
		return difference