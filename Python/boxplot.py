
import re
import matplotlib.pyplot as plt
import numpy as np


file1 = "D:/Thesis/Samples/Outdoor/10_meters.txt"
file2 = "D:/Thesis/Samples/Outdoor/20_meters.txt"
file3 = "D:/Thesis/Samples/Outdoor/30_meters.txt"

files = [file1, file2, file3]

actual_dist = [400, 400]

dists = []
count = 0

for i in range(len(files)):
	f = open(files[i], mode='r', encoding='utf-8')
	temp_dists = []
	for line in f:
		count = count + 1

		if count == 6 :
			count = 0
			#print(line, end = '')
			for match in re.finditer(r'\s\d*\s', line):
				s=match.start()
				e=match.end()
				#print(line[(s+1):(e-1)])
				temp = int(line[(s+1):(e-1)])
				if temp > 5000: print(temp)
				temp_dists.append(temp)

	dists.append(temp_dists)

	f.close()
#print(dists)
#print(len(dists))
#x = []
#y = []
#for i in range(1, (len(dists)+1)):
	#x.append(i)
	#y.append(i)
#plt.bar(x, dists, color = 'green', width=0.1)
x = []

for i in range(len(dists)):
	x.append(i+1)


plt.boxplot(dists)
plt.xticks(x, ['400 cm', '400 cm', '1000cm'])
plt.xlabel('Actual Distance(cm)')
plt.ylabel('Measured Distance(cm)')
#plt.set_yticklabels([10])
#plt.plot(x, dists)
#plt.plot(x, y)
plt.show()

	



