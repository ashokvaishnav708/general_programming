
import re
import matplotlib.pyplot as plt
import numpy as np


file = "D:/Thesis/Samples/Indoor/20_meters.txt"


actual_dist = 2000

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
			temp = int(line[(s+1):(e-1)])
			if temp > 5000: print(temp)
			dists.append(temp)

f.close()
#print(dists)
#print(len(dists))
#x = []
#y = []
#for i in range(1, (len(dists)+1)):
	#x.append(i)
	#y.append(i)
#plt.bar(x, dists, color = 'green', width=0.1)


plt.boxplot(dists)
plt.xticks([1], [actual_dist])
plt.xlabel('Actual Distance(cm)')
plt.ylabel('Measured Distance(cm)')
#plt.set_yticklabels([10])
#plt.plot(x, dists)
#plt.plot(x, y)


plt.savefig('20_meters.png')
plt.show()

	



