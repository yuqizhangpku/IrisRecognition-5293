#encoding=utf8
'''
detecting pupil and outer boundary of iris
'''

import cv2
import numpy as np
# import matplotlib.pyplot as plt

def getimagecenter(image):
	height, width = image.shape[:2]
	return height/2, width/2

def getcenterregion(image, x, y):
	res = image[x-60:x+60, y-60:y+60]
	return res

def getimagecentroid(image):
	ret,thresh_img = cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
	print cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE, cv2.THRESH_BINARY
	# cv2.imshow('img_centroid2', thresh_img)
	# cv2.waitKey (0)  
	# cv2.destroyAllWindows()  
	image, contours, hierarchy = cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	M = None
	max_m00 = 0.0
	for i in contours:
		cnt = i
		tmp_M = cv2.moments(cnt)
		if tmp_M['m00'] > max_m00:
			M = tmp_M
			max_m00 = tmp_M['m00']

	# img_color1 = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
	# cv2.drawContours(img_color1,contours,-1,(0,0,255),3)  
	# cv2.imshow('debug',img_color1)
	# cv2.waitKey (0)  
	# cv2.destroyAllWindows()  

	# M = cv2.moments(cnt)

	print M

	cx = int(M['m01']/M['m00'])
	cy = int(M['m10']/M['m00'])

	return cx, cy

def IrisLocalization(image):
	'''
	localize the iris 
	'''
	x, y = getimagecenter(image)
	height, width = image.shape
	tmp_image = getcenterregion(image, x, y)
	x_1, y_1 = getimagecentroid(tmp_image)
	x = x-60+x_1
	y = y-60+y_1
	tmp_image = getcenterregion(image, x, y)
	x_1, y_1 = getimagecentroid(tmp_image)
	x = x-60+x_1
	y = y-60+y_1

	tmp_image = image[max(x-120,0):min(x+120, height), max(y-120,0):min(y+120,width)]
	tmp_image = cv2.GaussianBlur(tmp_image,(3,3),0)
	circles_tmp = cv2.HoughCircles(tmp_image,cv2.HOUGH_GRADIENT, dp=1,minDist=200,param1=100,param2=10,minRadius=90,maxRadius=250)
	big_circles = circles_tmp[0,:,:] # transform into 2-dimension
	big_circles = np.uint16(np.around(big_circles)) # round numbers
	big_circles[0][0] += max(y-120,0)
	big_circles[0][1] += max(x-120,0)

	tmp_image = image[max(x-60,0):min(x+60, height), max(y-60,0):min(y+60,width)]
	tmp_image = cv2.GaussianBlur(tmp_image,(3,3),0)  
	circles_tmp = cv2.HoughCircles(tmp_image,cv2.HOUGH_GRADIENT, dp=1,minDist=200,param1=220,param2=10,minRadius=10,maxRadius=90)
	small_circles = circles_tmp[0,:,:] # transform into 2-dimension
	small_circles = np.uint16(np.around(small_circles)) # round numbers
	small_circles[0][0] += max(y-60,0)
	small_circles[0][1] += max(x-60,0)

	return big_circles[0], small_circles[0]
	

if __name__ == "__main__":
	# load the image
	image = cv2.imread('./CASIA Iris Image Database (version 1.0)/098/1/098_1_2.bmp',0) # Black and white image
	height, width = image.shape
	x, y = getimagecenter(image)
	tmp_image = getcenterregion(image, x, y)
	# cv2.imshow('img', tmp_image)
	# cv2.waitKey (0)  
	# cv2.destroyAllWindows()  
	x_1, y_1 = getimagecentroid(tmp_image)
	print x_1, y_1
	x_1 = x-60+x_1
	y_1 = y-60+y_1
	print x_1, y_1
	tmp_image = getcenterregion(image, x_1, y_1)
	x = x_1
	y = y_1
	x_1, y_1 = getimagecentroid(tmp_image)
	x_1 = x-60+x_1
	y_1 = y-60+y_1
	print x_1, y_1
	tmp_image = getcenterregion(image, x_1, y_1)
	tmp_image = image[max(x_1-120,0):min(x_1+120, height), max(y_1-120,0):min(y_1+120,width)]

	tmp_image = cv2.GaussianBlur(tmp_image,(3,3),0)  
	# ret,tmp_image = cv2.threshold(tmp_image,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

	# big circle test
	cv2.imshow('img2', tmp_image)
	canny = cv2.Canny(tmp_image, 10, 100)  
 	cv2.imshow('Canny', canny)
 	cv2.waitKey (0)  
	cv2.destroyAllWindows()  

	circles1 = cv2.HoughCircles(tmp_image,cv2.HOUGH_GRADIENT, dp=1,minDist=600,param1=100,param2=10,minRadius=80,maxRadius=500)
	img_color1 = cv2.cvtColor(tmp_image, cv2.COLOR_GRAY2BGR)
	circles = circles1[0,:,:] # transform into 2-dimension
	circles = np.uint16(np.around(circles)) # round numbers
	for i in circles[:]: 
	    cv2.circle(img_color1,(i[0],i[1]),i[2],(255,0,0),5) # draw the circle
	    cv2.circle(img_color1,(i[0],i[1]),2,(255,0,255),10) # draw the center of the circle
	    print i[0], i[1], i[2]
	cv2.imshow('circle', img_color1)

	# small circle test
	# tmp_image = image[x_1-60:x_1+60, y_1-60:y_1+60]
	# tmp_image = cv2.GaussianBlur(tmp_image,(3,3),0)  

	# cv2.imshow('img2', tmp_image)
	# canny = cv2.Canny(tmp_image, 10, 220)  
 # 	cv2.imshow('Canny', canny) 

	# circles1 = cv2.HoughCircles(tmp_image,cv2.HOUGH_GRADIENT, dp=1,minDist=200,param1=220,param2=10,minRadius=10,maxRadius=90)
	# img_color1 = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
	# circles = circles1[0,:,:]#提取为二维
	# circles = np.uint16(np.around(circles))#四舍五入，取整
	# for i in circles[:]: 
	#     cv2.circle(img_color1,(y_1-60+i[0],x_1-60+i[1]),i[2],(255,0,0),5)#画圆
	#     cv2.circle(img_color1,(y_1-60+i[0],x_1-60+i[1]),2,(255,0,255),10)#画圆心
	# cv2.imshow('circle', img_color1)

	cv2.waitKey (0)  
	cv2.destroyAllWindows()  

	