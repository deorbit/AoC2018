def read_input(fname):
    with open(fname) as f:
        content = f.readlines()
    return [int(l.strip()) for l in content]

def day_01_star1():
    deltas = read_input("day_01_input.txt")
    return sum(deltas)

def day_01_star2(deltas = read_input("day_01_input.txt")):
    cur_sum, delta_index = 0, 0
    repeated = False
    sums = set()
    while not repeated:
        cur_sum += deltas[delta_index]
        delta_index = (delta_index + 1) % len(deltas)
        if cur_sum in sums:
            repeated = True
        else:
            sums.add(cur_sum)
    return cur_sum
    
if __name__=="__main__":
    print(day_01_star2())