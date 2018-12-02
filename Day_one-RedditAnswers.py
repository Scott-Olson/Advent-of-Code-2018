import itertools
data = [int(x) for x in open("input.txt").readlines()]
# part 1 - functional
print(sum(data))
# part 2 - functional
freq = 0
seen = set([0])
for num in itertools.cycle(data):
    freq += num
    if freq in seen:
        print(freq); break
    seen.add(freq)


# alt methods
# part 1 - not working on the import of data
# inp = open("input.txt").readlines()
# lines = inp.splitlines()
# print(sum(map(int, lines)))
# # part 2
# lines = inp.splitlines()
# o = []
# s = 0
# for _ in range(1000000):
#     for i in map(int, lines):
#         s += i
#         if s in o:
#             print(s)
#             break
#         sprint(s)
#         o.append(s)


# Part 1
with open('input.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += int(line)

print("Part 1: " + str(count))

# Part 2
counts = set()
count = 0
ind = 0
while (True):
    count += int(lines[ind % len(lines)])
    if (count in counts):
        break
    counts.add(count)
    ind += 1

print("Part 2: " + str(count))


