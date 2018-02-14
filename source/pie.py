'''
	Created by Sidhant Nagpal
	Feb 1, 2018
'''

from matplotlib import pyplot as plt
from random import shuffle
import numpy as np
import json

plt.figure(figsize=(12,6))
data = json.load(open('data.json'))
a = [(k,v) for k, v in data.iteritems()]

for i in xrange(2,len(a)):
	if a[i-2]>a[i] and a[i-2]>a[i-1]:
		a[i-2], a[i] = a[i], a[i-2]
	elif a[i]>a[i-2] and a[i]>a[i-1]:
		a[i-1], a[i] = a[i], a[i-1]
values = [y for x, y in a]
probs = sum(values)
labels = ['{} ({}) ({:.1f}%)'.format(x,y,100.*y/probs) for x, y in a]

colors = ['crimson','lightcoral','darkcyan','green','coral','orange','seagreen','purple','gold','mediumvioletred','darkturquoise','greenyellow','indigo','limegreen']
shuffle(colors)
colors = colors[:len(a)]
patches, texts = plt.pie(values, colors=colors, rotatelabels=True, frame=True, shadow=True, startangle=100)
plt.axis('equal')
plt.title('Total Solved = {}'.format(probs), loc='left')
plt.legend(patches, labels, loc='lower right')
plt.tight_layout()
plt.show()