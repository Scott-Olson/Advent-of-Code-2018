data = open('input5.txt').read()
# test input
test = 'dabAcCaCBAcCcaDA'
lines = data.sort()

new = data
count = 1
cycles = 0

# this is removing pairs, but very slowly
# should retool to sort through once, mark all the pairs, then remove them at once
while count > 0:
	temp = new
	count = 0
	print("\n\n pre-count: \n\n", count)
	for i in range(0, len(new)-2):
		print(len(new))
		cycles += 1
		temp1 = temp[i]
		temp2 = temp[i+1]
		if temp1 == temp2.upper() or temp1 == temp2.lower():
			new = temp[0:i] + temp[i+2:len(temp)]
			count += 1
			# print("count: ", count)
print(len(new))
