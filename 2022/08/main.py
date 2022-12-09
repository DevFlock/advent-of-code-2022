import sys, pathlib;sys.path.append(str(pathlib.Path(__name__).absolute().parent.parent))
import util
import time

_input = """30373
25512
65332
33549
35340"""

data = [i.strip() for i in util.get_input(8, 2022).split("\n") if i != ""]
# data = [i.strip() for i in _input.split("\n") if i != ""]

def part_1(inp):
    grid = []

    for line in inp:
        grid.append([int(c) for c in line])
    

    visible_trees = 0

    for yindx, line in enumerate(grid[1:-1]):
        for xindx, num in enumerate(line[1:-1]):
            x, y = xindx+1, yindx+1

            check_directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for x_dir, y_dir in check_directions:
                curx, cury = x, y

                visible = True

                while True:
                    curx, cury = curx+x_dir, cury+y_dir

                    if curx < 0 or cury < 0:
                        break
                    elif curx > len(grid)-1 or cury > len(grid)-1:
                        break

                    grid_value = grid[curx][cury]

                    if grid_value >= num:
                        visible = False
                        break

                if visible:
                    visible_trees += 1
                    break

    perim = len(grid)*2 + (len(grid[0])-2)*2

    print(visible_trees, perim)

    return visible_trees + perim

def part_2(inp):
    return None


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
