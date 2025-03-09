def n_queens_solver(board_size):
    def is_position_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, board_size), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def explore_solutions(board, col):
        if col >= board_size:
            solutions.append([row.index(1) for row in board])
            return
        
        for row in range(board_size):
            if is_position_safe(board, row, col):
                board[row][col] = 1
                explore_solutions(board, col + 1)
                board[row][col] = 0

    board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    solutions = []
    explore_solutions(board, 0)
    return solutions

def show_solutions(solutions, board_size):
    for solution in solutions:
        board = [['.' for _ in range(board_size)] for _ in range(board_size)]
        for row, col in enumerate(solution):
            board[row][col] = 'Q'
        for row in board:
            print(' '.join(row))
        print()

def count_solutions(board_size):
    def is_safe(queens, row, col):
        for r, c in enumerate(queens):
            if c == col or r + c == row + col or r - c == row - col:
                return False
        return True
    
    def explore_count(queens, row):
        if row == board_size:
            return 1
        count = 0
        for col in range(board_size):
            if is_safe(queens, row, col):
                queens[row] = col
                count += explore_count(queens, row + 1)
                queens[row] = -1
        return count
    
    return explore_count([-1] * board_size, 0)

def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt).strip())
            if num > 0:
                return num
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Enter a valid integer.")

if __name__ == "__main__":
    size = get_positive_integer("Enter the chessboard size (N): ")
    choice = input("Do you want to see a solution (S), count solutions (C), or both (B)? ").strip().upper()
    
    if choice in ['S', 'B']:
        solutions_list = n_queens_solver(size)
        if solutions_list:
            print(f"\nTotal possible arrangements for {size}-Queens: {len(solutions_list)}")
            show_solutions(solutions_list, size)
        else:
            print(f"No solution exists for {size}-Queens problem.")
    
    if choice in ['C', 'B']:
        total_solutions = count_solutions(size)
        print(f"\nNumber of solutions for {size}-Queens problem: {total_solutions}")
