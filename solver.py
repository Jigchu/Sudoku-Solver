from state import State

def main():
	board = []
	with open("input.txt") as puzzle:
		for row in puzzle:
			row = list(map(int, row.strip().split()))
			board.append(row)
	
	s = []
	with open("solution.txt") as solution:
		for row in solution:
			row = list(map(int, row.strip().split()))
			s.append(row)
	
	solved_state = State(board=s)
	start = State(board=board)

	if not solver(start):
		print("No Solutions")
		return 1
	
	for row in start.board:
		print(*row)

	print(State.compare(start, solved_state))

	return 0

def solver(start: State):
	if start.invalid:
		return False
	if start.solved:
		return True

	autofilled = start.autofill()
	if start.invalid:
		for cell in autofilled:
			start.clear_cell(cell)
			return False
	for cell, moves in start.next_moves.items():
		if len(moves) == 0:
			return False
		for move in moves:
			start.fill_cell(cell, move)
			if start.invalid:
				start.clear_cell(cell)
				continue
			if solver(start):
				return True
	
	return False

main()