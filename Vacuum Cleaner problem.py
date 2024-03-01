class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.current_position = (0, 0)
        self.direction = "right"
        self.clean_count = 0

    def move(self):
        if self.direction == "right":
            self.current_position = (self.current_position[0], min(self.current_position[1] + 1, len(self.grid[0]) - 1))
        elif self.direction == "left":
            self.current_position = (self.current_position[0], max(self.current_position[1] - 1, 0))
        elif self.direction == "down":
            self.current_position = (min(self.current_position[0] + 1, len(self.grid) - 1), self.current_position[1])
        elif self.direction == "up":
            self.current_position = (max(self.current_position[0] - 1, 0), self.current_position[1])

    def clean(self):
        if self.grid[self.current_position[0]][self.current_position[1]] == "dirty":
            self.grid[self.current_position[0]][self.current_position[1]] = "clean"
            self.clean_count += 1

    def turn_right(self):
        if self.direction == "right":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "up"
        elif self.direction == "up":
            self.direction = "right"

    def turn_left(self):
        if self.direction == "right":
            self.direction = "up"
        elif self.direction == "down":
            self.direction = "right"
        elif self.direction == "left":
            self.direction = "down"
        elif self.direction == "up":
            self.direction = "left"

    def print_grid(self):
        for row in self.grid:
            print(row)
        print()

    def clean_all(self):
        while self.clean_count < sum(row.count("dirty") for row in self.grid):
            self.clean()
            self.move()
            self.turn_left()
            self.clean()
            self.move()
            self.turn_right()
        print("All cells are clean.")

if __name__ == "__main__":
    grid = [["dirty", "clean", "dirty", "dirty"],
            ["dirty", "clean", "clean", "dirty"],
            ["clean", "clean", "dirty", "clean"],
            ["clean", "dirty", "dirty", "clean"]]

    cleaner = VacuumCleaner(grid)
    print("Initial grid:")
    cleaner.print_grid()
    cleaner.clean_all()
    print("Final grid:")
    cleaner.print_grid()
