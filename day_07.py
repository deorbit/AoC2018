import re
import collections

def read_input(fname="./day_07_input.txt"):
    dag = {}
    successors = set()
    with open(fname) as f:
        for l in f:
            found = re.findall(r'step ([A-Z])', l, re.IGNORECASE)
            next_steps = dag.setdefault(found[0], [])
            next_steps.append(found[1])
            successors.add(found[1]) # so we can add final step(s) to the map
    return (dag, successors)


def day_07_star1(dag_successors):
    dag = dag_successors[0]
    successors = dag_successors[1]
    starts = [d for d in dag if d not in successors]
    ends = [s for s in successors if s not in dag]

    for e in ends:
        dag[e] = []

    q = collections.deque(sorted(starts, reverse=True))
    plan = collections.deque()
    visited = set()

    def visit(n):
        if n in visited:
            return
        for m in sorted(dag[n], reverse=True):
            visit(m)
        visited.add(n)
        plan.appendleft(n)
        print("plan:", plan)
    while q:
        n = q.popleft()
        visit(n)

    return list(plan)

    