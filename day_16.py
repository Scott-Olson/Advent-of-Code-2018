import re
from collections import *
from itertools import *
from math import *

test = open('input16.txt').read().strip().split('\n\n\n')
lines = test[0].strip().split('\n')


def addr(R, a, b, c):
	R[c] = R[a] + R[b]


def addi(R, a, b, c):
	R[c] = int(R[a]) + b


def mulr(R, a, b, c):
	R[c] = R[a] * R[b]


def muli(R, a, b, c):
	R[c] = int(R[a]) + b


def banr(R, a, b, c):
	R[c] = R[a] & R[b]


def bani(R, a, b, c):
	R[c] = int(R[a]) & b 


def borr(R, a, b, c):
	R[c] = R[a] | R[b]


def bori(R, a, b, c):
	R[c] = int(R[a]) | b


def setr(R, a, b, c):
	R[c] = R[a]


def seti(R, a, b, c):
	R[c] = a


def gtir(R, a, b, c):
	if a > int(R[b]):
		R[c] = 1
	else: 
		R[c] = 0


def gtri(R, a, b, c):
	if int(R[a]) > b:
		R[c] = 1
	else:
		R[c] = 0


def gtrr(R, a, b, c):
	if R[a] > R[b]:
		R[c] = 1
	else:
		R[c] = 0


def eqir(R, a, b, c):
	if a == int(R[b]):
		R[c] = 1
	else: 
		R[c] = 0


def eqri(R, a, b, c):
	if int(R[a]) == b:
		R[c] = 1
	else:
		R[c] = 0


def eqrr(R, a, b, c):
	if R[a] == R[b]:
		R[c] = 1
	else:
		R[c] = 0


inst = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtrr, eqir, eqri, eqrr]
options = {}

def runTests(R, a, b, c):
	local = 0
	for m in inst:
		print(m)
		if m(R, a, b, c):
			print("worked somehow")
		else:
			print("no go")

	return local


count = 0
new = []
d = re.compile(r'\d+')
for i in range(0, len(lines), 4):
	reg = d.findall(lines[i])
	# print(reg)
	local = runTests(reg, int(reg[1]), int(reg[2]) ,int(reg[3]))


	if local >= 3:
		count += 1

print(count)


