"""
Computer Vision 2019 Fall
Homework #1 
"""

import sys
import numpy as np
import cv2  

# Upside-down image
def plot1(img):
	upside_down_img = img.copy()
	for i in range(length):
		for j in range(width):
			upside_down_img[i][j] = img[length - 1 - i][j]

	cv2.imwrite('01_upside_down.bmp', upside_down_img)
	cv2.imshow('Upside-down Lena', upside_down_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


# Right-side-left image
def plot2(img):
	right_side_left_img = img.copy()
	for i in range(length):
		for j in range(width):
			right_side_left_img[i][j] = img[i][width - 1 - j]

	cv2.imwrite('02_right_side_left.bmp', right_side_left_img)
	cv2.imshow('Right-side-left Lena', right_side_left_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

# Diagonally mirrored image
def plot3(img):
	diagonally_mirrored_img = img.copy()
	for i in range(length):
		for j in range(width):
			diagonally_mirrored_img[i][j] = img[j][i]

	cv2.imwrite('03_diagonally_mirrored.bmp', diagonally_mirrored_img)
	cv2.imshow('Diagonally mirrored Lena', diagonally_mirrored_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	# Read the original image
	img = cv2.imread('lena.bmp')
	length = img.shape[0]
	width = img.shape[1]

	if sys.argv[1] == '1':
		plot1(img)
	elif sys.argv[1] == '2':
		plot2(img)
	elif sys.argv[1] == '3':
		plot3(img)
	else:
		print("Invalid argument.\nUsage: python3 hw1.py [problem number]")