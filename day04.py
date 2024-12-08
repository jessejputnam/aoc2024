from lib import get_input


class CeresPart1:
    def __init__(self, matrix: list[list[str]]):
        self.data = matrix
        self.valid_xmas = 0

    def add_count(self):
        self.valid_xmas += 1

    def build_string(self, y: int, x: int, y_dir: int, x_dir: int) -> str:
        s = ""
        for i in range(4):
            s += self.data[y + (y_dir * i)][x + (x_dir * i)]
        return s

    def check_horizontal(self, y: int, x: int, direction: str):
        if direction == "left" and x < 3:
            return
        if direction == "right" and x > len(self.data[0]) - 4:
            return
        x_dir = -1 if direction == "left" else 1
        if self.build_string(y, x, 0, x_dir) == "XMAS":
            self.add_count()

    def check_vertical(self, y: int, x: int, direction: str):
        if direction == "up" and y < 3:
            return
        if direction == "down" and y > len(self.data) - 4:
            return
        y_dir = -1 if direction == "up" else 1
        if self.build_string(y, x, y_dir, 0) == "XMAS":
            self.add_count()

    def check_diagonal(self, y: int, x: int, direction: str):
        if direction == "up-left" and (x < 3 or y < 3):
            return
        if direction == "up-right" and (x > (len(self.data[0]) - 4) or y < 3):
            return
        if direction == "down-left" and (y > (len(self.data) - 4) or x < 3):
            return
        if direction == "down-right":
            if x > (len(self.data[0]) - 4) or y > (len(self.data) - 4):
                return
        y_dir = -1 if direction in ["up-left", "up-right"] else 1
        x_dir = -1 if direction in ["up-left", "down-left"] else 1
        if self.build_string(y, x, y_dir, x_dir) == "XMAS":
            self.add_count()

    def get_valid_xmas_count(self) -> int:
        return self.valid_xmas

    def analyze(self):
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                if self.data[y][x] != "X":
                    continue
                self.check_horizontal(y, x, "left")
                self.check_diagonal(y, x, "up-left")
                self.check_vertical(y, x, "up")
                self.check_diagonal(y, x, "up-right")
                self.check_horizontal(y, x, "right")
                self.check_diagonal(y, x, "down-right")
                self.check_vertical(y, x, "down")
                self.check_diagonal(y, x, "down-left")


# data = get_input(4).text

# matrix = data.split("\n")[:-1]

# c1 = CeresPart1(matrix)
# c1.analyze()
# print(c1.get_valid_xmas_count())


class CeresPart2:
    def __init__(self, matrix: list[list[str]]):
        self.data = matrix
        self.valid_x_mas = 0

    def add_count(self):
        self.valid_x_mas += 1

    def build_string(self, y: int, x: int, slash_dir: str) -> str:
        if slash_dir == "back":
            return self.data[y - 1][x - 1] + self.data[y][x] + self.data[y + 1][x + 1]
        if slash_dir == "forward":
            return self.data[y - 1][x + 1] + self.data[y][x] + self.data[y + 1][x - 1]

    def check_x_mas(self, y: int, x: int):
        if y < 1 or x < 1 or y > len(self.data) - 2 or x > len(self.data[0]) - 2:
            return
        back_slash = self.build_string(y, x, "back") in ["MAS", "SAM"]
        forward_slash = self.build_string(y, x, "forward") in ["MAS", "SAM"]
        if back_slash and forward_slash:
            self.add_count()

    def get_valid_x_mas_count(self) -> int:
        return self.valid_x_mas

    def analyze(self):
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                if self.data[y][x] != "A":
                    continue
                self.check_x_mas(y, x)


data = get_input(4).text
matrix = data.split("\n")[:-1]

c2 = CeresPart2(matrix)
c2.analyze()
print(c2.get_valid_x_mas_count())
