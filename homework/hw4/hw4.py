"""
Computer Vision 2019 Fall
Homework #4
"""

import sys
import cv2
import numpy as np 

# Octogonal 3-5-5-5-3 kernel
octogon = np.array([[0, 1, 1, 1, 0], 
				   	[1, 1, 1, 1, 1],
				    [1, 1, 1, 1, 1],
				    [1, 1, 1, 1, 1],
				    [0, 1, 1, 1, 0]])

L = np.array([[1, 1],
			  [0, 1]])

class Kernel:
	def __init__(self, origin, pattern):
		offsets = []
		for i in range(pattern.shape[0]):
			for j in range(pattern.shape[1]):
				if(pattern[i][j] == 1):
					offsets.append([i - origin[0], j - origin[1]])

		self._offsets = offsets

	def offsets(self):
		return self._offsets

def binarize_img(img): 
	binary_128_img = np.zeros((length, width))
	threshold = 128
	for i in range(length):
		for j in range(width):
			if(img[i][j] < threshold):
	 			binary_128_img[i][j] = 0
			else:
				binary_128_img[i][j] = 255

	return binary_128_img

def plot_img(img, filename, title):
	cv2.imwrite(filename, img)
	cv2.imshow(title, img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def intersection(img1, img2):
	intersection_img = np.zeros((length, width), dtype = np.uint8)
	for i in range(length):
		for j in range(width):
			if(img1[i][j] == img2[i][j] and img1[i][j] == 255):
				intersection_img[i][j] = 255

	return intersection_img

def complement(img):
	complement_img = np.copy(img)
	for i in range(length):
		for j in range(width):
			complement_img[i][j] = 255 - complement_img[i][j]

	return complement_img

def dilation(img, kernel):
	dilated_img = np.zeros((length, width), dtype = np.uint8)
	for i in range(length):
		for j in range(width):
			if(img[i][j] == 255):
				for offset in kernel.offsets():
					if(i + offset[0] >= 0 and i + offset[0] < length 
						and j + offset[1] >= 0 and j + offset[1] < width):
						dilated_img[i + offset[0]][j + offset[1]] = 255
	return dilated_img

def erosion(img, kernel):
	eroded_img = np.zeros((length, width), dtype = np.uint8)
	for i in range(length):
		for j in range(width):
			valid = 1
			for offset in kernel.offsets():
				if(i + offset[0] >= 0 and i + offset[0] < length
					and j + offset[1] >= 0 and j + offset[1] < width):
					if(img[i + offset[0]][j + offset[1]] != 255):
						valid = 0
						break
				else:
					valid = 0
					break
			if(valid):
				eroded_img[i][j] = 255

	return eroded_img

def opening(img, kernel):
	return dilation(erosion(img, kernel), kernel)

def closing(img, kernel):
	return erosion(dilation(img, kernel), kernel)

def hit_and_miss(img, j_kernel, k_kernel):
	return intersection(erosion(img, j_kernel), erosion(complement(img), k_kernel))

if __name__ == "__main__":
	# Read the input image in grayscale mode 
	img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
	length, width = img.shape[0], img.shape[1]

	# Binarize the input imgage
	img = binarize_img(img) 

	oct_kernel = Kernel((2, 2), octogon)
	j_kernel = Kernel((0, 1), L)
	k_kernel = Kernel((1, 0), L)

	if(sys.argv[2] == "1"):
		plot_img(dilation(img, oct_kernel), '01_dilated.bmp', 'Dilated Image')
	elif(sys.argv[2] == "2"):
		plot_img(erosion(img, oct_kernel), '02_eroded.bmp', 'Eroded Image')
	elif(sys.argv[2] == "3"):
		plot_img(opening(img, oct_kernel), '03_opening.bmp', 'Opening Image')
	elif(sys.argv[2] == "4"):
		plot_img(closing(img, oct_kernel), '04_closing.bmp', 'Closing Image')
	elif(sys.argv[2] == "5"):
		plot_img(hit_and_miss(img, j_kernel, k_kernel), '05_hit_and_miss.bmp', 'Hit-and-miss Image')
	else:
		printf("Invalid argument.\nUsage: python3 hw4.py [input image] [problem number]\n")