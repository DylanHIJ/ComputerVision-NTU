# Computer Vision 2019 Fall

## Homework #3 

<div style="text-align:right"> B06902059 資工三 謝宜儒</div>

##### Description

This homework focuses on some pixel-wise manipulations on an image and plotting the histograms of the resulting images. 

##### Results

(a) original image and its histogram

<img src="/Users/dylanhsieh/NTU/course/CV2019f/hw3/01_original.bmp" style="zoom:33%;" />

<img src="/Users/dylanhsieh/NTU/course/CV2019f/hw3/01_original_hist.png" alt="01_original_hist" style="zoom: 50%;" />

(b) image with intensity divided by 3 and its histogram 

<img src="/Users/dylanhsieh/NTU/course/CV2019f/hw3/02_weakened.bmp" style="zoom:33%;" />

<img src="/Users/dylanhsieh/NTU/course/CV2019f/hw3/02_weakened_hist.png" alt="02_weakened_hist" style="zoom:50%;" />

(c) image after applying histogram equalization to (b) and its histogram 

<img src="/Users/dylanhsieh/NTU/course/CV2019f/hw3/03_equalized.bmp" alt="03_equalized" style="zoom:33%;" />

<img src="/Users/dylanhsieh/NTU/course/CV2019f/hw3/03_equalized_hist.png" alt="03_equalized_hist" style="zoom:50%;" />

##### Source Code (fragment)

```python
# Plot the histogram of an image 
def plot_hist(img, title, filename):
	plt.hist(img.flatten(), bins = range(0, 257))
	plt.title(title)
	plt.savefig(filename)
	plt.show()

# (a) original image and its histogram
def generate_original(img):
	cv2.imwrite('01_original.bmp', img)
	cv2.imshow('Original Image', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	plot_hist(img, 'Histogram of Original Image', '01_original_hist')
	
# (b) image with intensity divided by 3 and its histogram
def generate_weakened(img):
	weakened_img = img // 3
	cv2.imwrite('02_weakened.bmp', weakened_img)
	cv2.imshow('Weakened Image', weakened_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	plot_hist(weakened_img, 'Histogram of Weakened Image', '02_weakened_hist')

# (c) image after applying histogram equalization to (b) and its histogram
def generate_equalized(img):
	n = length * width
	weakened_img = img // 3
	equalized_img_flatten = np.copy(weakened_img.flatten())
	pixels_hist = np.zeros(256)
	for i in range(length):
		for j in range(width):
			pixels_hist[weakened_img[i][j]] += 1
	pre_sum = np.cumsum(pixels_hist)
	for i in range(0, 256):
		equalized_img_flatten[np.argwhere(weakened_img.flatten() == i)] = pre_sum[i] * 255 // n
	equalized_img = equalized_img_flatten.reshape(length, width)

	cv2.imwrite('03_equalized.bmp', equalized_img)
	cv2.imshow('Equalized Image', equalized_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	plot_hist(equalized_img, 'Histogram of Equalized Image', '03_equalized_hist')
```

To run the source code, type the following line in a terminal:

```
python3 hw3.py [input image] [problem number]
```

where in this homework, the input image is **lena.bmp** and the problem numbers are **1 ~ 3** .