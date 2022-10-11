
import re
import matplotlib.pyplot as plt
import numpy as np

file = "D:/Thesis/Samples/Indoor/04_meter.txt"
actual_dist = 400

try:
	dists = []
	count = 0
	f = open(file, mode='r', encoding='utf-8')
	for line in f:
		count = count + 1

		if count == 6 :
			count = 0
			#print(line, end = '')
			for match in re.finditer(r'\s\d*\s', line):
				s=match.start()
				e=match.end()
				#print(line[(s+1):(e-1)])
				dists.append(int(line[(s+1):(e-1)]))

	#print(dists)
	#print(len(dists))
	x = []
	y = []
	for i in range(1, (len(dists)+1)):
		x.append(i)
		y.append(actual_dist)
	plt.bar(x, dists, color = 'green', width=0.1)
	#plt.plot(x, dists)
	plt.plot(x, y)
	plt.show()

finally:
	f.close()



