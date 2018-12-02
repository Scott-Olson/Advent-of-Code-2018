with open('input.txt') as f:
    parsed = f.readlines()
# Part 1
# input data from AoC
# take data as string, split the string on the line breaks "\n"
# set a charge varaible -> point of the AoC is to take the data and add it up to see the current charge
# iterate through the split data
# sum the data
# return the sum
charge = 0
for i in parsed:
    charge = charge + int(i)        
print(charge)

# Part 2
# input data from AoC
# take data as string, split the string on the line breaks "\n"
# set a charge varaible -> point of the AoC is to take the data and add it up to see when a charge repeats during the calibratoin
# store the seen frequencies
# set a repeat flag
# count cycles for fun and safety net
# iterate through the parsed data
# sum the charge
# check if we have seen the charge before in the freqTable
# if so, return that
freqRepeat = False
freqTable = []
charge = 0
cycles = 0
while not freqRepeat:
	for i in parsed:
		cycles += 1
		
		if cycles > 1000000:
			print("repeat not found, run")
			freqRepeat = True
		charge = charge + int(i)
		print("cycles/charge", cycles, charge)

		if charge in freqTable:
			print("repeat found: ", charge)
			freqRepeat = True
			break

		freqTable.append(charge)

		

