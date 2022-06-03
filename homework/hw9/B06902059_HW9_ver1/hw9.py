"""
Computer Vision 2019 Fall
Homework #9
"""
import cv2, sys, math
import numpy as np

def robert(img, threshold):
	mask_r1 = np.array([[-1, 0], [0, 1]])
	mask_r2 = np.array([[0, -1], [1, 0]])
	pad_width = mask_r1.shape[0] - 1
	padded_img = np.pad(img, pad_width, 'reflect')
	robert_img = np.zeros(img.shape, dtype = np.uint8)
	for i in range(pad_width, padded_img.shape[0] - pad_width):
		for j in range(pad_width, padded_img.shape[1] - pad_width):
			r1 = np.sum(np.multiply(mask_r1, padded_img[i:i+mask_r1.shape[0], j:j+mask_r1.shape[1]]))
			r2 = np.sum(np.multiply(mask_r2, padded_img[i:i+mask_r2.shape[0], j:j+mask_r2.shape[1]]))
			grad_magnitude = math.sqrt(r1 ** 2 + r2 ** 2)
			if(grad_magnitude > threshold):
				robert_img[i-pad_width][j-pad_width] = 0
			else:
				robert_img[i-pad_width][j-pad_width] = 255
	return robert_img

def prewitt(img, threshold):
	mask_p1 = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
	mask_p2 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
	pad_width = mask_p1.shape[0] // 2
	padded_img = np.pad(img, pad_width, 'reflect')
	prewitt_img = np.zeros(img.shape, dtype = np.uint8)
	for i in range(pad_width, padded_img.shape[0] - pad_width):
		for j in range(pad_width, padded_img.shape[1] - pad_width):
			p1 = np.sum(np.multiply(mask_p1, padded_img[i-pad_width:i+pad_width+1, j-pad_width:j+pad_width+1]))
			p2 = np.sum(np.multiply(mask_p2, padded_img[i-pad_width:i+pad_width+1, j-pad_width:j+pad_width+1]))
			grad_magnitude = math.sqrt(p1 ** 2 + p2 ** 2)
			if(grad_magnitude > threshold):
				prewitt_img[i-pad_width][j-pad_width] = 0
			else:
				prewitt_img[i-pad_width][j-pad_width] = 255
	return prewitt_img

def sobel(img, threshold):
	mask_s1 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
	mask_s2 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
	pad_width = mask_s1.shape[0] // 2
	padded_img = np.pad(img, pad_width, 'reflect')
	sobel_img = np.zeros(img.shape, dtype = np.uint8)
	for i in range(pad_width, padded_img.shape[0] - pad_width):
		for j in range(pad_width, padded_img.shape[1] - pad_width):
			s1 = np.sum(np.multiply(mask_s1, padded_img[i-pad_width:i+pad_width+1, j-pad_width:j+pad_width+1]))
			s2 = np.sum(np.multiply(mask_s2, padded_img[i-pad_width:i+pad_width+1, j-pad_width:j+pad_width+1]))
			grad_magnitude = math.sqrt(s1 ** 2 + s2 ** 2)
			if(grad_magnitude > threshold):
				sobel_img[i-pad_width][j-pad_width] = 0
			else:
				sobel_img[i-pad_width][j-pad_width] = 255
	return sobel_img

def frei_and_chen(img, threshold):
	mask_f1 = np.array([[-1, -math.sqrt(2), -1], [0, 0, 0], [1, math.sqrt(2), 1]])
	mask_f2 = np.array([[-1, 0, 1], [-math.sqrt(2), 0, math.sqrt(2)], [-1, 0, 1]])
	pad_width = mask_f1.shape[0] // 2
	padded_img = np.pad(img, pad_width, 'reflect')
	frei_and_chen_img = np.zeros(img.shape, dtype = np.uint8)
	for i in range(pad_width, padded_img.shape[0] - pad_width):
		for j in range(pad_width, padded_img.shape[1] - pad_width):
			f1 = np.sum(np.multiply(mask_f1, padded_img[i-pad_width:i+pad_width+1, j-pad_width:j+pad_width+1]))
			f2 = np.sum(np.multiply(mask_f2, padded_img[i-pad_width:i+pad_width+1, j-pad_width:j+pad_width+1]))
			grad_magnitude = math.sqrt(f1 ** 2 + f2 ** 2)
			if(grad_magnitude > threshold):
				frei_and_chen_img[i-pad_width][j-pad_width] = 0
			else:
				frei_and_chen_img[i-pad_width][j-pad_width] = 255
	return frei_and_chen_img

def kirsch_compass(img, threshold):
	mask_k = np.array([[[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]],
					   [[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]],
					   [[5, 5, 5], [-3, 0, -3], [-3, -3, -3]],
					   [[5, 5, -3], [5, 0, -3], [-3, -3, -3]],
					   [[5, -3, -3], [5, 0, -3], [5, -3, -3]],
					   [[-3, -3, -3], [5, 0, -3], [5, 5, -3]],
					   [[-3, -3, -3], [-3, 0, -3], [5, 5, 5]],
					   [[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]]])
	pad_width = mask_k.shape[1] // 2
	padded_img = np.pad(img, pad_width, 'reflect')
	kirsch_compass_img = np.zeros(img.shape, dtype = np.uint8)
	for i in range(pad_width, padded_img.shape[0] - pad_width):
		for j in range(pad_width, padded_img.shape[1] - pad_width):
			grad_magnitude = 0
			for k in range(mask_k.shape[0]):
				grad_magnitude = max(grad_magnitude, 
					np.sum(np.multiply(mask_k[k], 
						padded_img[i-pad_width:i+pad_width+1, j-pad_width:j+pad_width+1])))
			if(grad_magnitude > threshold):
				kirsch_compass_img[i-pad_width][j-pad_width] = 0
			else:
				kirsch_compass_img[i-pad_width][j-pad_width] = 255
	return kirsch_compass_img

