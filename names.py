#!/usr/bin/env python

import glob
import os
import random

# The Name database is a list of "popular" boys names, in order from 
# most to least popular. If you set a smaller limit (e.g. limit = 128), then
# it will just use the most popular 128 names.
limit = 512 

if not os.path.isfile('Round_1.txt'):
    infile = 'Name_database.txt'
    counter = 1
else:
    flist = glob.glob('Round*.txt')
    flist = sorted(flist)
    infile = flist[-1]
    counter = int(infile[-5]) + 1

outfile = 'Round_%d.txt' % counter

f = open(infile,'r')
names = f.read().split('\n')
f.close()

lines = len(names)
if lines > limit:
    lines = limit
if lines % 2 == 1:
    lines -= 1
assert lines >= 2, 'There must be at least 2 names'

print('Round %d:' % counter)
print(lines, 'Names to choose from')
print('-----------------------')

names = names[:lines]
random.shuffle(names)
ndraw = int(lines / 2)

fo = open(outfile,'w')
for i in range(ndraw):
    name1 = names[2*i]
    name2 = names[2*i+1]

    while True:
        print ('%s or %s? Enter 1 or 2' % (name1, name2))
        nn = input()
        nn = str(nn)
        if nn=='1':
            fo.write(name1 + '\n')
            break
        elif nn=='2':
            fo.write(name2 + '\n')
            break
        else:
            print ('Try again!')

fo.close()
