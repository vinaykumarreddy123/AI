class EightQueens:
    def __init__(self):
        self.board = [[0] * 8 for _ in range(8)]
        self.solutions = []

    def solve(self):
        self.place_queen(0)
        return self.solutions

    def place_queen(self, col):
        if col >= 8:
            self.solutions.append([row[:] for row in self.board])
            return

        for row in range(8):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.place_queen(col + 1)
                self.board[row][col] = 0

    def is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

def print_solution(solution):
    for row in solution:
        print(" ".join("Q" if cell == 1 else "-" for cell in row))
    print()

if __name__ == "__main__":
    solver = EightQueens()
    solutions = solver.solve()
    
    print("Number of solutions:", len(solutions))
    print("One of the solutions:")
    print_solution(solutions[0])
