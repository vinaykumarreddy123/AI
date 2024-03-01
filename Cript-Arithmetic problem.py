def solve_cryptarithmetic(puzzle):
    words = puzzle.split()
    unique_letters = set("".join(words))
    if len(unique_letters) > 10:
        return "Invalid input: More than 10 unique letters."

    unique_letters = list(unique_letters)
    first_letters = set(word[0] for word in words)
    if len(first_letters) > 10:
        return "Invalid input: More than 10 words with different first letters."

    if len(unique_letters) > 10 - len(first_letters):
        return "Invalid input: Too many unique letters."

    # Generate permutations of digits for unique letters
    for perm in generate_permutations(range(10), len(unique_letters)):
        digit_map = {letter: digit for letter, digit in zip(unique_letters, perm)}
        if all(digit_map[word[0]] != 0 for word in words):
            if evaluate_expression(words, digit_map):
                return digit_map

    return "No solution found."

def generate_permutations(elements, length):
    if length == 0:
        yield []
    else:
        for element in elements:
            for permutation in generate_permutations(elements, length - 1):
                if element not in permutation:
                    yield [element] + permutation

def evaluate_expression(words, digit_map):
    values = [sum(digit_map[char] * 10 ** (len(word) - i - 1) for i, char in enumerate(word)) for word in words[:-1]]
    return sum(values[:-1]) == values[-1]

if __name__ == "__main__":
    puzzle = input("Enter the cryptarithmetic puzzle: ")
    solution = solve_cryptarithmetic(puzzle)
    if isinstance(solution, dict):
        print("Solution:")
        for letter, digit in sorted(solution.items()):
            print(f"{letter}: {digit}")
    else:
        print(solution)
