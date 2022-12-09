_input = """30373
25512
65332
33549
35340"""

data = [i.strip() for i in _input.split("\n") if i != ""]

grid = []

for line in data:
    grid.append([int(c) for c in line])

visible_trees = 0

for yindx, line in enumerate(grid[1:-1]): # [1:-1] Ignores edges
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

print(visible_trees, perim, visible_trees+perim)