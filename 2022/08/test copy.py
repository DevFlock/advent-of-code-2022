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

for yind, line in enumerate(grid[1:-1]):
    for xind, num in enumerate(line[1:-1]):
        
        up = True
        for y in range(yind, -1, -1):
            if num <= grid[xind][y]:
                up = False
                break
        
        down = True
        for y in range(yind, len(grid)):
            if num <= grid[xind][y]:
                down = False
                break
        
        left = True
        for x in range(xind, -1, -1):
            if num <= grid[x][yind]:
                left = False
                break
        
        right = True
        for x in range(xind, len(grid)):
            if num <= grid[x][yind]:
                right = False
                break
        
        if True in [up, down, left, right]:
            visible_trees += 1

perim = len(grid)*2 + (len(grid[0])-2)*2

print(visible_trees, perim, visible_trees+perim)