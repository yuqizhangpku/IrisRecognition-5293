'''
filtering the iris and extracting features
'''

import cv2
import numpy as np
from ImageEnhancement import ImageEnhancement

def getkernal(thetax, thetay):
	res_mat = np.zeros((40, 40))
	for x in range(40):
		for y in range(40):
			M = np.cos(2*np.pi*np.sqrt(x*x+y*y))
			G = 1/(2*np.pi*thetax*thetay)*np.exp(-1/2*(x*x/(thetax*thetax)+y*y/(thetay*thetay)))*M
			res_mat[x,y] = G
	return res_mat

# def FeatureExtraction(image, init_angle=0):
# 	features = []
# 	feature_image = ImageEnhancement(image, init_angle)
# 	feature_image = feature_image[0:32, 0:512]
# 	kernel = getkernal(3, 1.5)
# 	feature_mat = cv2.filter2D(feature_image,-1,kernel)
# 	for i in range(0, 32, 8):
# 		for j in range(0, 512, 8):
# 			m = 0.0
# 			for k in range(8):
# 				for l in range(8):
# 					m += np.abs(feature_mat[i+k][j+l])
# 			m /= 64
# 			theta = 0.0
# 			for k in range(8):
# 				for l in range(8):
# 					theta += np.abs(np.abs(feature_mat[i+k][j+l])-m)
# 			theta /= 64
# 			features.append(m)
# 			features.append(theta)
# 	kernel = getkernal(4.5, 1.5)
# 	feature_mat = cv2.filter2D(feature_image,-1,kernel)
# 	for i in range(0, 32, 8):
# 		for j in range(0, 512, 8):
# 			m = 0.0
# 			for k in range(8):
# 				for l in range(8):
# 					m += np.abs(feature_mat[i+k][j+l])
# 			m /= 64
# 			theta = 0.0
# 			for k in range(8):
# 				for l in range(8):
# 					theta += np.abs(np.abs(feature_mat[i+k][j+l])-m)
# 			theta /= 64
# 			features.append(m)
# 			features.append(theta)
# 	return features

# def FeatureExtraction(image, init_angle=0):
# 	features = []
# 	feature_image = ImageEnhancement(image, init_angle)
# 	feature_image = feature_image[0:40, 0:512]
# 	kernel = getkernal(3, 1.5)
# 	feature_mat = cv2.filter2D(feature_image,-1,kernel)
# 	for i in range(0, 40, 8):
# 		for j in range(0, 512, 8):
# 			m = 0.0
# 			for k in range(8):
# 				for l in range(8):
# 					m += np.abs(feature_mat[i+k][j+l])
# 			m /= 64
# 			theta = 0.0
# 			for k in range(8):
# 				for l in range(8):
# 					theta += np.abs(np.abs(feature_mat[i+k][j+l])-m)
# 			theta /= 64
# 			features.append(m)
# 			features.append(theta)
# 	kernel = getkernal(4.5, 1.5)
# 	feature_mat = cv2.filter2D(feature_image,-1,kernel)
# 	for i in range(0, 40, 8):
# 		for j in range(0, 512, 8):
# 			m = 0.0
# 			for k in range(8):
# 				for l in range(8):
# 					m += np.abs(feature_mat[i+k][j+l])
# 			m /= 64
# 			theta = 0.0
# 			for k in range(8):
# 				for l in range(8):
# 					theta += np.abs(np.abs(feature_mat[i+k][j+l])-m)
# 			theta /= 64
# 			features.append(m)
# 			features.append(theta)
# 	return features

def FeatureExtraction(image, init_angle=0):
	features = []
	feature_image = ImageEnhancement(image, init_angle)
	feature_image = feature_image[0:48, 0:512]
	kernel = getkernal(3, 1.5)
	feature_mat = cv2.filter2D(feature_image,-1,kernel)
	for i in range(0, 48, 8):
		for j in range(0, 512, 8):
			m = 0.0
			for k in range(8):
				for l in range(8):
					m += np.abs(feature_mat[i+k][j+l])
			m /= 64
			theta = 0.0
			for k in range(8):
				for l in range(8):
					theta += np.abs(np.abs(feature_mat[i+k][j+l])-m)
			theta /= 64
			features.append(m)
			features.append(theta)
	kernel = getkernal(4.5, 1.5)
	feature_mat = cv2.filter2D(feature_image,-1,kernel)
	for i in range(0, 48, 8):
		for j in range(0, 512, 8):
			m = 0.0
			for k in range(8):
				for l in range(8):
					m += np.abs(feature_mat[i+k][j+l])
			m /= 64
			theta = 0.0
			for k in range(8):
				for l in range(8):
					theta += np.abs(np.abs(feature_mat[i+k][j+l])-m)
			theta /= 64
			features.append(m)
			features.append(theta)
	return features

if __name__ == "__main__":
	features = []
	image = cv2.imread('./CASIA Iris Image Database (version 1.0)/102/1/102_1_2.bmp',0)
	feature_image = ImageEnhancement(image)
	feature_image = feature_image[0:32, 0:512]
	cv2.imshow('test', feature_image)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
	kernel = getkernal(3, 1.5)
	feature_mat = cv2.filter2D(feature_image,-1,kernel)
	for i in range(0, 32, 8):
		for j in range(0, 512, 8):
			m = 0.0
			for k in range(8):
				for l in range(8):
					m += np.abs(feature_mat[i+k][j+l])
			m /= 64
			theta = 0.0
			for k in range(8):
				for l in range(8):
					theta += np.abs(np.abs(feature_mat[i+k][j+l])-m)
			theta /= 64
			features.append(m)
			features.append(theta)
	kernel = getkernal(4.5, 1.5)
	cv2.imshow('result1', feature_mat)
	feature_mat = cv2.filter2D(feature_image,-1,kernel)
	for i in range(0, 32, 8):
		for j in range(0, 512, 8):
			m = 0.0
			for k in range(8):
				for l in range(8):
					m += np.abs(feature_mat[i+k][j+l])
			m /= 64
			theta = 0.0
			for k in range(8):
				for l in range(8):
					theta += np.abs(np.abs(feature_mat[i+k][j+l])-m)
			theta /= 64
			features.append(m)
			features.append(theta)
	# print len(features)
	cv2.imshow('result2', feature_mat)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
