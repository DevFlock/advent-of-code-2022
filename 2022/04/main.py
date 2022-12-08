import sys, pathlib;sys.path.append(str(pathlib.Path(__name__).absolute().parent.parent))
import util
import time
from numpy import sign

data = [l.strip() for l in util.get_input(4, 2022).split("\n")]

def part_1(inp):
    overlaps = 0

    for pair in inp:
        e1, e2 = [[int(i) for i in i.split("-")] for i in pair.split(",")]

        if e1[0] <= e2[0] and e1[1] >= e2[1]:
            overlaps += 1
        elif e2[0] <= e1[0] and e2[1] >= e1[1]:
            overlaps += 1

    return overlaps

def part_2(inp):
    overlaps = 0

    for pair in inp:
        e1, e2 = [[int(i) for i in i.split("-")] for i in pair.split(",")]
        # im sorry
        overlaps += sign(sum(1 for i in range(e2[0], e2[1]+1) if i in list(range(e1[0], e1[1]+1))))

    return overlaps


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
