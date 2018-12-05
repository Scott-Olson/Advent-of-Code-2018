lines = open('input4.txt').read().split('\n')
import numpy as np
import pprint


data = []
# structure: each entry should have date, guard #, and 

guards = []
for line in lines:
	if "Guard" in line:
		print(line)
		guards.append(line[line.find("#")+1:line.find("\s")])

print(guards)