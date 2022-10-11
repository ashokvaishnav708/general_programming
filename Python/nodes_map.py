import re
import matplotlib.pyplot as plt
import numpy as np
import json


actual_dist = [[0, 5.49, 9.06, 20.67, 6.12, 14.44],
				[5.49, 0, 7.21, 19.92, 6.64, 19.93],
				[9.06, 7.21, 0, 12.71, 3.65,  21.19],
				[20.67, 19.92, 12.71, 0, 14.57, 28.18],
				[6.12, 6.64, 3.65, 14.57, 0, 17.55],
				[14.44, 19.93, 21.19, 28.18, 17.55, 0]]


mesaured_dist = []
row = []



def get_hwid(num):
	if num == 0:
		return "48d741a7"
	elif num == 1:
		return "1c1b656e"
	elif num == 2:
		return "1d5a2a62"
	elif num == 3:
		return "e732e3a5"
	elif num == 4:
		return "66182c94"
	elif num == 5:
		return "509a127c"

def get_distances(file):

	raspi03_dist = []
	raspi06_dist = []
	raspi07_dist = []
	raspi10_dist = []
	raspi12_dist = []
	raspi16_dist = []
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
			
	dists = [raspi03_dist, raspi06_dist, raspi07_dist, raspi10_dist, raspi12_dist, raspi16_dist]
	return dists

def get_medians(file):

	dists = get_distances(file)
	bp = plt.boxplot(dists, showmeans=True)
	medians = [round(item.get_ydata()[0], 1) for item in bp['medians']]

	#print(medians)
	
	return medians

def get_means(file):
	dists = get_distances(file)
	bp = plt.boxplot(dists, showmeans=True)
	means = [round(item.get_ydata()[0], 1) for item in bp['means']]

	#print(medians)
	
	return means

def get_segregated(dists):
	data = {}
	data['03'] = dists[0]
	data['06'] = dists[1]
	data['07'] = dists[2]
	data['10'] = dists[3]
	data['12'] = dists[4]
	data['16'] = dists[5]

	return data

if __name__=="__main__":

	path = "D:/Thesis/Testbed Results/RangingTest/"
	file = path+"RangingTest_12_03/log.txt"
	row_03 = get_medians(file)

	file = path+"RangingTest_12_06/log.txt"
	row_06 = get_medians(file)

	file = path+"RangingTest_12_07/log.txt"
	row_07 = get_medians(file)

	file = path+"RangingTest_06_10/log.txt"
	row_10 = get_medians(file)

	file = path+"RangingTest_06_12/log.txt"
	row_12 = get_medians(file)

	file = path+"RangingTest_12_16/log.txt"
	row_16 = get_medians(file)



	file = path+"RangingTest_06_03/log.txt"
	tmp = get_medians(file)
	row_03[4] = tmp[4]

	file = path+"RangingTest_03_06/log.txt"
	tmp = get_medians(file)
	row_06[4] = tmp[4]

	file = path+"RangingTest_06_07/log.txt"
	tmp = get_medians(file)
	row_07[4] = tmp[4]

	#file = path+"RangingTest_12_06/distance.json"
	#tmp = get_medians(file)
	row_10[1] = row_06[3]

	file = path+"RangingTest_03_12/log.txt"
	tmp = get_medians(file)
	row_12[1] = tmp[1]

	file = path+"RangingTest_06_16/log.txt"
	tmp = get_medians(file)
	row_16[4] = tmp[4]


	json_file = path+"distance_matrix.json"
	jsondata = []

	jsondata.append(row_03)
	jsondata.append(row_06)
	jsondata.append(row_07)
	jsondata.append(row_10)
	jsondata.append(row_12)
	jsondata.append(row_16)

	#jsondata['03'] = get_segregated(row_03)
	#jsondata['06'] = get_segregated(row_06)
	#jsondata['07'] = get_segregated(row_07)
	#jsondata['10'] = get_segregated(row_10)
	#jsondata['12'] = get_segregated(row_12)
	#jsondata['16'] = get_segregated(row_16)

	with open(json_file, 'w') as f:
		json.dump(jsondata, f, indent=4) 