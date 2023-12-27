from board import Board

class State:
	def __init__(self, board: list[list[int]]):
		self.board: Board = Board(board=board)
		self.invalid = False
		self.solved = False
		self.evaluate()
		self.next_states = []	# Remember to call next states function later
	
	def evaluate(self):
		if len(self.board.possible_moves) == 0:
			self.solved = True
			return

		for blank_cell, possible_moves in self.board.possible_moves.items():
			if len(possible_moves) == 0:
				self.invalid = True
				return
		
		return

	def get_next_states(self):
		next_states: list[State] = []
		for blank_cell, possible_moves in self.board.possible_moves.items():
			for move in possible_moves:
				new_state = State(board=self.board.enter_number(blank_cell, move))
				if new_state.invalid:
					continue
				next_states.append(new_state)
		self.next_states = next_states[:]
		return next_states