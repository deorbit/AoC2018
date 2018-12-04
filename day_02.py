def read_input(fname="day_02_input.txt"):
    with open(fname) as f:
        content = f.readlines()
    return [l.strip() for l in content]
    
def day_02_star1(box_ids):
    two_count, three_count = 0, 0
    for box_id in box_ids:
        charcount = {c: box_id.count(c) for c in box_id}
        values = list(charcount.values())
        if 2 in values:
            two_count += 1
        if 3 in values:
            three_count += 1
    return two_count * three_count

def day_02_star2(box_ids):
    memo = [{} for _ in range(len(box_ids[0]))]
    for box_id in box_ids:
        for i, _ in enumerate(box_id):
            id_with_char_missing = box_id[0:i] + box_id[i+1:]
            if id_with_char_missing not in memo[i]:
                memo[i][id_with_char_missing] = True
            else:
                return id_with_char_missing
            