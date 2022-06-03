"""
Computer Vision 2019 Fall
Homework #8
"""

import sys
import cv2
import numpy as np 
import math
import os

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

octogon = np.array([[0, 1, 1, 1, 0], 
				   	[1, 1, 1, 1, 1],
				    [1, 1, 1, 1, 1],
				    [1, 1, 1, 1, 1],
				    [0, 1, 1, 1, 0]])

filter_box_3 = (1 / 9) * np.array([[1, 1, 1],
						  		   [1, 1, 1],
						  		   [1, 1, 1]])

filter_box_5 = (1 / 25) * np.array([[1, 1, 1, 1, 1],
						  			[1, 1, 1, 1, 1],
						  			[1, 1, 1, 1, 1],
						  			[1, 1, 1, 1, 1],
						  			[1, 1, 1, 1, 1]])

def gaussian_noise(img, amplitude):
	gau_noise_img = np.zeros(img.shape, dtype = np.uint8)
	for i in range(length):
		for j in range(width):
			noise_val = img[i][j] + int(amplitude * np.random.normal(0, 1))
			gau_noise_img[i][j] = max(0, min(255, noise_val))
	return gau_noise_img

def salt_and_pepper_noise(img, prob):
	sp_noise_img = np.zeros(img.shape, dtype = np.uint8)
	for i in range(length):
		for j in range(width):
			randval = np.random.uniform(0, 1)
			if randval < prob: 
				sp_noise_img[i][j] = 0
			elif randval > (1 - prob):
				sp_noise_img[i][j] = 255
			else:
				sp_noise_img[i][j] = img[i][j]
	return sp_noise_img

def dilation(img, kernel): # grayscale
	dilated_img = np.zeros((length, width), dtype = np.uint8)
	for i in range(length):
		for j in range(width):
			max_color = 0		
			for offset in kernel.offsets():
				if(i + offset[0] >= 0 and i + offset[0] < length
					and j + offset[1] >= 0 and j + offset[1] < width):
					max_color = max(max_color, img[i + offset[0]][j + offset[1]])
			dilated_img[i][j] = int(max_color)
	return dilated_img

def erosion(img, kernel): # grayscale
	eroded_img = np.zeros((length, width), dtype = np.uint8)
	for i in range(length):
		for j in range(width):
			in_image = True
			min_color = 255
			for offset in kernel.offsets():
				if(i + offset[0] >= 0 and i + offset[0] < length
					and j + offset[1] >= 0 and j + offset[1] < width):
					min_color = min(min_color, img[i + offset[0]][j + offset[1]])
					continue
				else:
					in_image = False 
					break
			if in_image:
				eroded_img[i][j] = int(min_color)
	return eroded_img

def opening(img, kernel):
	return dilation(erosion(img, kernel), kernel)

def closing(img, kernel):
	return erosion(dilation(img, kernel), kernel)

def box_filter(img, filter_box):
	pad_width = filter_box.shape[0] // 2
	padded_img = np.pad(img, pad_width, 'reflect')
	noise_removed_img = np.zeros(img.shape, dtype = np.int)
	for i in range(pad_width, padded_img.shape[0] - pad_width):
		for j in range(pad_width, padded_img.shape[1] - pad_width):
			noise_removed_img[i-pad_width][j-pad_width] = np.sum(np.multiply(padded_img[i-pad_width:i+pad_width+1, 
					j-pad_width:j+pad_width+1], filter_box))
	return noise_removed_img

