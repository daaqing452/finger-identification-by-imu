import matplotlib.pyplot as plt
import math
import numpy as np
import sys
import pickle
from utils import *

def read(f):
	a = []
	b = []
	c = []
	idx = 0
	while True:
		line = f.readline()
		if len(line) == 0: break
		arr = line[:-1].split(' ')
		if len(arr) < 14: continue
		if int(arr[1]) == 1: b.append(idx)
		c.append(int(arr[1]))
		a.append([float(arr[i]) for i in range(2, 14)])
		idx += 1
	return np.array(a).T, b, np.array(c)

filename = sys.argv[1]
outname = sys.argv[2]
f = open(filename, 'r')
a, b, c = read(f)

# b[193] -= 100
# c[b[193]] = 1

pickle.dump((a, b), open(outname, 'wb'))
print('tap num:', len(b))
f.close()

for i in range(a.shape[0]):
	pass
	# a[i] = highpass_filter(a[i])
	# a[i] = a[i] - a[i].mean()
	# a[i] = kalman_filter(a[i])

plt.figure(1)
porder = [0, 3, 1, 4, 2, 5, 6, 9, 7, 10, 8, 11]
for i in range(len(porder)):
	plt.subplot(6, 2, i+1)
	plt.plot(a[porder[i]])
	if i == 0: plt.plot((c * 0.1))

amp = 0.2
plt.figure(2)
for i in range(10):
	for j in range(12):
		now = a[j + 0, b[i]-30 : b[i]+30]
		now = (now - now.mean()) / now.std()
		plt.subplot(10, 12, i * 12 + j + 1)
		# plt.ylim(-amp, amp)
		plt.plot(now)

plt.show()