import matplotlib.pyplot as plt
import numpy as np
import json



actual_dist = [[0, 5.49, 9.06, 20.67, 6.12, 14.44],
				[5.49, 0, 7.21, 19.92, 6.64, 19.93],
				[9.06, 7.21, 0, 12.71, 3.65,  21.19],
				[20.67, 19.92, 12.71, 0, 14.57, 28.18],
				[6.12, 6.64, 3.65, 14.57, 0, 17.55],
				[14.44, 19.93, 21.19, 28.18, 17.55, 0]]

measured_dist = []

node_coords = [[14.44, 19.92], [19.93, 19.92], [19.93, 12.71], [19.93, 0.0], [16.0, 13.0], [0.0, 19.92]]

node_name = ['03', '06', '07', '10', '12', '16']

if __name__=="__main__":

	file = "distance_matrix.json"

	with open(file, 'r') as f:
		measured_dist = json.load(f)
	
	x = [1,2,3,4,5,6]
	i = 0
	for row in measured_dist:
		j = 0
		act_dist_col = actual_dist[i]
		print(row)
		for col in row:
			if i != j:
				plt.plot(x[i], (col/100)/act_dist_col[j], marker="o")
				#plt.plot(x[i], act_dist_col[j], marker="o")

				plt.annotate(str(node_name[i])+"-"+str(node_name[j]), (x[i], (col/100)/act_dist_col[j]))
				#plt.annotate("act_"+str(node_name[i])+"-"+str(node_name[j]), (x[i], act_dist_col[j]))
			j = j+1
		i = i+1

		
	plt.xticks(x, ['raspi03', 'raspi06', 'raspi07', 'raspi10', 'raspi12', 'raspi16'])
	plt.xlabel('Anchors')

	plt.ylabel('Measured Distance(meters)')
	plt.show()

