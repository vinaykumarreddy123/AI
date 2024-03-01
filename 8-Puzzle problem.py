import heapq

class PuzzleState:
    def __init__(self, puzzle, parent=None, move=None):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __lt__(self, other):
        return (self.depth + self.heuristic()) < (other.depth + other.heuristic())

    def __hash__(self):
        return hash(str(self.puzzle))

    def __str__(self):
        return str(self.puzzle)

    def is_goal(self):
        return self.puzzle == ((1, 2, 3), (4, 5, 6), (7, 8, 0))

    def heuristic(self):
        # Manhattan distance heuristic
        h = 0
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] != 0:
                    x, y = divmod(self.puzzle[i][j] - 1, 3)
                    h += abs(i - x) + abs(j - y)
        return h

    def get_neighbors(self):
        neighbors = []
        zero_pos = [(i, j) for i in range(3) for j in range(3) if self.puzzle[i][j] == 0][0]
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in moves:
            new_x, new_y = zero_pos[0] + move[0], zero_pos[1] + move[1]
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_puzzle = [list(row) for row in self.puzzle]
                new_puzzle[zero_pos[0]][zero_pos[1]] = self.puzzle[new_x][new_y]
                new_puzzle[new_x][new_y] = 0
                neighbors.append(PuzzleState(tuple(map(tuple, new_puzzle)), self, move))
        return neighbors

def solve_puzzle(initial_state):
    frontier = []
    heapq.heappush(frontier, initial_state)
    explored = set()

    while frontier:
        current_state = heapq.heappop(frontier)
        if current_state.is_goal():
            path = []
            while current_state.parent:
                path.append(current_state.move)
                current_state = current_state.parent
            return path[::-1]
        
        explored.add(current_state)
        for neighbor in current_state.get_neighbors():
            if neighbor not in explored:
                heapq.heappush(frontier, neighbor)
    
    return None

if __name__ == "__main__":
    initial_puzzle = ((1, 2, 3), (4, 0, 5), (6, 7, 8))  # Example initial state
    initial_state = PuzzleState(initial_puzzle)
    solution = solve_puzzle(initial_state)
    if solution:
        print("Solution found! Steps to reach the goal state:")
        for step in solution:
            if step == (0, 1):
                print("Move blank tile right")
            elif step == (0, -1):
                print("Move blank tile left")
            elif step == (1, 0):
                print("Move blank tile down")
            elif step == (-1, 0):
                print("Move blank tile up")
    else:
        print("No solution found.")
