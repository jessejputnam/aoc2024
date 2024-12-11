from lib import get_input


class Device:
    def __init__(self, data: str):
        # instance vars
        self.map: list[str] = data.split("\n")[:-1]
        self.visited: set = set()
        self.guard: list[int] = [-1, -1]
        self.facing: int = 0

        # static vars
        self.dirs = ["^", ">", "v", "<"]
        self.key: dict[str, list[int]] = {
            "^": [-1, 0],
            ">": [0, 1],
            "v": [1, 0],
            "<": [0, -1],
        }
        self.y_max = len(self.map)
        self.x_max = len(self.map[0])

        # initialize guard
        for idx, row in enumerate(self.map):
            if "^" in row:
                self.guard[0] = idx
                self.guard[1] = row.index("^")

    def print_guard(self) -> None:
        print(self.guard)

    def move_guard(self) -> None:
        move = self.key[self.dirs[self.facing]]
        self.guard = [sum(x) for x in zip(self.guard, move)]

    def turn_guard(self) -> None:
        self.facing = self.facing + 1 if self.facing < 3 else 0

    def mark_cell(self) -> None:
        self.visited.add(f"{self.guard[0]},{self.guard[1]}")

    def get_next_cell(self) -> int:
        move = self.key[self.dirs[self.facing]]
        cell_idx = [sum(x) for x in zip(self.guard, move)]
        if -1 in cell_idx or cell_idx[0] >= self.y_max or cell_idx[1] >= self.x_max:
            return -1
        return 1 if self.map[cell_idx[0]][cell_idx[1]] == "#" else 0

    def run(self) -> None:
        self.mark_cell()
        while self.get_next_cell() != -1:
            next_cell = self.get_next_cell()
            if next_cell == 1:
                self.turn_guard()
            else:
                self.move_guard()
                self.mark_cell()
        print("Distinct cells visited: ", len(self.visited))


data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

data = get_input(6)
d = Device(data)
d.run()
