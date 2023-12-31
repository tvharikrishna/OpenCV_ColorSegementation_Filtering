<div align="center">
  <h1>Color Segementation Filtering and Masks</h1>
</div>

<br>

<p align="center">
  <img src="data_readme/project_title.png" alt="Project Logo Cover" width="1500"/>
</p>

---------------------------------------------

## ★ About this Project:

The project focuses on color segementation in images using OpenCV, a powerful image porocessing library. The core of the project is the `ColorSpaceProcessor` class, designed to extract specific solors from an image by converting it into various color spaces like grascale and `HSV (Hue, Saturation, Value)`. The class allows users to specify `color ranges for segementation` and efficientyl processes images to isolate these colors. This functionality is particularly valuable in applications hwere precise `color detection` and `isolation` are crucial, such as in quality control, medical imaging, or even in artistic domains. The script is a testament to the versatility of Python and OpenCV in handling complex image processing tasks with ease and efficiency.

---------------------------------------------

## ★ What is Color Segementation vs Image Segementation:

### Color Segmentation
Color segmentation is a process in image processing that involves dividing an image into segments based on color. By analyzing the color distribution and `separating pixels into groups with similar colors`, this technique simplifies image analysis, particularly useful in applications like object tracking, quality control, and sorting systems. It typically employs color spaces such as HSV or LAB for more effective segmentation and relies on methods like color thresholding, but it can be challenged by varying lighting conditions which affect color consistency.

<p align="center">
  <img src="data_readme/example_image.png" alt="Project Logo Cover" width="1500"/>
</p>

### ★ Image Segmentation
Image segmentation is a crucial technique in image processing where an image is `partitioned into multiple segments or regions` to simplify and change its representation, making it more meaningful for analysis. Unlike color segmentation, it considers various image attributes like texture, intensity, and color, using methods such as thresholding, clustering, and deep learning. Image segmentation is essential in diverse applications, from medical imaging for tissue differentiation to autonomous driving for scene understanding, offering a comprehensive approach to understanding and interpreting complex image data.

<p align="center">
  <img src="data_readme/img segementation.png" alt="Project Logo Cover" width="600"/>
</p>

---------------------------------------------

## ★ Project Observations:

### Original Image ➔ Gray Image ➔ HSV Image ➔ Threshold/Mask Image ➔ ColorSpaces & Filtering

#### `Blue Color`

<p align="center">
  <img src="data_readme/original_Image.png" alt="Original Image" width="150"/>
  <img src="data_readme/gray.png" alt="Gray Image" width="150"/>
  <img src="data_readme/hsv.png" alt="HSV Image" width="150"/>
  <img src="data_readme/blue_tres.png" alt="Threshold/Mask Image" width="150"/>
  <img src="data_readme/blue_color.png" alt="Filtered ColorSpaces Image" width="150"/>
</p>

---------------------------------------------

#### `Green Color`

<p align="center">
  <img src="data_readme/original_Image.png" alt="Original Image" width="150"/>
  <img src="data_readme/gray.png" alt="Gray Image" width="150"/>
  <img src="data_readme/hsv.png" alt="HSV Image" width="150"/>
  <img src="data_readme/green_tres.png" alt="Threshold/Mask Image" width="150"/>
  <img src="data_readme/green_color.png" alt="Filtered ColorSpaces Image" width="150"/>
</p>

---------------------------------------------

#### `Red Color`

<p align="center">
  <img src="data_readme/original_Image.png" alt="Original Image" width="150"/>
  <img src="data_readme/gray.png" alt="Gray Image" width="150"/>
  <img src="data_readme/hsv.png" alt="HSV Image" width="150"/>
  <img src="data_readme/red_tres.png" alt="Threshold/Mask Image" width="150"/>
  <img src="data_readme/red_color.png" alt="Filtered ColorSpaces Image" width="150"/>
</p>

---------------------------------------------

#### `Yellow Color`

<p align="center">
  <img src="data_readme/original_Image.png" alt="Original Image" width="150"/>
  <img src="data_readme/gray.png" alt="Gray Image" width="150"/>
  <img src="data_readme/hsv.png" alt="HSV Image" width="150"/>
  <img src="data_readme/yellow_tres.png" alt="Threshold/Mask Image" width="150"/>
  <img src="data_readme/yellow_color.png" alt="Filtered ColorSpaces Image" width="150"/>
</p>

---------------------------------------------

## ★ Result and Analysis:

1. **Accuracy of Color Segmentation:** The segmentation accurately isolated the specified color & demonstrating the effectiveness of the HSV color range definitions.
2. **Color Space Conversion Efficacy:** HSV conversion was crucial for effective segmentation, outperforming the RGB color space in ease and accuracy.
3. **Grayscale and HSV Transformations:** Grayscale highlighted image luminance, while HSV was instrumental in color segmentation processes.
4. **Mask Application:** Generated masks effectively filtered out the targeted color, particularly for complex ranges like red and blue.
5. **Final Filtered Image:** The final image vividly highlighted areas with the specified color, though effectiveness varied with saturation and lighting.
6. **Challenges and Limitations:** Consistency in color detection was affected by lighting variations; accuracy heavily depended on precise color range settings.
7. **Performance:** Processing was swift and efficient, suggesting potential for real-time applications and effective file management.
8. **General Observations:** The tool's flexibility and adaptability for various applications were notable, though it requires adjustments for different conditions and lighting.
   
---------------------------------------------

## ★ My Project Video Demonstration:

<p align="center">
  
  <a href="https://www.linkedin.com/posts/tvharikrishna_computervision-imageprocessing-opencv-activity-7134409502384103424-Cb_E?utm_source=share&utm_medium=member_desktop">
  <img src="https://img.shields.io/badge/Video-Watch Color Segementation in Action -blue" alt="Video"/>
  </a>
</p>

---------------------------------------------
