with open('input3.txt') as f:
    parsed = f.readlines()
import numpy as np
import pprint

# part 1
ids = []
first = []
second = []
x = []
y = []
for line in parsed:
	ids.append(int(line[line.find("#")+1:line.find("@")]))
	first.append(int(line[line.find("@")+1:line.find(",")]))
	second.append(int(line[line.find(",")+1:line.find(":")]))
	x.append(int(line[line.find(":")+1:line.find("x")]))
	y.append(int(line[line.find("x")+1:line.find("\n")]))

width = int(max(first)) + int(max(x))
height = int(max(second)) + int(max(y))


print("width: ", width)
print("height: ", height)

fabric = np.full((width, height), 0)

for idx in range(0, len(parsed)):
	for m in range(0, y[idx]):
		for i in range(0, x[idx]):
			fabric[second[idx] + m][first[idx] + i] += 1
			
test = fabric[ np.where(fabric > 1) ]
print(len(test))
# 111630 is correct answer

fabMax = 0
for k in range(0, len(fabric)):
	if np.amax(fabric[k]) > fabMax:
		fabMax = np.amax(fabric[k])
print("fabric max: ", fabMax)


#part 2
cloth = [[[] for j in range(1020)] for i in range(1020)]

for t in range(0, len(parsed)):
	for g in range(0, y[t]):
		for d in range(0, x[t]):
			cloth[second[t] + g][first[t] + d].append(ids[t])

helpMe = []

for row in cloth:
	for col in row:
		if len(col) == 1:
			helpMe.append(col)

for entry in range(0, len(ids)):
	if helpMe.count([ids[entry]]) == (x[entry] * y[entry]):
		print("found er: ", ids[entry])




# taylor = 
# pprint.pprint(taylor)

# print(id(taylor[0][0]))
# print(id(taylor[0][1]))


