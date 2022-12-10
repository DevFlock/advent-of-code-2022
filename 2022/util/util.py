from requests import get
import os
from shutil import copy2
from typing import Self
from dotenv import load_dotenv

load_dotenv()

SESSION = os.getenv("SESSION_KEY")
YEAR = os.getenv("YEAR")

def get_input(day: int, year: int = YEAR) -> str:
    try:
        day = int(day)
    except ValueError:
        raise ValueError("\"day\" has to be an int.")

    if day <= 0 or day > 25:
        raise ValueError("\"day\" has to be an int from 1-25 (inclusive)")

    year = str(year)  # type: ignore
    day = str(day)  # type: ignore

    # Check the cache
    try:
        with open(os.path.join(os.path.dirname(__file__), f"../../cache/{year}_{day}_input.txt"), "r") as f:
            return f.read()

    except FileNotFoundError:
        pass

    req = get(f"https://adventofcode.com/{year}/day/{day}/input",
                cookies={"session": SESSION})

    if req.status_code != 200:
        raise Exception(f"Unable to get input, error code: {req.status_code} {req.reason}")

    with open(os.path.join(os.path.dirname(__file__), f"../../cache/{year}_{day}_input.txt"), "w") as f:
        out = req.text
        f.write(out)

    return out


def create_day(day: int, year: int = YEAR):
    try:
        day = int(day)
    except ValueError:
        raise ValueError("\"day\" has to be an int.")

    if day <= 0 or day > 25:
        raise ValueError("\"day\" has to be an int from 1-25 (inclusive)")

    base = os.path.dirname(__file__)
    _dir = os.path.join(base, "../..", year := str(year), day := str(day).zfill(2))  # type: ignore
    templates = os.path.join(base, "../../templates")

    try: os.makedirs(_dir)
    except FileExistsError: pass

    for file in os.listdir(templates):
        copy2(os.path.join(templates, file), _dir)

    with open(os.path.join(_dir, "main.py"), "r") as f:
        data = f.read()

    with open(os.path.join(_dir, "main.py"), "w") as f:
        day = str(int(day)) # This is to remove any 0's from start
        f.write(data.replace("{{YEAR}}", year).replace("{{DAY}}", day))  # type: ignore


class Point2D:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def manhattan_distance(self, other: Self) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    @classmethod 
    def add(cls, p1, p2):
        return Point2D((p1.x+p2.x), (p1.y+p2.y))
    
    @classmethod
    def multiply(cls, p1, p2):
        return Point2D((p1.x*p2.x), (p1.y*p2.y))
    
    def __str__(self) -> str:
        return f"Point(x:{self.x}, y:{self.y})"
    
    def __repr__(self) -> str:
        return f"Point(x:{self.x}, y:{self.y})"

class Point3D:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def manhattan_distance(self, other: Self) -> int:
        return abs(self.x - other.x) + abs(self.y, other.y) + abs(self.z, other.z)

if __name__ == "__main__":
    from datetime import datetime
    now = datetime.today()

    if now.month == 12 and now.day <= 25:
        create_day(now.day)
        exit()

    day = input("What day would you like to create? ")
    create_day(day)
