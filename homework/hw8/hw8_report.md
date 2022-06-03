# Computer Vision 2019 Fall

## Homework #8

<div style="text-align:right">b06902059 資工三 謝宜儒</div>
#### Description

This homework focuses on generating noisy images and removing noise from images.

#### Results

##### Gaussian noise image with amplitude 10

<div style="text-align:center">
  <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/gau_noise_10/noised.bmp" alt="noised" style="zoom: 33%;" />
  <p>
    noisy image  <br> SNR = 13.938
  </p>
</div>

<div style="text-align:center">
	<div>
    <div style="display:inline-block">
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/gau_noise_10/box_filtered_3.bmp" alt="box_filtered_3" style="zoom:33%;" />  
      <p> 3x3 box filter <br> SNR = 17.828 </p>
    </div>
    <div style="display:inline-block"> 
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/gau_noise_10/box_filtered_5.bmp" alt="box_filtered_5" style="zoom:33%;" /> 
      <p> 5x5 box filter <br> SNR = 14.869 </p>
    </div>
    <div style="display:inline-block">
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/gau_noise_10/median_filtered_3.bmp" alt="median_filtered_3" style="zoom:33%;" /> 
      <p> 3x3 median filter <br> SNR = 17.907 </p>
    </div>
  </div> 
</div>

<div style="text-align:center">
	<div>
    <div style="display:inline-block">
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/gau_noise_10/median_filtered_5.bmp" alt="median_filtered_5" style="zoom:33%;" />  
      <p> 5x5 median filter <br> SNR = 16.074 </p>
    </div>
    <div style="display:inline-block"> 
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/gau_noise_10/open_close.bmp" alt="open_close" style="zoom:33%;" /> 
      <p> open then close <br> SNR = 8.572 </p>
    </div>
    <div style="display:inline-block">
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/gau_noise_10/close_open.bmp" alt="close_open" style="zoom:33%;" /> 
      <p> close then open <br> SNR = 7.652 </p>
    </div>
  </div> 
</div>

##### Gaussian noise image with amplitude 30

<div style="text-align:center">
  <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/gau_noise_30/noised.bmp" alt="noised" style="zoom: 33%;" />
  <p>
    noisy image <br> SNR = 4.290
  </p>
</div>

<div style="text-align:center">
	<div>
    <div style="display:inline-block">
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/gau_noise_30/box_filtered_3.bmp" alt="box_filtered_3" style="zoom:33%;" />  
      <p> 3x3 box filter <br> SNR = 12.688 </p>
    </div>
    <div style="display:inline-block"> 
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/gau_noise_30/box_filtered_5.bmp" alt="box_filtered_5" style="zoom:33%;" /> 
      <p> 5x5 box filter <br> SNR = 13.349 </p>
    </div>
    <div style="display:inline-block">
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/gau_noise_30/median_filtered_3.bmp" alt="median_filtered_3" style="zoom:33%;" /> 
      <p> 3x3 median filter <br> SNR = 11.314 </p>
    </div>
  </div> 
</div>

<div style="text-align:center">
	<div>
    <div style="display:inline-block">
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/gau_noise_30/median_filtered_5.bmp" alt="median_filtered_5" style="zoom:33%;" />  
      <p> 5x5 median filter <br> SNR = 13.077</p>
    </div>
    <div style="display:inline-block"> 
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/gau_noise_30/open_close.bmp" alt="open_close" style="zoom:33%;" /> 
      <p> open then close <br> SNR = 8.588 </p>
    </div>
    <div style="display:inline-block">
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/gau_noise_30/close_open.bmp" alt="close_open" style="zoom:33%;" /> 
      <p> close then open <br> SNR = 6.065</p>
    </div>
  </div> 
</div>

##### Salt-and-pepper noise image with probability 0.1

<div style="text-align:center">
  <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/sp_noise_0.1/noised.bmp" alt="noised" style="zoom: 33%;" />
  <p>
    noisy image <br> SNR = -2.106
  </p>
</div>

<div style="text-align:center">
	<div>
    <div style="display:inline-block">
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/sp_noise_0.1/box_filtered_3.bmp" alt="box_filtered_3" style="zoom:33%;" />  
      <p> 3x3 box filter  <br> SNR = 6.342 </p>
    </div>
    <div style="display:inline-block"> 
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/sp_noise_0.1/box_filtered_5.bmp" alt="box_filtered_5" style="zoom:33%;" /> 
      <p> 5x5 box filter <br> SNR = 8.523 </p>
    </div>
    <div style="display:inline-block">
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/sp_noise_0.1/median_filtered_3.bmp" alt="median_filtered_3" style="zoom:33%;" /> 
      <p> 3x3 median filter <br> SNR = 14.913 </p>
    </div>
  </div> 
</div>

<div style="text-align:center">
	<div>
    <div style="display:inline-block">
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/sp_noise_0.1/median_filtered_5.bmp" alt="median_filtered_5" style="zoom:33%;" />  
      <p> 5x5 median filter <br> SNR = 15.785</p>
    </div>
    <div style="display:inline-block"> 
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/sp_noise_0.1/open_close.bmp" alt="open_close" style="zoom:33%;" /> 
      <p> open then close <br> SNR = -2.300</p>
    </div>
    <div style="display:inline-block">
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/sp_noise_0.1/close_open.bmp" alt="close_open" style="zoom:33%;" /> 
      <p> close then open <br> SNR = -2.937</p>
    </div>
  </div> 
</div>

#####Salt-and-pepper noise image with probability 0.05

<div style="text-align:center">
  <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/sp_noise_0.05/noised.bmp" alt="noised" style="zoom: 33%;" />
  <p>
    noisy image <br> SNR = 0.991
  </p>
</div>

<div style="text-align:center">
	<div>
    <div style="display:inline-block">
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/sp_noise_0.05/box_filtered_3.bmp" alt="box_filtered_3" style="zoom:33%;" />  
      <p> 3x3 box filter <br> SNR = 9.501 </p>
    </div>
    <div style="display:inline-block"> 
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/sp_noise_0.05/box_filtered_5.bmp" alt="box_filtered_5" style="zoom:33%;" /> 
      <p> 5x5 box filter <br> SNR = 11.194</p>
    </div>
    <div style="display:inline-block">
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/sp_noise_0.05/median_filtered_3.bmp" alt="median_filtered_3" style="zoom:33%;" /> 
      <p> 3x3 median filter <br> SNR = 19.266 </p>
    </div>
  </div> 
</div>

<div style="text-align:center">
	<div>
    <div style="display:inline-block">
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/sp_noise_0.05/median_filtered_5.bmp" alt="median_filtered_5" style="zoom:33%;" />  
      <p> 5x5 median filter <br> SNR = 16.358</p>
    </div>
    <div style="display:inline-block"> 
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/sp_noise_0.05/open_close.bmp" alt="open_close" style="zoom:33%;" /> 
      <p> open then close <br> SNR = 4.451</p>
    </div>
    <div style="display:inline-block">
      <img src="/Users/dylanhsieh/NTU/course/CV2019f/hw8/sp_noise_0.05/close_open.bmp" alt="close_open" style="zoom:33%;" /> 
      <p> close then open <br> SNR = 4.014</p>
    </div>
  </div> 
</div>

##### 