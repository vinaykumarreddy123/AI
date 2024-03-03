import sys

def tsp(graph):
    num_cities = len(graph)
    # Initialize memoization table
    memo = [[None] * num_cities for _ in range(2**num_cities)]

    # Helper function to solve TSP using dynamic programming
    def tsp_helper(curr, visited):
        if visited == (1 << num_cities) - 1:
            return graph[curr][0]  # Return to the start city

        if memo[visited][curr] is not None:
            return memo[visited][curr]

        min_cost = sys.maxsize

        for next_city in range(num_cities):
            if not visited & (1 << next_city):
                cost = graph[curr][next_city] + tsp_helper(next_city, visited | (1 << next_city))
                min_cost = min(min_cost, cost)

        memo[visited][curr] = min_cost
        return min_cost

    # Start from the first city
    return tsp_helper(0, 1 << 0)

# Example usage:
if __name__ == "__main__":
    # Example graph represented as an adjacency matrix
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    min_cost = tsp(graph)
    print("Minimum cost for TSP:", min_cost)
