from state import State

def main():
	b = []
	with open("input.txt") as puzzle:
		for row in puzzle:
			b.append(list(map(int, row.strip().split())))
	start = State(board=b)
	solved_state = solve_board(start=start)
	if solved_state == None:
		print("Puzzle is unsolvable")
		return 1
	
	print(solved_state.board)

	return 0

def solve_board(start: State):
	if start.solved:
		return start

	start.get_next_states()
	for state in start.next_states:
		try:
			final_state: State = solve_board(start=state)
			if final_state != None:
				return final_state
		except KeyboardInterrupt:
			print(state.board)
			print(state.board.possible_moves)
	
	return None # Board is unsolvable

main()