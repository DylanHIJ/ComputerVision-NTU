# Computer Vision 2019 Fall

## Homework #10

<div style="text-align:right"> b06902059 資工三 謝宜儒 </div>

##### Description

This homework focuses on zero crossing edge detection.

##### Results

1. Laplacian Mask 1 (Threshold: 15)

$$
\left[
\begin{array}{lc}
0 & 1 & 0 \\
1 & -4 & 1 \\
0 & 1 & 0 \\
\end{array}
\right]
$$

<img src="/Users/dylanhsieh/NTU/course/CV2019f/hw10/laplacian_1.bmp" alt="laplacian_1" style="zoom:33%;" />

2. Laplacian Mask 2 (Threshold: 15)

$$
\frac{1}{3}
\left[
\begin{array}{lc}
1 & 1 & 1 \\
1 & -8 & 1 \\
1 & 1 & 1 \\
\end{array}
\right]
$$

<img src="/Users/dylanhsieh/NTU/course/CV2019f/hw10/laplacian_2.bmp" alt="laplacian_2" style="zoom:33%;" />

3. Minimum Variance Laplacian (Threshold: 10)
   $$
   \frac{1}{3}
   \left[
   \begin{array}{clr}
   2 & -1 & 2 \\
   -1 & -4 & -1 \\
   2 & -1 & 2 \\ 
   \end{array}
   \right]
   $$
   <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw10/minimum_variance_laplacian.bmp" alt="minimum_variance_laplacian" style="zoom:33%;" />

4. Laplacian of Gaussian (Threshold: 2000)
   $$
   \left[
   \begin{array}{lc}
   0 & 0 & 0 & -1 & -1 & -2 & -1 & -1 & 0 & 0 & 0 \\
   0 & 0 & -2 & -4 & -8 & -9 & -8 & -4 & -2 & 0 & 0 \\
   0 & -2 & -7 & -15 & -22 & -23 & -22 & -15 & -7 & -2 & 0 \\
   -1 & -4 & -15 & -24 & -14 & -1 & -14 & -24 & -15 & -4 & -1 \\
   -1 & -8 & -22 & -14 & 52 & 103 & 52 & -14 & -22 & -8 & -1 \\
   -2 & -9 & -23 & -1 & 103 & 178 & 103 & -1 & -23 & -9 & -2 \\
   -1 & -8 & -22 & -14 & 52 & 103 & 52 & -14 & -22 & -8 & -1 \\
   -1 & -4 & -15 & -24 & -14 & -1 & -14 & -24 & -15 & -4 & -1 \\
   0 & -2 & -7 & -15 & -22 & -23 & -22 & -15 & -7 & -2 & 0 \\
   0 & 0 & -2 & -4 & -8 & -9 & -8 & -4 & -2 & 0 & 0 \\
   0 & 0 & 0 & -1 & -1 & -2 & -1 & -1 & 0 & 0 & 0 
   \end{array}
   \right]
   $$
   

<img src="/Users/dylanhsieh/NTU/course/CV2019f/hw10/laplacian_gaussian.bmp" alt="laplacian_gaussian" style="zoom:33%;" />

5. Difference of Gaussian (Threshold: 1)
   $$
   \left[
   \begin{array}{lc}
   -1 & -3 & -4 & -6 & -7 & -8 & -7 & -6 & -4 & -3 & -1 \\
   -3 & -5 & -8 & -11 & -13 & -13 & -13 & -11 & -8 & -5 & -3 \\
   -4 & -8 & -12 & -16 & -17 & -17 & -17 & -16 & -12 & -8 & -4 \\
   -6 & -11 & -16 & -16 & 0 & 15 & 0 & -16 & -16 & -11 & -6 \\
   -7 & -13 & -17 & 0 & 85 & 160 & 85 & 0 & -17 & -13 & -7 \\
   -8 & -13 & -17 & 15 & 160 & 283 & 160 & 15 & -17 & -13 & -8 \\
   -7 & -13 & -17 & 0 & 85 & 160 & 85 & 0 & -17 & -13 & -7 \\
   -6 & -11 & -16 & -16 & 0 & 15 & 0 & -16 & -16 & -11 & -6 \\
   -4 & -8 & -12 & -16 & -17 & -17 & -17 & -16 & -12 & -8 & -4 \\
   -3 & -5 & -8 & -11 & -13 & -13 & -13 & -11 & -8 & -5 & -3 \\
   -1 & -3 & -4 & -6 & -7 & -8 & -7 & -6 & -4 & -3 & -1 \\
   \end{array}
   \right]
   $$
   <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw10/difference_gaussian.bmp" alt="difference_gaussian" style="zoom:33%;" />