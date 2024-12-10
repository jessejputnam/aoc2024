from lib import get_input


class Manual:
    def __init__(self, data):
        rules, pages = data.split("\n\n")
        self.rules = [[int(y) for y in x.split("|")] for x in rules.split("\n")]
        self.pages = [[int(y) for y in x.split(",")] for x in pages.split("\n")[:-1]]
        self.mid_sum = 0

    def print_pages(self):
        for page in self.pages:
            print(page)

    def get_index(self, arr, val) -> int:
        for i, v in enumerate(arr):
            if v == val:
                return i
        return -1

    def calc_middle_sums(self, idxs: list[int] = None):
        if idxs is None:
            for page in self.pages:
                self.mid_sum += page[int(len(page) / 2)]
        else:
            for i in idxs:
                self.mid_sum += self.pages[i][int(len(self.pages[i]) / 2)]

    def print_middle_sum(self):
        print(self.mid_sum)

    def analyze1(self):
        for rule in self.rules:
            valid_pages = []
            for page in self.pages:
                a = self.get_index(page, rule[0])
                b = self.get_index(page, rule[1])
                if a < b or -1 in [a, b]:
                    valid_pages.append(page)
            self.pages = valid_pages
        self.calc_middle_sums()

    def analyze2(self):
        swapped_idxs = []
        for idx, page in enumerate(self.pages):
            valid = False
            while not valid:
                swaps = 0
                for rule in self.rules:
                    a = self.get_index(page, rule[0])
                    b = self.get_index(page, rule[1])
                    if a > b and -1 not in [a, b]:
                        if idx not in swapped_idxs:
                            swapped_idxs.append(idx)
                        page[a] = rule[1]
                        page[b] = rule[0]
                        swaps += 1
                valid = swaps == 0

        self.calc_middle_sums(swapped_idxs)


data = get_input(5).text

m = Manual(data)
m.analyze2()
m.print_middle_sum()
