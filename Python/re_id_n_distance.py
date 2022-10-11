import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json

path = "D:/Thesis/Testbed Results/RangingTest/RangingTest_06_12/"
jsonfile = path+"distance.json"
file = path+"log.txt"
hwid = ""
dist = -1
raspi03_dist = []
raspi06_dist = []
raspi07_dist = []
raspi10_dist = []
raspi12_dist = []
raspi16_dist = []

#hwids[4] = {"48d741a7", "1d5a2a62", "e732e3a5", "509a127c"}

f = open(file, mode='r', encoding='utf-8')

for line in f:
	for word in re.finditer(r"ID:\s\w+", line):
		#print(line[(word.start()+4):(word.end())])
		hwid = line[(word.start()+4):(word.end())]
	for word in re.finditer(r"Distance:\s\d*", line):
		#print(line[(word.start()+10):(word.end())])
		dist = int(line[(word.start()+10):(word.end())])
		if hwid == "48d741a7":
			if not(dist == 0):
				raspi03_dist.append(dist)
			#print(hwid+" : "+str(dist))
		elif hwid == "1c1b656e":
			if not(dist == 0):
				raspi06_dist.append(dist)
			#print(hwid+" : "+str(dist))
		elif hwid == "1d5a2a62":
			if not(dist == 0):
				raspi07_dist.append(dist)
			#print(hwid+" : "+str(dist))
		elif hwid == "e732e3a5":
			if not(dist == 0):
				raspi10_dist.append(dist)
			#print(hwid+" : "+str(dist))
		elif hwid == "66182c94":
			if not(dist == 0):
				raspi12_dist.append(dist)
			#print(hwid+" : "+str(dist))
		elif hwid == "509a127c":
			if not(dist == 0):
				raspi16_dist.append(dist)
			#print(hwid+" : "+str(dist))

dists = {}
		
dists = [raspi03_dist, raspi06_dist, raspi07_dist, raspi10_dist, raspi12_dist, raspi16_dist]

jsondata = {}

jsondata['raspi03'] = raspi03_dist
jsondata['raspi06'] = raspi06_dist
jsondata['raspi07'] = raspi07_dist
jsondata['raspi10'] = raspi10_dist
jsondata['raspi12'] = raspi12_dist
jsondata['raspi16'] = raspi16_dist

with open(jsonfile, 'w') as f:
	json.dump(jsondata, f)


x = [1,2,3,4,5,6]


#df = pd.DataFrame(dists, columns=['raspi03', 'raspi06', 'raspi07', 'raspi10', 'raspi12', 'raspi16'])
#df.plot.box()
bp = plt.boxplot(dists, showmeans=True)

medians = [round(item.get_ydata()[0], 1) for item in bp['medians']]
means = [round(item.get_ydata()[0], 1) for item in bp['means']]



plt.xticks(x, ['raspi03', 'raspi06', 'raspi07', 'raspi10', 'raspi12', 'raspi16'])
plt.xlabel('Anchors')

plt.ylabel('Measured Distance(cm)')

#plt.set_yticklabels([10])
#plt.plot(x, dists)
#plt.plot(x, y)

plt.show()
	