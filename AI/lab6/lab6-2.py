def is_safe(board, row, col, n):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    # Base case: If all queens are placed, return True
    if col >= n:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place the queen
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_n_queens_util(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove the queen (Backtrack)
            board[i][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join(["[Q]" if cell == 1 else "[.]" for cell in row]))

def main():
    n = 8
    # Initialize an 8x8 chessboard with 0s
    board = [[0 for _ in range(n)] for _ in range(n)]

    print(f"--- N-Queens Solver ({n}x{n} Board) ---")
    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
        return

    print("\nFound Solution:")
    print_board(board)

if __name__ == "__main__":
    main()