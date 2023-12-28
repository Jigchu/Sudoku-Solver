class State:
	def __init__(self, board: list[list[int]]):
		self.board = board
		self.size = 9
		self.next_moves = self.get_next_moves()
		self.invalid = not self.is_valid()
		self.solved = len(self.next_moves) == 0 
	
	def fill_cell(self, location: tuple[int, int], number: int):
		self.board[location[0]][location[1]] = number

	def fill(self):
		unfilled = []
		for cell, moves in self.next_moves.items():
			if len(moves) == 1:
				self.fill_cell(cell, moves[0])
			else:
				unfilled.append(cell)
		return unfilled

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