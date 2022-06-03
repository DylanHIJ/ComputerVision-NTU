"""
Computer Vision 2019 Fall
Homework #6
"""

import sys
import cv2
import numpy as np

def binarize(img): 
	binarized_img = np.zeros((length, width))
	threshold = 128
	for i in range(length):
		for j in range(width):
			if(img[i][j] < threshold):
	 			binarized_img[i][j] = 0
			else:
				binarized_img[i][j] = 255
	return binarized_img

def downsample(img, scale):
	downsampled_img = np.zeros((int(length / scale), int(width / scale)), dtype = np.uint8)
	for i in range(0, length, scale):
		for j in range(0, width, scale):
			downsampled_img[int(i / scale)][int(j / scale)] = img[i][j]
	return downsampled_img

def h(b, c, d, e):
	if(b == c and (d != b or e != b)):
		return 1
	if(b == c and (d == b and e == b)):
		return 2
	if(b != c):
		return 3

def yokoi_num(img):
	padding_img = np.zeros((img.shape[0] + 2, img.shape[1] + 2), dtype = np.uint8)
	padding_img[1:-1, 1:-1] = img
	yokoi_graph = np.zeros(img.shape, dtype = np.uint8)
	
	# -1 for "undefined" (border points), 0 for default
	# 1 for q, 2 for r, 3 for s
	for i in range(1, padding_img.shape[0] - 1):
		for j in range(1, padding_img.shape[1] - 1):
			if(padding_img[i][j] == 0):
				continue
			a1 = h(padding_img[i][j], padding_img[i][j + 1], padding_img[i - 1][j + 1], padding_img[i - 1][j])
			a2 = h(padding_img[i][j], padding_img[i - 1][j], padding_img[i - 1][j - 1], padding_img[i][j - 1])
			a3 = h(padding_img[i][j], padding_img[i][j - 1], padding_img[i + 1][j - 1], padding_img[i + 1][j])
			a4 = h(padding_img[i][j], padding_img[i + 1][j], padding_img[i + 1][j + 1], padding_img[i][j + 1])
			count_q = (a1 == 1) + (a2 == 1) + (a3 == 1) + (a4 == 1)
			count_r = (a1 == 2) + (a2 == 2) + (a3 == 2) + (a4 == 2)
			if(count_r == 4):
				yokoi_graph[i - 1][j - 1] = 5
			else:
				yokoi_graph[i - 1][j - 1] = count_q

	return yokoi_graph

def print_graph(graph):
	for i in range(graph.shape[0]):
		for j in range(graph.shape[1]):
			if(graph[i][j] != 0):
				print(graph[i][j], end = '')
			else:
				print(' ', end = '')
		print('')

if __name__ == "__main__":
	if(len(sys.argv) != 2):
		printf("Usage: python3 hw6.py [input image]\n")

	# Read the input image in grayscale mode 
	img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
	length, width = img.shape[0], img.shape[1] 

	binarized_img = binarize(img)
	downsampled_img = downsample(binarized_img, 8)
	yokoi_graph = yokoi_num(downsampled_img)
	print_graph(yokoi_graph)