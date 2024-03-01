class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target_amount):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target_amount = target_amount
        self.visited_states = set()
        self.solution_steps = []

    def solve(self):
        self.dfs(0, 0)

    def dfs(self, jug1_amount, jug2_amount):
        if jug1_amount == self.target_amount or jug2_amount == self.target_amount:
            self.solution_steps.append((jug1_amount, jug2_amount))
            return True

        if (jug1_amount, jug2_amount) in self.visited_states:
            return False

        self.visited_states.add((jug1_amount, jug2_amount))

        # Fill jug1
        if jug1_amount < self.jug1_capacity:
            if self.dfs(self.jug1_capacity, jug2_amount):
                self.solution_steps.append((self.jug1_capacity, jug2_amount))
                return True

        # Fill jug2
        if jug2_amount < self.jug2_capacity:
            if self.dfs(jug1_amount, self.jug2_capacity):
                self.solution_steps.append((jug1_amount, self.jug2_capacity))
                return True

        # Empty jug1
        if jug1_amount > 0:
            if self.dfs(0, jug2_amount):
                self.solution_steps.append((0, jug2_amount))
                return True

        # Empty jug2
        if jug2_amount > 0:
            if self.dfs(jug1_amount, 0):
                self.solution_steps.append((jug1_amount, 0))
                return True

        # Pour from jug1 to jug2
        pour_amount = min(jug1_amount, self.jug2_capacity - jug2_amount)
        if pour_amount > 0:
            if self.dfs(jug1_amount - pour_amount, jug2_amount + pour_amount):
                self.solution_steps.append((jug1_amount - pour_amount, jug2_amount + pour_amount))
                return True

        # Pour from jug2 to jug1
        pour_amount = min(jug2_amount, self.jug1_capacity - jug1_amount)
        if pour_amount > 0:
            if self.dfs(jug1_amount + pour_amount, jug2_amount - pour_amount):
                self.solution_steps.append((jug1_amount + pour_amount, jug2_amount - pour_amount))
                return True

        return False

    def print_solution(self):
        if not self.solution_steps:
            print("No solution found.")
        else:
            print("Solution Steps:")
            for step in self.solution_steps:
                print("Jug 1:", step[0], "  Jug 2:", step[1])

if __name__ == "__main__":
    jug1_capacity = int(input("Enter capacity of jug 1: "))
    jug2_capacity = int(input("Enter capacity of jug 2: "))
    target_amount = int(input("Enter target amount: "))

    problem = WaterJugProblem(jug1_capacity, jug2_capacity, target_amount)
    problem.solve()
    problem.print_solution()
