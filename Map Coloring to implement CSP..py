class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, variable, assignment, value):
        for neighbor in self.constraints.get(variable, []):
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtracking_search(self):
        return self.backtrack({})

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, assignment, value):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result:
                    return result
                del assignment[var]
        return None

    def select_unassigned_variable(self, assignment):
        for var in self.variables:
            if var not in assignment:
                return var

    def order_domain_values(self, var, assignment):
        return self.domains[var]

# Example usage:
if __name__ == "__main__":
    variables = ['WA', 'NT', 'SA', 'QLD', 'NSW', 'VIC', 'TAS']
    domains = {var: ['Red', 'Green', 'Blue'] for var in variables}
    constraints = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'QLD'],
        'SA': ['WA', 'NT', 'QLD', 'NSW', 'VIC'],
        'QLD': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'QLD', 'VIC'],
        'VIC': ['SA', 'NSW', 'TAS'],
        'TAS': ['VIC']
    }

    csp = CSP(variables, domains, constraints)
    solution = csp.backtracking_search()

    if solution:
        print("Map Coloring Solution:")
        for state, color in solution.items():
            print(state, ":", color)
    else:
        print("No solution found.")
