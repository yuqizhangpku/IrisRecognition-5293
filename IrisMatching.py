'''
using Fisher linear discriminant for dimension reduction and nearest center classifier for classification
'''
import sklearn
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import cv2
from FeatureExtraction import FeatureExtraction
# import matplotlib.pyplot as plt

def IrisMatching(lda, trainset, result, f, dis_function=1):
	min_dist = 10000000.0
	res = 0
	# f = lda.transform([target])[0]
	for i in range(len(result)):
		fi = trainset[i]
		dist = 0
		if dis_function == 1:
			dist = np.sum(np.abs(np.array(f)-np.array(fi)))
		elif dis_function == 2:
			dist = np.linalg.norm(np.array(f)-np.array(fi))
		elif dis_function == 3:
			dist = 1-(np.dot(fi, f)/(np.linalg.norm(fi)*np.linalg.norm(f)))
		if dist < min_dist:
			min_dist = dist
			res = result[i]
	return res

def IrisMatchingDist(lda, trainset, result, f, dis_function=1):
	min_dist = 10000000.0
	# f = lda.transform([target])[0]
	for i in range(len(result)):
		fi = trainset[i]
		dist = 0
		if dis_function == 1:
			dist = np.sum(np.abs(np.array(f)-np.array(fi)))
		elif dis_function == 2:
			dist = np.linalg.norm(np.array(f)-np.array(fi))
		elif dis_function == 3:
			dist = 1-(np.dot(fi, f)/(np.linalg.norm(fi)*np.linalg.norm(f)))
		if dist < min_dist:
			min_dist = dist
	return min_dist

if __name__ == "__main__":
	dir = './CASIA Iris Image Database (version 1.0)/'
	X = []
	y = []
	for p in range(1,109):
		for s in range(1, 5):
			image_dir = dir + '%03d/'%(p) + '2/' + '%03d_2_%d.bmp'%(p, s)
			print image_dir
			image = cv2.imread(image_dir, 0)
			fea = FeatureExtraction(image)
			X.append(fea)
			y.append(p)
			f = open('test48', 'a')
			result = ''
			for i in fea:
				result += str(i) + ' '
			f.write('%s %s\n'%(result, str(p)))
			f.close()


	# lda = LinearDiscriminantAnalysis(n_components=2)
	# lda.fit(X,y)
	# X_new = lda.transform(X)
	# plt.scatter(X_new[:, 0], X_new[:, 1],marker='o',c=y)
	# plt.show()

	# dir = './CASIA Iris Image Database (version 1.0)/'
	# X = []
	# y = []
	# for p in range(1, 109):
	# 	for s in range(1, 4):
	# 		image_dir = dir + '%03d/'%(p) + '1/' + '%03d_1_%d.bmp'%(p, s)
	# 		print image_dir
	# 		image = cv2.imread(image_dir, 0)
	# 		for init_angle in [0]:
	# 			fea = FeatureExtraction(image, init_angle)
	# 			X.append(fea)
	# 			y.append(p)
	# 			f = open('feature48_2', 'a')
	# 			result = ''
	# 			for i in fea:
	# 				result += str(i) + ' '
	# 			f.write('%s %s\n'%(result, str(p)))
	# 			f.close()

	# lda = LinearDiscriminantAnalysis(n_components=2)
	# lda.fit(X,y)
	# X_new = lda.transform(X)
	# plt.scatter(X_new[:, 0], X_new[:, 1],marker='o',c=y)
	# plt.show()
