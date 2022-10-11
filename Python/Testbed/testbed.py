import matplotlib.pyplot as plt
import math
import numpy as np
import re
import statistics as stats
from matplotlib.patches import Circle

NODE_IDS = ['03', '06', '07', '10', '12', '16']

NODE_POSITION = [[2015,  135], [2730,  135], [2730, 1065], [2730, 2705], [2295,  875], [135,  135]] # 19: old x value: 1530

class Node:
	def __init__(self, node_id, x, y):
		self.node_id = node_id
		self.x = x
		self.y = y



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


def plot_nodes(map_path, radiuses=False):
	# init plot
	
    plt.subplot(111)
    plt.axis('off')
    plt.tight_layout()
    im = plt.imread(map_path)
    

    fig, ax = plt.subplots()
    ax.imshow(im)
    
    ratio = 2570/1992
    Nodes = []

    for i  in range(6):
    	Nodes.append(Node(NODE_IDS[i], NODE_POSITION[i][0], NODE_POSITION[i][1]))

    	ax.scatter(Nodes[i].x, Nodes[i].y, s=280, c='#1f77b4')

    	ax.annotate(NODE_IDS[i], (Nodes[i].x, Nodes[i].y), ha='center', va='center', weight='bold')

    	if radiuses:
    		circle = Circle((Nodes[i].x, Nodes[i].y), (radiuses[i] * ratio), fill=False)
    		ax.add_patch(circle)

    plt.show()

if __name__ == '__main__':

	path = 'D:/Thesis/Testbed Results/Indoor_Localization_v2.0/8050_indoor_ranging_12_16/logs/raspi12/'

	medians = getDistsMedianMeans(path)

	print(medians)



	path = 'D:/Projects/General Programming/Python/Testbed/floor_plan_kiel.png'

	

	dist = math.dist(NODE_POSITION[1], NODE_POSITION[5])
	#print(dist/ratio)
	plot_nodes(path, medians)