class Board:
	def __init__(self, board: list[list[int]]):
		self.board = board
		self.size = 9 # May make variable size boards
		self.possible_moves = self.get_possible_moves()

	def enter_number(self, position: tuple[int, int], number: int):
		new_board = []
		for r in self.board:
			new_board.append(r[:])
		new_board[position[0]][position[1]] = number
		return new_board
	
	def __str__(self):
		output_string = ""
		for row in self.board:
			for i in row:
				output_string += f"{i} "
			output_string += "\n"
		return output_string

	def get_possible_moves(self):
		possible_moves = {}
		blank_cells = self.get_blank_cells()
		
		for cell in blank_cells:
			moves = [i for i in range(1, 10)]
			for i in self.board[cell[0]]:				# Checks row
				if i != 0:
					try:
						moves.remove(i)
					except ValueError:
						pass
			for row in self.board:						# Checks column
				if row[cell[1]] != 0:
					try:
						moves.remove(row[cell[1]])
					except ValueError:
						pass
			grid_location = self.grid_location(cell)	# Checks closest 3x3 grid
			for x_offset in range(3):
				new_x = grid_location[0] + x_offset
				for y_offset in range(3):
					new_y = grid_location[1] + y_offset
					if self.board[new_x][new_y] != 0:
						try:
							moves.remove(self.board[new_x][new_y])
						except ValueError:
							pass
			possible_moves[cell] = moves
			
		return possible_moves

	def grid_location(self, position: tuple[int, int]):
		grid_location = [0, 0]
		num_of_grids = self.size // 3
		
		for i in range(num_of_grids):
			curr_grid_pos = self.size - (3 * (i+1))
			if position[0] >= curr_grid_pos:
				grid_location[0] = curr_grid_pos
				break

		for i in range(num_of_grids):
			curr_grid_pos = self.size - (3 * (i+1))
			if position[1] >= curr_grid_pos:
				grid_location[1] = curr_grid_pos
				break

		return tuple(grid_location)

	def get_blank_cells(self):
		blank_coords = []

		for row in range(self.size):
			for column in range(self.size):
				if self.board[row][column] == 0:
					blank_coords.append((row, column))
		
		return blank_coords