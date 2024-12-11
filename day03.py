from lib import get_input


class Parser:
    def __init__(self):
        self.i: int = 0
        self.j: int = 0
        self.x: str = ""
        self.y: str = ""
        self.enabled: bool = True
        self.sum: int = 0
        self.is_part_2: bool = False

    def get_sum(self) -> int:
        print(f"Part {2 if self.is_part_2 else 1}: ", self.sum)

    def reset_x_y(self) -> None:
        self.x, self.y = "", ""

    def reset(self):
        self.i: int = 0
        self.j: int = 0
        self.x: str = ""
        self.y: str = ""
        self.enabled: bool = True
        self.sum: int = 0
        self.is_part_2: bool = False

    def advance_i_to_j(self) -> None:
        self.i = self.j
        self.reset_x_y()

    def update_var(self, var: str, num: str) -> None:
        if var == "x":
            self.x += num
        else:
            self.y += num
        self.j += 1

    def mul(self, x: str, y: str) -> None:
        self.sum += int(x) * int(y)

    def read(self, input: str, is_part_2: bool = False) -> None:
        self.reset()
        self.is_part_2 = is_part_2
        while self.i < len(input) - 8:
            if is_part_2 and input[self.i : (self.i + 4)] == "do()":
                self.enabled = True
                self.i = self.i + 4
                continue

            if is_part_2 and input[self.i : (self.i + 7)] == "don't()":
                self.enabled = False
                self.i = self.i + 7
                continue

            if input[self.i : (self.i + 4)] == "mul(":
                self.j = self.i + 4

                if not input[self.j].isnumeric():
                    self.advance_i_to_j()
                    continue

                while input[self.j].isnumeric():
                    self.update_var("x", input[self.j])

                if input[self.j] != ",":
                    self.advance_i_to_j()
                    continue

                self.j += 1

                if not input[self.j].isnumeric():
                    self.advance_i_to_j()
                    continue

                while input[self.j].isnumeric():
                    self.update_var("y", input[self.j])

                if input[self.j] != ")":
                    self.advance_i_to_j()
                    continue

                if self.enabled:
                    self.mul(self.x, self.y)
                self.reset_x_y()
            self.i += 1


data = get_input(3)
p = Parser()
p.read(data)
p.get_sum()
p.read(data, True)
p.get_sum()
