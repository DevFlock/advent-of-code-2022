import sys, pathlib;sys.path.append(str(pathlib.Path(__name__).absolute().parent.parent))
import util
import time

data = util.get_input(6, 2022)

def part_1(inp):
    prev_chars = []
    index = 0

    for char in inp:
        if len(prev_chars) == 4:
            if sum(1 for i in prev_chars if prev_chars.count(i) != 1) == 0:
                return index
            prev_chars.pop(0)
        prev_chars.append(char)
        index += 1

def part_2(inp):
    prev_chars = []
    index = 0

    for char in inp:
        if len(prev_chars) == 14:
            if sum(1 for i in prev_chars if prev_chars.count(i) != 1) == 0:
                return index
            prev_chars.pop(0)
        prev_chars.append(char)
        index += 1

if __name__ == "__main__":
    # Test stuff
    a = part_1("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    b = part_1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    c = part_1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    d = part_1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    e = part_1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

    a2 = part_2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    b2 = part_2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    c2 = part_2("nppdvjthqldpwncqszvftbrmjlhg") == 23
    d2 = part_2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    e2 = part_2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
    print(sum([a,b,c,d,e]) == 5, sum([a2,b2,c2,d2,e2]) == 5)

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
