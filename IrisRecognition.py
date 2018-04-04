'''
the main function, which will use all the following sub functions
'''

import sklearn
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import cv2
from FeatureExtraction import FeatureExtraction
from IrisMatching import IrisMatching
from PerformanceEvaluation import calculateCRR, calculateROC

def readfeature():
	f = open('feature48','r')
	train = []
	result = []
	line = f.readline()
	while line:
		spline = line.strip().split()
		tmp_line = []
		for i in spline[:-1]:
			tmp_line.append(float(i))
		train.append(tmp_line)
		result.append(float(spline[-1]))
		line = f.readline()
	f.close()
	return train, result

def readtest():
	f = open('test48','r')
	test = []
	result = []
	line = f.readline()
	while line:
		spline = line.strip().split()
		tmp_line = []
		for i in spline[:-1]:
			tmp_line.append(float(i))
		test.append(tmp_line)
		result.append(float(spline[-1]))
		line = f.readline()
	f.close()
	return test, result


if __name__ == "__main__":

	X, y = readfeature()
	T, r = readtest()

	Xresult = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
	yresult = []
	for i in Xresult:
		yresult.append(calculateCRR(X, y, T, r, i))
	calculateROC(X, y, T, r)

	plt.plot(Xresult, yresult)
	plt.show()  

	# lda = LinearDiscriminantAnalysis(n_components=100)
	# lda.fit(X,y)
	# X_new = lda.transform(X)

	# print 'start'
	# cnt = 0
	# now = 0
	# T, r = readtest()
	# total = len(r)/4
	# get = {}
	# T_new = lda.transform(T)
	# for i in range(len(r)):
	# 	res = IrisMatching(lda, X_new, y, T_new[i])
	# 	print res, r[i]
	# 	if float(res) == float(r[i]) and res not in get:
	# 		print 'get'
	# 		get[res] = 1
	# 		cnt += 1
	# 	print 'go' + str(now)
	# 	now += 1
	# print float(cnt)/total


