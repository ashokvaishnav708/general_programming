#SF_BW_Test Plot
import matplotlib.pyplot as plt
import numpy as np
import re
import statistics as stats
import itertools as iter

LoS = 1
N_LoS = 2

BWs = [400, 800, 1600]

SFs = [5, 6, 7, 8, 9, 10]

class BW_SF:
	def __init__(self, BW, SF, Dist):
		self.BW = BW
		self.SF = SF
		self.Dist = Dist


####################################################################
def myplot(X, Y, Z):

    nx, ny, nz = len(X), len(Y), len(Z)
    zmin = min(Z)

    if nx*ny!=nz: 
        print("invalid inputs: len(x)*len(y) should be equal to len(z)")
        return

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    xdata = list(
        iter.chain(
            *iter.repeat(X, ny)
        )
    )

    ydata = list(
        iter.chain(
            *(list(iter.repeat(y, nx)) for y in Y)
        )
    )

    ax.scatter3D(xdata, ydata, Z, c='orange', alpha=0.5)

    #tempZ = np.array(Z)

    ax.plot_trisurf(xdata, ydata, Z, color='green', alpha=0.10)

    for i, y in enumerate(Y):
        ax.plot3D(X, list(iter.repeat(y, nx)), Z[i*nx:(i+1)*nx], c='orange', alpha=0.5)

    for i, x in enumerate(X):
        ax.plot3D(list(iter.repeat(x, ny)), Y, Z[i::nx], c='orange', alpha=0.5)

    for (x, y, z) in zip(xdata, ydata, Z):
        ax.plot3D([x, x], [y, y], [zmin, z], c='orange', alpha=0.5)

    ax.set_xticks(X)
    ax.set_yticks(Y)
    ax.set_ylim(ymin=min(Y), ymax=max(Y))
    ax.set_xlim(xmin=min(X), xmax=max(X))
    ax.set_zlim(min(Z), max(Z))
    ax.set_xlabel('Spreading Factor')
    ax.set_ylabel('Bandwidths(MHz.')
    ax.set_zlabel('Distance error(meters)')

    plt.show()

################################################################################
def getErrVal(type):
	bw_counter = 0
	sf_counter = 0

	test_no = 0

	if (type == N_LoS):
		test_no = 8014
	if (type == LoS):
		test_no = 1

	actual_dist = 2000

	data = []

	for i in range(18):

		path = ""
		if (type == N_LoS):
			path = "D:/Thesis/Testbed Results/RangingTest_SF_BW/"+str(test_no + i)+"_SF_BW_Test/logs/raspi06/log.txt";
		if (type == LoS):
			path = "D:/Thesis/Testbed Results/RangingTest_SF_BW/Temp/1 ("+str(test_no + i)+").log"

		file = open(path, mode='r', encoding='utf-8')

		dist = []

		sample = 0

		for line in file:
			for word in re.finditer(r"Dist:\s\d*", line):
				dist.append(int(line[(word.start()+6):(word.end())]))
				sample += 1
			# 	if (sample > 99):
			# 		break
			# else:
			# 	continue
			# break
		#print("Sample: ",sample)

		avg = stats.median(dist)

		#print(avg)	

		data.append(BW_SF(BWs[bw_counter], SFs[sf_counter], avg))
		sf_counter += 1
		if (sf_counter > 5):
			sf_counter = 0
			bw_counter += 1

	Err = []

	#print("Length: ", len(data))

	for each in data:
		Err.append((each.Dist - actual_dist)/100)

	print(Err)
	return Err

#Z = [1150.5, 812.0, 699.5, 298.0, -612.0, -1031.5, 330.0, 857.0, 1118.0, 1466.0, 1317.0, -617.0, 1452.5, 1975.0, 1934.0, 1402.5, 572.0, -265.0]

if __name__ == '__main__':
    
    #myplot(X = SFs, Y = BWs, Z = getErrVal(type = N_LoS))
    myplot(X = SFs, Y = BWs, Z = getErrVal(type = LoS))

