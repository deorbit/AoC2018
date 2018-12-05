from collections import deque
import math

def read_input(fname="day_05_input.txt"):
    with open(fname) as f:
        return f.readline()

def collapse(polymer, remove_type=None):
    if remove_type is not None:
        polymer = polymer.replace(remove_type.lower(), "").replace(remove_type.upper(), "")
    q = deque(polymer[0])
    for u in polymer[1:]:
        if q and abs(ord(u) - ord(q[-1])) == 32:
            q.pop()
        else:
            q.append(u)
    return ''.join(q)

def day_05_star1(polymer):
    return collapse(polymer)

def day_05_star2(polymer):
    typecount = {}
    for u in polymer:
        unit_type = u.lower()
        _ = typecount.setdefault(unit_type, 0)
        typecount[unit_type] += 1
    lengths = []
    for t in typecount:
        lengths.append(len(collapse(polymer, remove_type=t)))
    return min(lengths)