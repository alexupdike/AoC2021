def part1():
    distance, depth = 0, 0
    commands = open('input.txt', 'r')
    commands = commands.read().splitlines()
    for command in commands:
        pair = command.split(" ")
        if (pair[0] == 'forward'):
            distance += int(pair[1])
        elif (pair[0] == 'down'):
            depth += int(pair[1])
        elif (pair[0] == 'up'):
            depth -= int(pair[1])
    return distance * depth

print('Part 1 results: ', part1())

def part2():
    distance, aim, depth = 0, 0, 0
    commands = open('input.txt', 'r')
    commands = commands.read().splitlines()
    for command in commands:
        pair = command.split(" ")
        if (pair[0] == 'forward'):
            distance += int(pair[1])
            depth += int(pair[1]) * aim
        elif (pair[0] == 'down'):
            aim += int(pair[1])
        elif (pair[0] == 'up'):
            aim -= int(pair[1])
    return distance * depth

print('Part 2 results: ', part2())