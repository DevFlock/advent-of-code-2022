import pytest
from main import part_1, part_2

def p1_correct_example():
    inp = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

    assert part_1([i.strip() for i in inp.split("\n")]) == None

def returns_value():
    assert part_2 != None
