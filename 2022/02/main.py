import sys, pathlib;sys.path.append(str(pathlib.Path(__name__).absolute().parent.parent))
import util
import time

data = [move.strip() for move in util.get_input(2, 2022).split("\n")]

def part_1(inp):
    score = 0
    for move in inp:
        opp, me = move.split(" ")

        opp = {"A": "r", "B": "p", "C": "s"}[opp]
        me = {"X": "r", "Y": "p", "Z": "s"}[me]

        try:
            assert \
                (opp, me) == ("r", "p") or \
                (opp, me) == ("p", "s") or \
                (opp, me) == ("s", "r")
            won = 1
        except AssertionError:
            won = 0

        try:
            assert \
                (opp, me) == (opp, opp)
            draw = 1
        except AssertionError:
            draw = 0

        score += won*6 + draw*3 + {"r":1,"p":2,"s":3}[me]

    return score

def part_2(inp):
    score = 0
    for move in inp:
        opp, outcome = move.split(" ")

        opp = {"A": "r", "B": "p", "C": "s"}[opp]
        me = {"r": ("p", "s"), "p": ("s", "r"), "s": ("r", "p")}[opp] # This gives a tuple for each move: (win against, lose against)

        match outcome:
            case "X":
                me = me[1]
            case "Y":
                me = opp
            case "Z":
                me = me[0]

        score += (outcome=="Z")*6 + (outcome=="Y")*3 + {"r":1,"p":2,"s":3}[me]

    return score



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
