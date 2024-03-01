class State:
    def __init__(self, missionaries, cannibals, boat_position):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat_position = boat_position

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries > 0 and self.missionaries < self.cannibals:
            return False
        if self.missionaries < 3 and (3 - self.missionaries) < (3 - self.cannibals):
            return False
        return True

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat_position == other.boat_position

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat_position))

    def __str__(self):
        return f"({self.missionaries}, {self.cannibals}, {'left' if self.boat_position == 0 else 'right'})"


class MissionariesCannibals:
    def __init__(self):
        self.initial_state = State(3, 3, 0)
        self.goal_state = State(0, 0, 1)

    def solve(self):
        if not self.initial_state.is_valid() or not self.goal_state.is_valid():
            return "No solution possible. Invalid initial or goal state."
        
        visited = set()
        frontier = [(self.initial_state, [])]

        while frontier:
            current_state, path = frontier.pop(0)
            if current_state == self.goal_state:
                return path + [current_state]
            visited.add(current_state)
            
            for successor, action in self.successors(current_state):
                if successor not in visited:
                    frontier.append((successor, path + [current_state]))

        return "No solution found."

    def successors(self, state):
        successors = []
        if state.boat_position == 0:  # Boat on the left side
            for m in range(3):
                for c in range(3):
                    if 1 <= m + c <= 2:
                        new_state = State(state.missionaries - m, state.cannibals - c, 1)
                        if new_state.is_valid():
                            successors.append((new_state, f"Move {m} missionaries and {c} cannibals to the right"))
        else:  # Boat on the right side
            for m in range(3):
                for c in range(3):
                    if 1 <= m + c <= 2:
                        new_state = State(state.missionaries + m, state.cannibals + c, 0)
                        if new_state.is_valid():
                            successors.append((new_state, f"Move {m} missionaries and {c} cannibals to the left"))
        return successors


def print_solution(solution):
    if isinstance(solution, str):
        print(solution)
    else:
        print("Solution Steps:")
        for i, state in enumerate(solution):
            print(f"Step {i + 1}: {state}")


if __name__ == "__main__":
    problem = MissionariesCannibals()
    solution = problem.solve()
    print_solution(solution)
