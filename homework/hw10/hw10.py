"""
Computer Vision 2019 Fall
Homework #10
"""

import cv2, sys
import numpy as np 

def plot_img(img, filename, title):
	cv2.imwrite(filename, img)
	cv2.imshow(title, img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def zero_crossing(mask):
	padded_mask = np.pad(mask, 1, 'reflect')
	zero_crossing_img = np.zeros(mask.shape, dtype = np.uint8)
	for i in range(1, padded_mask.shape[0] - 1):
		for j in range(1, padded_mask.shape[1] - 1):
			if padded_mask[i][j] == 1 and -1 in padded_mask[i-1:i+2, j-1:j+2]:
				zero_crossing_img[i-1][j-1] = 0
			else:
				zero_crossing_img[i-1][j-1] = 255
	return zero_crossing_img

def laplacian(img, threshold):
	operator_l1 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
	operator_l2 = (1 / 3) * np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]]) 
	pad_width = operator_l1.shape[0] // 2
	padded_img = np.pad(img, pad_width, 'reflect')
	mask_l1 = np.zeros(img.shape, dtype = np.int8)
	mask_l2 = np.zeros(img.shape, dtype = np.int8)
	for i in range(pad_width, padded_img.shape[0] - pad_width):
		for j in range(pad_width, padded_img.shape[1] - pad_width):
			grad_magnitude = np.sum(np.multiply(operator_l1, 
					padded_img[i-pad_width:i+pad_width+1, j-pad_width:j+pad_width+1]))
			if grad_magnitude >= threshold:
				mask_l1[i-pad_width][j-pad_width] = 1
			elif grad_magnitude <= -threshold:
				mask_l1[i-pad_width][j-pad_width] = -1
			else:
				mask_l1[i-pad_width][j-pad_width] = 0

			grad_magnitude = np.sum(np.multiply(operator_l2, 
					padded_img[i-pad_width:i+pad_width+1, j-pad_width:j+pad_width+1]))
			if grad_magnitude >= threshold:
				mask_l2[i-pad_width][j-pad_width] = 1
			elif grad_magnitude <= -threshold:
				mask_l2[i-pad_width][j-pad_width] = -1
			else:
				mask_l2[i-pad_width][j-pad_width] = 0
	laplacian_img1 = zero_crossing(mask_l1)
	laplacian_img2 = zero_crossing(mask_l2)
	return laplacian_img1, laplacian_img2

def minimum_variance_laplacian(img, threshold):
	operator = (1 / 3) * np.array([[2, -1, 2], [-1, -4, -1], [2, -1, 2]])
	pad_width = operator.shape[0] // 2
	padded_img = np.pad(img, pad_width, 'reflect')
	mask = np.zeros(img.shape, dtype = np.int8)
	for i in range(pad_width, padded_img.shape[0] - pad_width):
		for j in range(pad_width, padded_img.shape[1] - pad_width):
			grad_magnitude = np.sum(np.multiply(operator, 
					padded_img[i-pad_width:i+pad_width+1, j-pad_width:j+pad_width+1]))
			if grad_magnitude >= threshold:
				mask[i-pad_width][j-pad_width] = 1
			elif grad_magnitude <= -threshold:
				mask[i-pad_width][j-pad_width] = -1
			else:
				mask[i-pad_width][j-pad_width] = 0
	mvl_img = zero_crossing(mask)
	return mvl_img

def laplacian_gaussian(img, threshold):
	operator = np.array([[0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0], 
						[0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0],
						[0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0],
						[-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1],
						[-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1],
						[-2, -9, -23, -1, 103, 178, 103, -1, -23, -9, -2],
						[-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1],
						[-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1],
						[0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0],
						[0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0],
						[0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0]])
	pad_width = operator.shape[0] // 2
	padded_img = np.pad(img, pad_width, 'reflect')
	mask = np.zeros(img.shape, dtype = np.int8)
	for i in range(pad_width, padded_img.shape[0] - pad_width):
		for j in range(pad_width, padded_img.shape[1] - pad_width):
			grad_magnitude = np.sum(np.multiply(operator, 
			  		padded_img[i-pad_width:i+pad_width+1, j-pad_width:j+pad_width+1]))
			if grad_magnitude >= threshold:
				mask[i-pad_width][j-pad_width] = 1
			elif grad_magnitude <= -threshold:
				mask[i-pad_width][j-pad_width] = -1
			else:
				mask[i-pad_width][j-pad_width] = 0
	laplacian_gaussian_img = zero_crossing(mask)
	return laplacian_gaussian_img

def difference_gaussian(img, threshold):
	operator = np.array([[-1, -3, -4, -6, -7, -8, -7, -6, -4, -3, -1],
						[-3, -5, -8, -11, -13, -13, -13, -11, -8, -5, -3],
						[-4, -8, -12, -16, -17, -17, -17, -16, -12, -8, -4],
						[-6, -11, -16, -16, 0, 15, 0, -16, -16, -11, -6],
						[-7, -13, -17, 0, 85, 160, 85, 0, -17, -13, -7],
						[-8, -13, -17, 15, 160, 283, 160, 15, -17, -13, -8],
						[-7, -13, -17, 0, 85, 160, 85, 0, -17, -13, -7],
						[-6, -11, -16, -16, 0, 15, 0, -16, -16, -11, -6],
						[-4, -8, -12, -16, -17, -17, -17, -16, -12, -8, -4],
						[-3, -5, -8, -11, -13, -13, -13, -11, -8, -5, -3],
						[-1, -3, -4, -6, -7, -8, -7, -6, -4, -3, -1]])
	pad_width = operator.shape[0] // 2
	padded_img = np.pad(img, pad_width, 'reflect')
	mask = np.zeros(img.shape, dtype = np.int8)
	for i in range(pad_width, padded_img.shape[0] - pad_width):
		for j in range(pad_width, padded_img.shape[1] - pad_width):
			grad_magnitude = np.sum(np.multiply(operator, 
			  		padded_img[i-pad_width:i+pad_width+1, j-pad_width:j+pad_width+1]))
			if grad_magnitude >= threshold:
				mask[i-pad_width][j-pad_width] = 1
			elif grad_magnitude <= -threshold:
				mask[i-pad_width][j-pad_width] = -1
			else:
				mask[i-pad_width][j-pad_width] = 0
	difference_gaussian_img = zero_crossing(mask)
	return difference_gaussian_img

if __name__ == '__main__':
	img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
	length, width = img.shape[0], img.shape[1]

	if sys.argv[2] == '1':
		laplacian_img1, laplacian_img2 = laplacian(img, 15)
		plot_img(laplacian_img1, 'laplacian_1.bmp', 'Laplacian_1')
		plot_img(laplacian_img2, 'laplacian_2.bmp', 'Laplacian_2')
	elif sys.argv[2] == '2':
		minimum_variance_laplacian_img = minimum_variance_laplacian(img, 10)
		plot_img(minimum_variance_laplacian_img, 'minimum_variance_laplacian.bmp', 'Minimum_variance_laplacian')
	elif sys.argv[2] == '3':
		laplacian_gaussian_img = laplacian_gaussian(img, 2000)
		plot_img(laplacian_gaussian_img, 'laplacian_gaussian.bmp', 'Laplacian_gaussian')
	elif sys.argv[2] == '4':
		difference_gaussian_img = difference_gaussian(img, 1)
		plot_img(difference_gaussian_img, 'difference_gaussian.bmp', 'Difference_gaussian')
	else:
		print("Usage: python3 hw10.py [input_img] [problem ID]")
