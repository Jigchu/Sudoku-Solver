from state import State

def main():
	board = []
	with open("input.txt") as puzzle:
		for row in puzzle:
			row = list(map(int, row.strip().split()))
			board.append(row)

	start = State(board=board)
	start.fill()
	print(start.board)
	return 0

main()