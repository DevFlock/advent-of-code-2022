import sys, pathlib;sys.path.append(str(pathlib.Path(__name__).absolute().parent.parent))
import util
import time

data = [i.strip() for i in util.get_input(7, 2022).split("\n")]

def calc_subdir(d: dict, sub = False):
    total_size = 0

    for key, value in d.items():
        if isinstance(value, dict):
            dir_size, new_dir = calc_subdir(value, sub=True)

            total_size += dir_size
            d[key] = new_dir

        else:
            total_size += value

    d["size"] = total_size

    if not sub:
        return d
    else:
        return total_size, d

def calc_dir_size(d: dict):
    total_size = 0

    for key, value in d.items():
        if isinstance(value, dict):
            dir_size = calc_dir_size(value)

            # if dir_size <= 100_000:
            total_size += dir_size

        elif key == "size":
            if value <= 100_000:
                total_size += value

    return total_size

def part_1(inp):
    working_dir = ""
    file_system = {}

    for line in inp:
        if line.startswith("$ cd"):
            _dir = line.split(" ")[2]
            if _dir != "..":
                if _dir.startswith("/"):
                    working_dir = _dir
                    continue
                working_dir += "/"+_dir

                pwd = None
                for path in working_dir.split("/"):
                    if path == "":
                        pwd = file_system
                        continue

                    if pwd.get(path) is None:
                        pwd[path] = {}
                    pwd = pwd[path]


            else:
                working_dir = "/" + "/".join(i for i in working_dir.split("/")[0:-1] if i.strip() != "")

            if working_dir.startswith("//"): working_dir = working_dir[1::]

        elif not line.startswith("$"):
            pwd = None

            for _dir in working_dir.split("/"):
                if _dir == "":
                    pwd = file_system
                    continue

                pwd = pwd[_dir]

            split = line.split(" ")

            if split[0] != "dir":
                pwd["size"] = pwd.get("size", 0) + int(split[0])

    file_system = calc_subdir(file_system)

    return calc_dir_size(file_system)


def all_sizes(d: dict) -> list[int]:
    _all = []

    for key, value in d.items():
        if isinstance(value, dict):
            dict_sizes = all_sizes(value)
            _all += dict_sizes

        else:
            _all.append(d["size"])
    return _all

def part_2(inp):
    working_dir = ""
    file_system = {}

    for line in inp:
        if line.startswith("$ cd"):
            _dir = line.split(" ")[2]
            if _dir != "..":
                if _dir.startswith("/"):
                    working_dir = _dir
                    continue
                working_dir += "/"+_dir

                pwd = None
                for path in working_dir.split("/"):
                    if path == "":
                        pwd = file_system
                        continue

                    if pwd.get(path) is None:
                        pwd[path] = {}
                    pwd = pwd[path]


            else:
                working_dir = "/" + "/".join(i for i in working_dir.split("/")[0:-1] if i.strip() != "")

            if working_dir.startswith("//"): working_dir = working_dir[1::]

        elif not line.startswith("$"):
            pwd = None

            for _dir in working_dir.split("/"):
                if _dir == "":
                    pwd = file_system
                    continue

                pwd = pwd[_dir]

            split = line.split(" ")

            if split[0] != "dir":
                pwd["size"] = pwd.get("size", 0) + int(split[0])

    file_system = calc_subdir(file_system)

    all_dir_sizes = all_sizes(file_system)

    total_space = 70_000_000
    required_space = 30_000_000
    used_space = total_space - file_system["size"]
    space_required = required_space - used_space

    smallest_size = 0

    for size in all_dir_sizes:
        if size >= space_required:
            if size < smallest_size or smallest_size == 0:
                smallest_size = size

    return smallest_size


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
