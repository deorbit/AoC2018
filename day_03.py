import re
import math

def read_input(fname="day_03_input.txt"):
    with open(fname) as f:
        active_region = {
            'left': math.inf,
            'top': math.inf,
            'right': 0,
            'bottom': 0
        }
        claims = []
        for l in f:
            print(l)
            (claim_id, left, top, width, height) = re.findall(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$', l)[0]
            (claim_id, left, top, width, height) = (int(claim_id), int(left), int(top), int(width), int(height))
            if left < active_region['left']:
                active_region['left'] = left
            if top < active_region['top']:
                active_region['top'] = top
            if left + width > active_region['right']:
                active_region['right'] = left + width
            if top + height > active_region['bottom']:
                active_region['bottom'] = top + height
            claims.append((claim_id, left, top, width, height))
    return (active_region, claims)

def day_03_star1(input):
    active_region_dims = input[0]
    active_left = active_region_dims['left']
    active_top = active_region_dims['top']
    active_bottom = active_region_dims['bottom']
    active_width = active_region_dims['right'] - active_region_dims['left']
    active_height = active_region_dims['bottom'] - active_region_dims['top']
    active_region = [[0 for _ in range(active_width)] for _ in range(active_height)]
    claims = input[1]
    overlap = 0

    if len(claims) == 0:
        return 0

    for c in claims:
        (claim_id, left, top, width, height) = c
        for y in range(top, top + height):
            for x in range(left, left + width):
                active_region[y][x] += 1
                if active_region[y][x] == 2:
                    overlap += 1

    return overlap

def day_03_star2(input):
    active_region_dims = input[0]
    active_left = active_region_dims['left']
    active_top = active_region_dims['top']
    active_bottom = active_region_dims['bottom']
    active_width = active_region_dims['right'] - active_region_dims['left']
    active_height = active_region_dims['bottom'] - active_region_dims['top']
    active_region = [[0 for _ in range(active_width)] for _ in range(active_height)]
    claims = input[1]
    overlap = 0

    if len(claims) == 0:
        return 0

    conflicted = {}

    for c in claims:
        (claim_id, left, top, width, height) = c
        for y in range(top, top + height):
            for x in range(left, left + width):
                prev_claim = active_region[y][x]
                active_region[y][x] = claim_id
                if prev_claim != 0:
                    conflicted[prev_claim] = True
                    conflicted[claim_id] = True
                    
    # Let's find out who is not overlapped
    for c in claims:
        (claim_id, left, top, width, height) = c
        if conflicted[claim_id] is not True:
            return claim_id
    return None