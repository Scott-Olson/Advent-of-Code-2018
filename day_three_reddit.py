import numpy as np
with open('input3.txt') as f:
    parsed = f.readlines() 
SIZE = 1000

def parse_claim(s):
    identifier, _, dist, size = s.split(' ')
    fromleft, fromtop = map(int, dist[:-1].split(','))
    width, height = map(int, size.split('x'))
    return identifier, fromleft, fromtop, width, height

def p1(d):
    rect = np.zeros((SIZE, SIZE))
    for claim in d:
         iden, leftoff, topoff, w, h = parse_claim(claim)
         rect[leftoff:leftoff + w, topoff:topoff+h] += 1
    return np.size(np.where(rect >= 2)[0])

def p2(d):
    rect = np.zeros((SIZE, SIZE))
    for claim in d:
        iden, leftoff, topoff, w, h = parse_claim(claim)
        rect[leftoff:leftoff + w, topoff:topoff+h] += 1
    for claim in d:
        iden, leftoff, topoff, w, h = parse_claim(claim)
        if np.all(rect[leftoff:leftoff + w, topoff:topoff+h] == 1):
            return iden

print(p1(parsed))
print(p2(parsed))