def median_filter(img, filter_size):
	pad_width = filter_size // 2
	padded_img = np.pad(img, pad_width, 'reflect')
	noise_removed_img = np.zeros(img.shape, dtype = np.int)
	for i in range(pad_width, padded_img.shape[0] - pad_width):
		for j in range(pad_width, padded_img.shape[1] - pad_width):
			noise_removed_img[i-pad_width][j-pad_width] = np.sort(padded_img[i-pad_width:i+pad_width+1,
				j-pad_width:j+pad_width+1], axis = None)[filter_size ** 2 // 2]
	return noise_removed_img

def calc_SNR(img, nimg):
	img = img.flatten() / 255
	nimg = nimg.flatten() / 255
	mean = np.mean(img)
	vs = np.mean((img - np.repeat(mean, img.shape[0])) ** 2)
	mean_n = np.mean(nimg - img)
	vn = np.mean((nimg - img - np.repeat(mean_n, img.shape[0])) ** 2)
	return 20 * math.log((math.sqrt(vs) / math.sqrt(vn)), 10)

def remove_noise(noise_img, original_img, directory):
	print("SNR of %s is %f" %
		(os.path.join(directory, 'noised.bmp'), calc_SNR(original_img, noise_img)))
	box_filtered_3_img = box_filter(noise_img, filter_box_3)
	print("SNR of %s is %f" % 
		(os.path.join(directory, 'box_filtered_3.bmp'), calc_SNR(original_img, box_filtered_3_img)))
	box_filtered_5_img = box_filter(noise_img, filter_box_5)
	print("SNR of %s is %f" % 
		(os.path.join(directory, 'box_filtered_5.bmp'), calc_SNR(original_img, box_filtered_5_img)))
	median_filtered_3_img = median_filter(noise_img, 3)
	print("SNR of %s is %f" % 
		(os.path.join(directory, 'median_filtered_3.bmp'), calc_SNR(original_img, median_filtered_3_img)))
	median_filtered_5_img = median_filter(noise_img, 5)
	print("SNR of %s is %f" % 
		(os.path.join(directory, 'median_filtered_5.bmp'), calc_SNR(original_img, median_filtered_5_img)))
	open_close_img = closing(opening(noise_img, oct_kernel), oct_kernel)
	print("SNR of %s is %f" % 
		(os.path.join(directory, 'open_close.bmp'), calc_SNR(original_img, open_close_img)))
	close_open_img = opening(closing(noise_img, oct_kernel), oct_kernel)
	print("SNR of %s is %f" % 
		(os.path.join(directory, 'close_open.bmp'), calc_SNR(original_img, close_open_img)))

	cv2.imwrite(os.path.join(directory, 'box_filtered_3.bmp'), box_filtered_3_img)
	cv2.imwrite(os.path.join(directory, 'box_filtered_5.bmp'), box_filtered_5_img)
	cv2.imwrite(os.path.join(directory, 'median_filtered_3.bmp'), median_filtered_3_img)
	cv2.imwrite(os.path.join(directory, 'median_filtered_5.bmp'), median_filtered_5_img)
	cv2.imwrite(os.path.join(directory, 'open_close.bmp'), open_close_img)
	cv2.imwrite(os.path.join(directory, 'close_open.bmp'), close_open_img)

if __name__ == '__main__':
	# Read the input image in grayscale mode 
	img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
	length, width = img.shape[0], img.shape[1] 

	oct_kernel = Kernel((2, 2), octogon) 	
	# Generate images with noise (gaussain noise and salt&pepper noise)
	gau_noise_img_10 = gaussian_noise(img, 10)
	gau_noise_img_30 = gaussian_noise(img, 30)
	sp_noise_img_005 = salt_and_pepper_noise(img, 0.05)
	sp_noise_img_01 = salt_and_pepper_noise(img, 0.1)
	cv2.imwrite(os.path.join('gau_noise_10', 'noised.bmp'), gau_noise_img_10)
	cv2.imwrite(os.path.join('gau_noise_30', 'noised.bmp'), gau_noise_img_30)
	cv2.imwrite(os.path.join('sp_noise_0.05', 'noised.bmp'), sp_noise_img_005)
	cv2.imwrite(os.path.join('sp_noise_0.1', 'noised.bmp'), sp_noise_img_01)

	remove_noise(gau_noise_img_10, img, 'gau_noise_10',)
	remove_noise(gau_noise_img_30, img, 'gau_noise_30')
	remove_noise(sp_noise_img_005, img, 'sp_noise_0.05')
	remove_noise(sp_noise_img_01, img, 'sp_noise_0.1')
