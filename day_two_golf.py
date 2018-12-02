with open('inputDay2.txt') as f:
    lines = f.readlines()
from collections import Counter
# part 1
c = [0, 0]
for i in lines:
    a = [j for i,j in Counter(i).most_common()]
    if 3 in a:
        c[0] += 1
    if 2 in a:
        c[1] += 1
print(c[0] * c[1])

# part 2
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
			print("answer: ", ''.join(answer))