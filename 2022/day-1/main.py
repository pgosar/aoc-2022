totals = [0]
with open('in.txt') as file:
    for line in file:
        if line != '\n':
            totals[-1] += int(line)
        else:
            totals.append(0)
            total = 0

print(f"Part 1: {max(totals)}")
print(f"Part 2: {sum(sorted(totals)[-3:])}")
