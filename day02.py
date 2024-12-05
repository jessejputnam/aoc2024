from lib import get_input


class Analyzer:
    def __init__(self):
        self.safe_reports = 0
        self.cur: int = None
        self.is_inc: bool = None

    def get_safe_reports(self) -> int:
        return self.safe_reports

    def reset(self):
        self.cur: int = None
        self.is_inc: bool = None

    def advance(self, next: int) -> bool:
        if self.cur is None:
            self.cur = next
            return True

        step = next - self.cur
        if self.is_inc is None:
            self.is_inc = step > 0

        if step == 0 or abs(step) > 3 or ((step > 0) != self.is_inc):
            return False
        self.cur = next
        return True

    def add_safe_report(self):
        self.safe_reports += 1

    def analyze(self, report: list[int]) -> bool:
        self.reset()
        for level in report:
            if not self.advance(level):
                return False
        self.add_safe_report()
        return True

    def analyze_fault_tolerant(self, report: list[int]) -> None:
        for i in range(len(report)):
            new_report = [x for idx, x in enumerate(report) if idx != i]
            result = self.analyze(new_report)
            if result:
                return


##################################


def part_one(input: str) -> None:
    a = Analyzer()
    for line in input.split("\n")[:-1]:
        report = [int(x) for x in line.split(" ")]
        a.analyze(report)
    return a.get_safe_reports()


def part_two(input: str) -> None:
    a = Analyzer()
    for line in input.split("\n")[:-1]:
        report = [int(x) for x in line.split(" ")]
        result = a.analyze(report)
        if not result:
            a.analyze_fault_tolerant(report)
    return a.get_safe_reports()


####################################

data = get_input(2).text
part_two(data)
