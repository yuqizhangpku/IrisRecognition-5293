'''
enhancing the normalized iris
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
from IrisNormalization import IrisNormalization

def get_item(image, x, y):
	if x < 0:
		x = abs(x) -1
	if y < 0:
		y = abs(y) -1
	if x >= image.shape[0]:
		x = image.shape[0] - x%image.shape[0] - 1
	if y >= image.shape[1]:
		y = image.shape[1] - y%image.shape[1] - 1
	return image[x, y]

def getw(x):
	a = -0.5
	x_1 = np.abs(x)
	if x_1 <= 1:
		return (a+2)*x_1**3 + (a+3)*x_1**2 + 1
	elif x > 1 and x < 2:
		return a*x_1**3 + 5*a*x_1**2 + 8*a*x_1 - 4*a
	else:
		return 0

def bicubicinterpolation(image, M, N):
	size = (w, h, channels) = (M, N, 1)
	res_image = np.empty(size, dtype=np.uint8)


	oM, oN = image.shape
	for i in range(M):
		for j in range(N):
			cor_i = (i+0.0)*M/oM
			cor_j = (j+0.0)*N/oN

			int_i = int(cor_i)
			int_j = int(cor_j)

			tmp_p = 0.0
			for ii in range(int_i, int_i+4):
				for jj in range(int_j, int_j+4):
					w = getw(cor_i - ii) * getw(cor_j - jj)
					p = get_item(image, jj, ii) * w
					tmp_p += p

			res_image[i][j] = tmp_p
	# cv2.imshow('result', res_image)
	return res_image

def ImageEnhancement(image, init_angle=0):
	Nor_image = IrisNormalization(image, init_angle)
	# lig_image = bicubicinterpolation(image, 64, 512)
	res_image = cv2.equalizeHist(Nor_image)
	print res_image.shape
	return res_image

if __name__ == "__main__":
	image = cv2.imread('./CASIA Iris Image Database (version 1.0)/098/1/098_1_2.bmp',0)
	print image.shape
	Nor_image = IrisNormalization(image)
	# lig_image = bicubicinterpolation(image, 64, 512)
	equ = cv2.equalizeHist(Nor_image)
	# res = np.hstack((Nor_image,equ))
	# plt.subplot(121),plt.imshow(Nor_image,'gray')
	# plt.subplot(122),plt.imshow(equ,'gray')
	cv2.imshow('original', Nor_image)
	cv2.imshow('result', equ)
	cv2.waitKey(0)
	cv2.destroyAllWindows()