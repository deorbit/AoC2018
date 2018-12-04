import re
from datetime import datetime

def read_input(fname="day_04_input.txt"):
    records = []
    with open(fname) as f:
        for l in f:
            # print(l)
            record = re.findall(r'^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (.*$)', l)[0]
            # print(record)
            records.append(record)
    return sorted(records, key=lambda x: x[0])

def get_guards(records):
    guards = {} # ID: []*60
    for r in records:
        timestamp = datetime.strptime(r[0], "%Y-%m-%d %H:%M")
        
        guard_match = re.match(r'Guard #(\d+) ', r[1])
        if guard_match:
            guard_id = int(guard_match.group(1))
            if guard_id not in guards:
                minutes = [0] * 60
                guards[guard_id] = minutes
        
        sleep_match = re.match('falls asleep', r[1])
        if sleep_match:
            sleep_start = timestamp
        
        awake_match = re.match('wakes up', r[1])
        if awake_match:
            start_minute = sleep_start.minute
            end_minute = timestamp.minute
            for m in range(start_minute, end_minute):
                guards[guard_id][m] += 1
    return guards

def day_04_star1(records):
    guards = get_guards(records)

    max_sleep = 0
    max_sleeper = None
    for guard, minutes in guards.items():
        total_sleep = sum(minutes)
        if total_sleep > max_sleep:
            max_sleep = total_sleep
            max_sleeper = guard

    max_minute = guards[max_sleeper].index(max(guards[max_sleeper]))
    return max_sleeper * max_minute

def day_04_star2(records):
    guards = get_guards(records)

    sorted_guards = sorted(guards.items(), key=lambda kv:max(kv[1]))
    guard_id = sorted_guards[-1][0]
    max_minute = sorted_guards[-1][1].index(max(sorted_guards[-1][1]))
    return guard_id * max_minute