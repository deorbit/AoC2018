import re
import collections
from random import randint
from PIL import Image
import numpy as np

def read_input(fname="./day_06_input.txt"):
    with open(fname) as f:
        coords = [[int(c) for c in l.split(',')] for l in f]
    return coords

def day_06_star1(coords):
    # bfs from each coordinate, stop when we collide with other searches
    cells_to_visit = {(c[0], c[1]): i for i, c in enumerate(coords)}
    cell_count = {i: 0 for i in range(len(coords))}
    visited = set()

    while cells_to_visit:
        visiting = cells_to_visit
        cells_to_visit = {}
        for x, y in visiting:
            for (dx, dy) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                neighbor = (x + dx, y + dy)
                if 0<=x+dx<360 and 0<=y+dy<360 and neighbor not in visited:
                    if neighbor in cells_to_visit and cells_to_visit[neighbor] != visiting[(x, y)]: # bumping into other neighborhood
                        cells_to_visit[neighbor] = -1
                    else:
                        cells_to_visit[neighbor] = visiting[(x, y)]
        
        for x, y in cells_to_visit:
            visited.add((x, y))
            seed_cell_id = cells_to_visit[(x, y)]
            if seed_cell_id in cell_count and (x in (0,359) or y in (0,359)):
                del cell_count[seed_cell_id]
            if seed_cell_id != -1:
                if seed_cell_id in cell_count:
                    cell_count[seed_cell_id] += 1

    return max(cell_count.values())

def day_06_star2(coords):
    x = [c[0] for c in coords]
    y = [c[1] for c in coords]
    xnp = np.array(x).reshape(50,1)
    ynp = np.array(y).reshape(50,1)
    xdist = np.abs(xnp - np.arange(360))
    ydist = np.abs(ynp - np.arange(360))
    xsum = np.sum(xdist, axis=0)
    ysum = np.sum(ydist, axis=0).reshape(360,1)
    total_sum = ysum + xsum
    lt10000 = total_sum[total_sum < 10000]
    
    return lt10000.shape[0]

import time


if __name__=="__main__":
    start = time.time()
    day_06_star2(read_input())
    end = time.time()
    print(end - start, "seconds")