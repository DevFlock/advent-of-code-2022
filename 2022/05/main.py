import sys, os.path;sys.path.append(os.path.abspath(".."))
import util
import time
from typing import Self

data = util.get_input(5, 2022)

class Stack:
    def __init__(self) -> None:
        self.crates = []
    
    def move(self, amount: int, stack: Self):
        crates = [self.crates.pop(-1) for _ in range(amount)]
        [stack.crates.append(i) for i in crates]
    
    def move2(self, amount: int, stack: Self):
        crates = [self.crates.pop(-1) for _ in range(amount)][::-1]
        [stack.crates.append(i) for i in crates]

    def add(self, crate: str):
        self.crates.append(crate)
    
    def peek(self) -> str:
        return self.crates[-1]
    
    def __str__(self):
        return " ".join(self.crates)

    def __repr__(self) -> str:
        return " ".join(self.crates)

def part_1(inp):
    crates, instructions = [i.split("\n") for i in data.split("\n\n")]
    stacks: dict = {}

    for line in crates[:-1]:
        for index in range(1, 9*4-1, 4):
            stack_num = (index//4)+1

            stacks[stack_num] = stacks.get(stack_num, Stack())
            if index > len(line):
                continue

            if line[index] != " ":
                stacks[stack_num].add(line[index])
    
    for stack in stacks:
        stacks[stack].crates = stacks[stack].crates[::-1]


    for inst in instructions:
        _, amount, _, stack1, _, stack2 = [i for i in inst.split(" ")]
        amount, stack1, stack2 = int(amount), int(stack1), int(stack2)
        stacks[(stack1)].move(amount, stacks[stack2])
    
    out = [stacks[i].peek() for i in stacks]
    return "".join(out)

def part_2(inp):
    crates, instructions = [i.split("\n") for i in data.split("\n\n")]
    stacks: dict = {}

    for line in crates[:-1]:
        for index in range(1, 9*4-1, 4):
            stack_num = (index//4)+1

            stacks[stack_num] = stacks.get(stack_num, Stack())
            if index > len(line):
                continue

            if line[index] != " ":
                stacks[stack_num].add(line[index])
    
    for stack in stacks:
        stacks[stack].crates = stacks[stack].crates[::-1]


    for inst in instructions:
        _, amount, _, stack1, _, stack2 = [i for i in inst.split(" ")]
        amount, stack1, stack2 = int(amount), int(stack1), int(stack2)
        stacks[(stack1)].move2(amount, stacks[stack2])
    
    out = [stacks[i].peek() for i in stacks]
    return "".join(out)


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
