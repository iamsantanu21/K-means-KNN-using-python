from math import sqrt
import random

class KMEANS:
	#Function for the K-Means algorithm
	def kmeans(self):
		print("The dataset is:")
		print(*self.data, sep = "\n")
		self.k = int(input("No. of clusters (K) = "))
		c = [
			[] for _ in range(self.k)
		]
		print("Enter ",self.k," centroids as follows:")
		for i in range(self.k):
			x,y = input("centroid {0} = " .format(i+1)).split(",")
			c[i] = [int(x),int(y)]
		print("The initial centroids are : ", *c, sep = "\n")
		cluster, length = self.clustering(c)
		ncluster = pcluster = cluster
		for n in range(10):
			if(0  in length):
				print("\noptimal position reached:")
				print("\nThe optimal clusters are:")
				print(*pcluster, sep="\n")
				break
			else:
				cnew = self.means(ncluster, length)
				if c==cnew:
					print("\noptimal position reached:")
					print("\nThe optimal clusters are:")
					print(*ncluster, sep="\n")
					break;
				else:
					c=cnew
					pcluster = ncluster
					ncluster,length =  self.clustering(c)
		
		return cluster

	#Function for clustering the dataset
	def clustering(self,c):
		cl=[ 
			[]	for _  in range(self.k)
		]
		length=[]
		for i in range(self.k):
			l=0
			for j in self.data:
				if(self.check(j,c)==i):
					cl[i].append(j)
					l+=1
			length.append(l)
		return cl, length

	#Function for finding new centroids
	def means(self,cluster,length):
		c=[[ [] for _ in range(2) ] for _ in range (self.k)]
		sx=sy=0
		for i in range(len(c)):
			for j in range(length[i]):
				sx,sy = sx+cluster[i][j][0],sy+cluster[i][j][1]
			c[i] = [sx/length[i],sy/length[i]]
		return c
	'''Function for finding the cluster number
	for a certain point'''
	def check(self,point,c):
		d=[]
		[x,y]=point[:]
		for i in range(len(c)):
			[x1,y1] = c[i]
			d.append(sqrt(((x-x1)**2)+((y-y1)**2)))
		return d.index(min(d))

class KNN:
	def knn(self):
		print("\nThe distance between the test value and the trained value:")
		dis = []
		for cluster in self.dataset:
			for point in cluster:
				d = self.euclidean_distance(point)
				dis.append(d)
				print(point," : ",round(d,4))
		self.dist = dis
		neighbour_value=int(input("\nHow many neighbours do you want?: "))

		print("\nThe {0} neighbours of {1} are:" .format(neighbour_value,self.test_data))
		self.neighbours = self.get_neighbours(neighbour_value)
		for neighbour in self.neighbours:
			print(neighbour[0]," of class ",neighbour[1])

		self.cls = self.predict_classification()
	'''Function for  finding the distance bewtween
	the test_data and the points in the dataset'''
	def euclidean_distance(self, point2):
		distance = 0.0
		for i in range(len(self.test_data)-1):
			distance = distance + (self.test_data[i] - point2[i])**2
		return sqrt(distance)
	 
	'''Function for finding the nearest neighbours
	of the test_data point'''
	def get_neighbours(self, num_neighbors):
		distances = list()
		cluster_value = i = 0
		for cluster in self.dataset:
			cluster_value+=1
			for point in cluster:
				distances.append((point, self.dist[i], cluster_value))
				i+=1
		distances.sort(key=lambda tup: tup[1])
		neighbours = list()
		for i in range(0,num_neighbors):
			neighbours.append((distances[i][0],distances[i][2]))
		return neighbours
	 
	#Function for finding the class value of the test_data
	def predict_classification(self):
		output_values = [row[-1] for row in self.neighbours]
		prediction = max(set(output_values), key=output_values.count)
		return prediction



k1 = KMEANS()
k1.data = [
	[random.randrange(50),random.randrange(50)] for _ in range(20)
];
k1.cluster = k1.kmeans()

k2 = KNN()
k2.dataset = k1.cluster

print("\nThe reference dataset is:\n")
print(*k2.dataset, sep="\n")

x,y = input("Enter test data point:").split(",")
k2.test_data = [int(x),int(y)]
k2.knn()
print("\nThe Class Value of {0} is {1}: " .format(k2.test_data,k2.cls))