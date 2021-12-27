def part1():
    depthCounter, current, previous = 0, 0, 0

    with open("input.txt") as file:
        for line in file:
            current = line.rstrip()
            current = int(current)
            if current > previous and previous != 0:
                depthCounter += 1
            previous = current
        
    return depthCounter

print("Part 1 total: ", part1())

def part2():
    depthCounter, current, previous = 0, 0, 0
    
    file = open("input.txt", 'r')
    values = [int(x) for x in (file.read().splitlines())]

    for index in range(len(values)):
        if index >= 2:
            current = sum(values[index - 2:index + 1])
            if current > previous and previous != 0:
                depthCounter += 1
            previous = current

    return depthCounter

print("Part 2 total: ", part2())