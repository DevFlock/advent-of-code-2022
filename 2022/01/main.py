import sys, pathlib;sys.path.append(str(pathlib.Path(__name__).absolute().parent.parent))
import util
import time

data = [i.strip() for i in util.get_input(1, 2022).split("\n")]

def part_1(inp):
    elves = []

    current_elf = 0
    for elf in data:
        if elf == "":
            elves.append(current_elf)
            current_elf = 0
            continue

        current_elf += int(elf)

    return sorted(elves, reverse=True)[0]

def part_2(inp):
    elves = []

    current_elf = 0
    for elf in data:
        if elf == "":
            elves.append(current_elf)
            current_elf = 0
            continue

        current_elf += int(elf)

    return sum(sorted(elves, reverse=True)[0:3])


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
