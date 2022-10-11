import matplotlib.pyplot as plt
import numpy as np
import re
import statistics as stats
from matplotlib.patches import Circle

figure, axis = plt.subplots(2,2)
##########################################################

path1 = "D:/Thesis/Testbed Results/RangingTest/RangingTest_12_03/"
path2 = "D:/Thesis/Testbed Results/RangingTest/RangingTest_12_06/"
path3 = "D:/Thesis/Testbed Results/RangingTest/RangingTest_12_07/"
path4 = "D:/Thesis/Testbed Results/RangingTest/RangingTest_12_16/"

title1 = "Locating RASPI03"
title2 = "Locating RASPI06"
title3 = "Locating RASPI07"
title4 = "Locating RASPI16"

def getDistsMedianMeans(path):
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
	medians = []
	means = []
	for dist in dists:
		if not dist:
			medians.append(float("nan"))
			means.append(float("nan"))
		else:
			medians.append(stats.median(dist))
			means.append(stats.mean(dist))

	#bp = axes.boxplot(dists, showmeans=True)

	#medians = [round(item.get_ydata()[0], 1) for item in bp['medians']]
	#means = [round(item.get_ydata()[0], 1) for item in bp['means']]

	return medians;


#plt.clf()


###########################################################


node_coords = [[14.44, 19.92], [19.93, 19.92], [19.93, 12.71], [19.93, 0.0], [16.0, 13.0], [0.0, 19.92]]
node_name = ['03', '06', '07', '10', '12', '16']

x = []
y = []

for node in node_coords:
	x.append(node[0])
	y.append(node[1])

path_idx = 0
paths = [path1, path2, path3, path4]
titles = [title1,title2, title3, title4]

for i in range(2):
	path_idx += i;
	for j in range(2):
		path_idx += j;

		#axis[i, j].axis(xmin=-2, xmax=22, ymin=-2, ymax=22)
		axis[i, j].set_title(titles[path_idx])
		medians = getDistsMedianMeans(paths[path_idx])
		axis[i, j].scatter(x, y, s=250, c='magenta')
		for k in range(len(node_name)):
			axis[i, j].annotate(node_name[k], (x[k], y[k]), ha='center', va='center')

			if (str(medians[k]) != 'nan'):
				#print(medians[i])

				circle = Circle((x[k], y[k]), (medians[k]/200), fill=False)
				axis[i, j].add_patch(circle)



plt.show()

