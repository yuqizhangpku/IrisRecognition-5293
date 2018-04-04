'''
mapping the iris from Cartesian coordinates to polar coordinates
'''

import cv2
import numpy as np
from IrisLocalization import IrisLocalization

def getcirclepointbyangle(circle, angle):
	x = circle[0]
	y = circle[1]
	r = circle[2]
	res_x = x + r * np.cos(angle)
	res_y = y + r * np.sin(angle) 
	return res_x, res_y

# def IrisNormalization(image, init_angle=0):
# 	big_circle, small_circle = IrisLocalization(image)
# 	size = (w, h, channels) = (64, 512, 1)
# 	res_img = np.zeros(size, np.uint8)
# 	height, weight = image.shape
# 	print height, weight
# 	# resume_img = np.zeros(image.shape, np.uint8)
# 	for i in range(w):
# 		for j in range(h):
# 			angle = init_angle+2*j*np.pi/(h*2)
# 			xp, yp = getcirclepointbyangle(small_circle, angle)
# 			xi, yi = getcirclepointbyangle(big_circle, angle)
# 			x = xp + (xi-xp)*i/w
# 			y = yp + (yi-yp)*i/w
# 			# print 'angle :' + str(angle)
# 			# print 'small : ' + str(xp) + ' ' + str(yp)
# 			# print 'big : ' + str(xi) + ' ' + str(yi)
# 			# print 'result : ' + str(x) + ' ' + str(y)
# 			res_img[i, j] = image[min(int(y), height-1), min(int(x), weight-1)]
# 			# resume_img[min(int(y), height-1), min(int(x), weight-1)] = image[min(int(y), height-1), min(int(x), weight-1)]
# 			# resume_img[min(int(yp), height-1), min(int(xp), weight-1)] = 255
# 			# resume_img[min(int(y), height-1), min(int(x), weight-1)] = 255
# 	# cv2.imshow('image', image)
# 	# cv2.imshow('draw', resume_img)
# 	# cv2.imshow('result', res_img), cv2.waitKey(0)
# 	# cv2.destroyAllWindows()
# 	return res_img

def IrisNormalization(image, init_angle=0):
	big_circle, small_circle = IrisLocalization(image)
	size = (w, h, channels) = (64, 512, 1)
	res_img = np.zeros(size, np.uint8)
	height, weight = image.shape
	print height, weight
	# resume_img = np.zeros(image.shape, np.uint8)
	for i in range(w):
		for j in range(h):
			angle = 0.0
			if j > h/4 and j < h/2:
				angle = init_angle+2*(j+3*h/4)*np.pi/(h*2)
			elif j >= h/2 and j < 3*h/4:
				angle = init_angle+2*(j+5*h/4)*np.pi/(h*2)
			else:
				angle = init_angle+2*j*np.pi/(h*2)
			xp, yp = getcirclepointbyangle(small_circle, angle)
			xi, yi = getcirclepointbyangle(big_circle, angle)
			x = xp + (xi-xp)*i/w
			y = yp + (yi-yp)*i/w
			# print 'angle :' + str(angle)
			# print 'small : ' + str(xp) + ' ' + str(yp)
			# print 'big : ' + str(xi) + ' ' + str(yi)
			# print 'result : ' + str(x) + ' ' + str(y)
			res_img[i, j] = image[min(int(y), height-1), min(int(x), weight-1)]
			# resume_img[min(int(y), height-1), min(int(x), weight-1)] = image[min(int(y), height-1), min(int(x), weight-1)]
			# resume_img[min(int(yp), height-1), min(int(xp), weight-1)] = 255
			# resume_img[min(int(y), height-1), min(int(x), weight-1)] = 255
	# cv2.imshow('image', image)
	# cv2.imshow('draw', resume_img)
	# cv2.imshow('result', res_img), cv2.waitKey(0)
	# cv2.destroyAllWindows()
	return res_img

if __name__ == "__main__":
	image = cv2.imread('./CASIA Iris Image Database (version 1.0)/056/2/056_2_2.bmp',0)
	IrisNormalization(image)