def robinson_compass(img, threshold):
	mask_r = np.array([[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]],
					   [[0, 1, 2], [-1, 0, 1], [-2, -1, 0]],
					   [[1, 2, 1], [0, 0, 0], [-1, -2, -1]],
					   [[2, 1, 0], [1, 0, -1], [0, -1, -2]],
					   [[1, 0, -1], [2, 0, -2], [1, 0, -1]],
					   [[0, -1, -2], [1, 0, -1], [2, 1, 0]],
					   [[-1, -2, -1], [0, 0, 0], [1, 2, 1]],
					   [[-2, -1, 0], [-1, 0, 1], [0, 1, 2]]])
	pad_width = mask_r.shape[1] // 2
	padded_img = np.pad(img, pad_width, 'reflect')
	robinson_compass_img = np.zeros(img.shape, dtype = np.uint8)
	for i in range(pad_width, padded_img.shape[0] - pad_width):
		for j in range(pad_width, padded_img.shape[1] - pad_width):
			grad_magnitude = 0
			for k in range(mask_r.shape[0]):
				grad_magnitude = max(grad_magnitude, 
					np.sum(np.multiply(mask_r[k],
						padded_img[i-pad_width:i+pad_width+1, j-pad_width:j+pad_width+1])))
			if(grad_magnitude > threshold):
				robinson_compass_img[i-pad_width][j-pad_width] = 0
			else:
				robinson_compass_img[i-pad_width][j-pad_width] = 255
	return robinson_compass_img

def nevatia_babu(img, threshold):
	mask_n = np.array([[[100, 100, 100, 100, 100], [100, 100, 100, 100, 100], [0, 0, 0, 0, 0],
						[-100, -100, -100, -100, -100], [-100, -100, -100, -100, -100]],
					   [[100, 100, 100, 100, 100], [100, 100, 100, 78, -32], [100, 92, 0, -92, -100],
						[32, -78, -100, -100, -100], [-100, -100, -100, -100, -100]],
					   [[100, 100, 100, 32, -100], [100, 100, 92, -78, -100], [100, 100, 0, -100, -100],
						[100, 78, -92, -100, -100], [100, -32, -100, -100, -100]],
					   [[-100, -100, 0, 100, 100], [-100, -100, 0, 100, 100], [-100, -100, 0, 100, 100],
						[-100, -100, 0, 100, 100], [-100, -100, 0, 100, 100]],
					   [[-100, 32, 100, 100, 100], [-100, -78, 92, 100, 100], [-100, -100, 0, 100, 100],
						[-100, -100, -92, 78, 100], [-100, -100, -100, -32, 100]],
					   [[100, 100, 100, 100, 100], [-32, 78, 100, 100, 100], [-100, -92, 0, 92, 100],
						[-100, -100, -100, -78, 32], [-100, -100, -100, -100, -100]]])
	pad_width = mask_n.shape[1] // 2
	padded_img = np.pad(img, pad_width, 'reflect')
	nevatia_babu_img = np.zeros(img.shape, dtype = np.uint8)
	for i in range(pad_width, padded_img.shape[0] - pad_width):
		for j in range(pad_width, padded_img.shape[1] - pad_width):
			grad_magnitude = 0
			for k in range(mask_n.shape[0]):
				grad_magnitude = max(grad_magnitude, 
					np.sum(np.multiply(mask_n[k], padded_img[i-pad_width:i+pad_width+1, j-pad_width:j+pad_width+1])))
			if(grad_magnitude > threshold):
				nevatia_babu_img[i-pad_width][j-pad_width] = 0
			else:
				nevatia_babu_img[i-pad_width][j-pad_width] = 255
	return nevatia_babu_img

def plot_img(img, filename, title):
	cv2.imwrite(filename, img)
	cv2.imshow(title, img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	# Read the input image in grayscale mode 
	img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
	length, width = img.shape[0], img.shape[1]

	if sys.argv[2] == '1':
		robert_img = robert(img, 25)
		plot_img(robert_img, 'robert.bmp', 'Robert edge image')
	elif sys.argv[2] == '2':
		prewitt_img = prewitt(img, 64)
		plot_img(prewitt_img, 'prewitt.bmp', 'Prewitt edge image')
	elif sys.argv[2] == '3':
		sobel_img = sobel(img, 80)
		plot_img(sobel_img, 'sobel.bmp', 'Sobel edge image')
	elif sys.argv[2] == '4':
		frei_and_chen_img = frei_and_chen(img, 45)
		plot_img(frei_and_chen_img, 'frei_and_chen.bmp', 'Frei and Chen edge image')
	elif sys.argv[2] == '5':
		kirsch_compass_img = kirsch_compass(img, 150)
		plot_img(kirsch_compass_img, 'kirsch_compass.bmp', 'Kirsch compass edge image')
	elif sys.argv[2] == '6':
		robinson_compass_img = robinson_compass(img, 50)
		plot_img(robinson_compass_img, 'robinson_compass.bmp', 'Robinson compass edge image')
	elif sys.argv[2] == '7':
		nevatia_babu_img = nevatia_babu(img, 15000)
		plot_img(nevatia_babu_img, 'nevatia_babu.bmp', 'Nevatia-Babu edge image')
	else:
		print("Usage: python3 hw9.py [input_img] [problem ID]")
