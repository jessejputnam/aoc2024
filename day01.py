from lib import get_input


def build_lists(input: str):
    l1 = []
    l2 = []
    for line in input.split("\n"):
        nums = [x for x in line.split(" ") if x]
        if nums:
            l1.append(int(nums[0]))
            l2.append(int(nums[1]))
    return [l1, l2]


def part_one(input: str) -> int:
    total = 0
    l1, l2 = build_lists(input)

    l1.sort()
    l2.sort()

    for i in range(len(l1)):
        total += abs(l1[i] - l2[i])

    return total


def part_two(input: str) -> int:
    total = 0
    l1, l2 = build_lists(input)

    scores = {x: 0 for x in l1}
    for n in l2:
        if n in scores:
            scores[n] += 1

    for key, val in scores.items():
        total += key * val

    return total


data = get_input(1).text
print(part_two(data))
