import sys, os.path;sys.path.append(os.path.abspath(".."))
import util
import time

data = [line.strip() for line in util.get_input(3, 2022).split()]

def part_1(inp):
    misplaced = []

    for rucksack in data:
        comp1, comp2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]

        comp1_items = []

        for item in comp1:
            comp1_items.append(item)

        for item in comp2:
            if item in comp1_items:
                misplaced.append(item)
                break

    value = 0

    for item in misplaced:
        if item.isupper():
            value += ord(item)-38
        else:
            value += ord(item)-96

    return value

def part_2(inp):
    groups = []

    for index in range(0, len(inp), 3):
        elves = [inp[index], inp[index+1], inp[index+2]]

        occurances = {}

        for elf in elves:
            appeared = []
            for item in elf:
                if item not in appeared:
                    occurances[item] = occurances.get(item, 0) + 1
                    appeared.append(item)

        _sorted = dict(sorted(occurances.items(), key=lambda x: x[1], reverse=True))
        groups.append(list(_sorted.keys())[0])

    value = 0

    for item in groups:
        if item.isupper():
            value += ord(item)-38
        else:
            value += ord(item)-96

    return value


if __name__ == "__main__":
    t1 = time.time()
    out_1 = part_1(data)
    t2 = time.time()
    out_2 = part_2(data)
    t3 = time.time()

    time_1 = round(t2-t1, 8)
    time_2 = round(t3-t2, 8)

    print(f"\n\n{'Code Output':-^30}")
    print(f"{'Part': <10}{'Time Taken': ^10}{'Output': >10}")
    print(f"{'1': <10}{time_1: ^10}{str(out_1): >10}")
    print(f"{'2': <10}{time_2: ^10}{str(out_2): >10}\n\n")
