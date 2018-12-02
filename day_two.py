with open('inputDay2.txt') as f:
    lines = f.readlines()

# part 1
countTwo = 0
countThree = 0
for line in lines:
	countDup = {}
	usedTwo , usedThree = (False,)*2
	for i in line:
			if i in countDup:
				countDup[i] = countDup[i] + 1
			else:
				countDup[i] = 1
	for m in countDup:
		if usedThree == False and countDup[m] == 3:
			usedThree = True
			countThree += 1
		if usedTwo == False and countDup[m] == 2:
			usedTwo = True
			countTwo += 1
print(countTwo * countThree)

# Part 2
for y in lines:
	for x in lines:
		diff = 0
		for i in range(len(x)-1):
			if x[i] != y[i]:
				diff += 1
		if diff == 1:
			answer = []
			for t in range(len(x)):
				if x[t] == y[t]:
					answer.append(x[t])
			print(x,y)
			print("answer: ", ''.join(answer))

 






