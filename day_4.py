lines = open('input4_test.txt').read().split('\n')
import numpy as np
import pprint, re, datetime, collections
import dateutil
from dateutil.parser import *

lines.sort()


# data = []
# # structure: each entry should have date, guard #, and 

# re1='(\\[.*?\\])'	# Square Braces 1
# re2='.*?'	# Non-greedy match on filler
# re3='(\\d)'	# Any Single Digit 1
# re4='(\\d)'	# Any Single Digit 2
# re5='(\\d)'	# Any Single Digit 3
# re6='(\\d)' # Any Single Digit 4

# rg = re.compile(re1+re2+re3+re4+re5+re6,re.IGNORECASE|re.DOTALL)

# sort the entries by date and time
# the input is not sorted by default
# once the input is sorted use the below code to parse out components
# have the code to seperate the date, guard number, asleep/awake pattern

# print(lines)
# guards = []
# asleep = False
# for line in lines:
# 	m = rg.search(line)
# 	if m:
# 		print(m.group(1))
# 	hold = line.split()
# 	if "Guard" in line:
# 		guards.append(int(hold[3][1:len(hold)]))
# 	if "falls asleep" in line:
# 		asleep = True
# 		print("guard asleep")
# 	if ("wakes up" in line) and (asleep == True):
# 		asleep = False
# 		print("guard wakes up")

# print(guards)


from collections import defaultdict


guards = collections.defaultdict(list)
times = collections.defaultdict(int)
guard = None
for line in lines:
    time, action = line.split('] ')

    time = dateutil.parser.parse(time[1:])

    if action.startswith('Guard'):
        guard = int(action.split()[1][1:])
    elif action == 'falls asleep':
        start = time
    elif action == 'wakes up':
        end = time
        guards[guard].append((start.minute, end.minute))
        times[guard] += (end - start).seconds

(guard, time) = max(times.items(), key=lambda i: i[1])
(minute, count) = max([
    (minute, sum(1 for start, end in guards[guard] if start <= minute < end))
for minute in range(60)], key=lambda i: i[1])

print('part 1:', guard * minute)

(guard, minute, count) = max([
    (guard, minute, sum(1 for start, end in guards[guard] if start <= minute < end))
for minute in range(60) for guard in guards], key=lambda i: i[2])

print('part 2:', guard * minute)



