import sys, pathlib;sys.path.append(str(pathlib.Path(__name__).absolute().parent.parent))
import util
from util import Point2D
import time
import math

data = [i.strip() for i in util.get_input(9, 2022).split("\n") if i != ""]

def part_1(inp, example=False):
    head_pos = Point2D(0, 0)
    tail_pos = Point2D(0, 0)
    visited = set()

    for move in inp:
        _dir, count = move.split(" ")
        count = int(count)

        diry, dirx = {"L": (-1,0), "R": (1,0), "U": (0,1), "D":(0,-1)}[_dir]
        _dir = Point2D(dirx, diry)

        for _ in range(count):
            head_pos = Point2D.add(head_pos, _dir)
            distance = head_pos.manhattan_distance(tail_pos)

            if (tail_pos.x, tail_pos.y) == (head_pos.x, head_pos.y):
                continue

            if distance > 2:

                xdif = head_pos.x - tail_pos.x
                ydif = head_pos.y - tail_pos.y

                if xdif == 0:
                    direction = Point2D(0, ydif//abs(ydif))
                elif ydif == 0:
                    direction = Point2D(xdif//abs(xdif), 0)
                else:
                    direction = Point2D(xdif//abs(xdif), ydif//abs(ydif))

                tail_pos = Point2D.add(tail_pos, direction)    

            elif distance == 2 and (head_pos.y == tail_pos.y or head_pos.x == tail_pos.x):
                xdif = head_pos.x - tail_pos.x
                ydif = head_pos.y - tail_pos.y

                if xdif == 0:
                    direction = Point2D(0, ydif//abs(ydif))
                elif ydif == 0:
                    direction = Point2D(xdif//abs(xdif), 0)

                tail_pos = Point2D.add(tail_pos, direction)    


            if str(tail_pos) not in visited:
                visited.add(str(tail_pos))

            if example:
                grid = [["." for i in range(6)] for i in range(6)]

                grid[head_pos.x][head_pos.y] = "H"
                grid[tail_pos.x][tail_pos.y] = "t"

                # for vis in visited:
                #     grid[vis.x][vis.y] = "x"

                if (head_pos.x, head_pos.y) == (tail_pos.x, tail_pos.y):
                    grid[head_pos.x][head_pos.y] = "O"

                for i in grid[::-1]:
                    print(" ".join(i))
                print(head_pos.manhattan_distance(tail_pos), "\n", dirx, diry, count)


    return len(visited)

def part_2(inp, example=False):
    head_pos = Point2D(11, 5)
    knots = [Point2D(0, 0) for _ in range(9)]
    tail_pos = knots[-1]
    visited = set()

    for move in inp:
        _dir, count = move.split(" ")
        count = int(count)

        diry, dirx = {"L": (-1,0), "R": (1,0), "U": (0,1), "D":(0,-1)}[_dir]
        _dir = Point2D(dirx, diry)

        for _ in range(count):
            head_pos = Point2D.add(head_pos, _dir)
            for index, knot in enumerate(knots):
                if index != 0:
                    target_knot = knots[index-1]
                else:
                    target_knot = head_pos
                distance = target_knot.manhattan_distance(knot)

                if (knot.x, knot.y) == (target_knot.x, target_knot.y):
                    continue

                if distance > 2:

                    xdif = target_knot.x - knot.x
                    ydif = target_knot.y - knot.y

                    if xdif == 0:
                        direction = Point2D(0, ydif//abs(ydif))
                    elif ydif == 0:
                        direction = Point2D(xdif//abs(xdif), 0)
                    else:
                        direction = Point2D(xdif//abs(xdif), ydif//abs(ydif))

                    knots[index] = Point2D.add(knot, direction)    

                elif distance == 2 and (target_knot.y == knot.y or target_knot.x == knot.x):
                    xdif = target_knot.x - knot.x
                    ydif = target_knot.y - knot.y

                    if xdif == 0:
                        direction = Point2D(0, ydif//abs(ydif))
                    elif ydif == 0:
                        direction = Point2D(xdif//abs(xdif), 0)

                    tail_pos = Point2D.add(tail_pos, direction)    


            if str(tail_pos) not in visited:
                visited.add(str(tail_pos))

            # print(knots)

            if example:
                grid = [["." for i in range(36)] for i in range(36)]

                grid[head_pos.x][head_pos.y] = "H"
                for index, knot in enumerate(knots):
                    grid[knot.x][knot.y] = str(index)
                    # print(knot.x, knot.y)

                # for vis in visited:
                #     grid[vis.x][vis.y] = "x"

                if (head_pos.x, head_pos.y) == (tail_pos.x, tail_pos.y):
                    grid[head_pos.x][head_pos.y] = "O"

                for i in grid[::-1]:
                    print(" ".join(i))
                print(head_pos.manhattan_distance(tail_pos), "\n", dirx, diry, count)


    print(len(visited) < 7551)
    return len(visited)


if __name__ == "__main__":
    t1 = time.time()
    out_1 = part_1(data)
    # out_1 = None
    t2 = time.time()
    out_2 = part_2(data)
    t3 = time.time()

    with open("example.txt") as f:
        example = [i.strip() for i in f.read().split("\n") if i != ""]

    example_1 = part_1(example, False)
    example_2 = part_2(example, True)

    time_1 = round(t2-t1, 8)
    time_2 = round(t3-t2, 8)

    print(f"\n\n{' Code Output ':-^40}")
    print(f"{'Part': <10}{'Time Taken': ^10}{'Output': ^10}{'Example': >10}")
    print(f"{'1': <10}{time_1: ^10}{str(out_1): ^10}{str(example_1): >10}")
    print(f"{'2': <10}{time_2: ^10}{str(out_2): ^10}{str(example_2): >10}\n\n")
