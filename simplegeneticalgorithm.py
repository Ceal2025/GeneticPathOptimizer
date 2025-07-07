import random

def calculatetakentime(route):
    takentime = 0
    size = 5
    for i in range(len(route) - 1):
        a, b = route[i], route[i + 1]
        diff = min(abs(a - b), size - abs(a - b))
        takentime += 1 if diff == 1 else 2
    return takentime

def findbesttwo(populationsize, locations):
    results = []
    for _ in range(populationsize):
        route = random.sample(locations, len(locations))
        time = calculatetakentime(route)
        results.append((route, time))
        print(route, time)

    results.sort(key=lambda x: x[1])
    best1, best2 = results[0], results[1]
    print("fastest 1:", best1[0], "time:", best1[1])
    print("fastest 2:", best2[0], "time:", best2[1])
    return best1[0], best2[0]

def crossover(parent1, parent2):
    size = len(parent1)
    child = [-1] * size
    start, end = sorted(random.sample(range(size), 2))
    child[start:end+1] = parent1[start:end+1]

    p2idx = 0
    for i in range(size):
        if child[i] == -1:
            while parent2[p2idx] in child:
                p2idx += 1
            child[i] = parent2[p2idx]

    mutationrate = 0.3
    while random.random() < mutationrate:
        mutationtype = random.choice([1, 2, 3])
        if mutationtype == 1:
            i, j = random.sample(range(size), 2)
            child[i], child[j] = child[j], child[i]
        elif mutationtype == 2:
            child.reverse()
        elif mutationtype == 3:
            random.shuffle(child)

    return child

populationsize = 10
locations = list(range(5))
parent1, parent2 = findbesttwo(populationsize, locations)

generation = 0
while generation < 100:
    children = []
    for _ in range(populationsize - 2):
        child = crossover(parent1, parent2)
        time = calculatetakentime(child)
        children.append((child, time))

    combined = [(parent1, calculatetakentime(parent1)),
                (parent2, calculatetakentime(parent2))] + children
    combined.sort(key=lambda x: x[1])
    nextgeneration = combined[:populationsize]

    parent1, parent2 = nextgeneration[0][0], nextgeneration[1][0]
    avgtime = sum(t for _, t in nextgeneration) / populationsize

    print(f"\n{generation + 1} generation:")
    for route, time in nextgeneration:
        print(route, time)
    print("parent 1:", parent1)
    print("parent 2:", parent2)

    optimalcount = sum(1 for _, time in nextgeneration if time == 4)
    if optimalcount >= 6:
      break


    generation += 1
