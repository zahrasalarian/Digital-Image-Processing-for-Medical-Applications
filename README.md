# Digital Image Processing

This repository contains assignments and projects related to various aspects of image processing, from basic operations to advanced techniques like active contours.

---

## Table of Contents

1. [HW0 - Introduction to Image Analysis with Python](#hw0)
    - [pt-1.ipynb (File Link)](<HW0 - Introduction to Image Analysis with Python/pt-1.ipynb>)
    - [pt-2.ipynb (File Link)](<HW0 - Introduction to Image Analysis with Python/pt-2.ipynb>)
    - [pt-3.ipynb (File Link)](<HW0 - Introduction to Image Analysis with Python/pt-3.ipynb>)
    - [pt-4.ipynb (File Link)](<HW0 - Introduction to Image Analysis with Python/pt-4.ipynb>)
2. [HW1 - Introduction to Operations on Images](#hw1)
    - [affine_transformations_and_image_interpolation.ipynb (File Link)](<HW1 - Introduction to Operations on Images/affine_transformations_and_image_interpolation.ipynb>)
    - [contrast_and_brightness_adjustments.ipynb (File Link)](<HW1 - Introduction to Operations on Images/contrast_and_brightness_adjustments.ipynb>)
3. [HW2 - Intensity-based Operations](#hw2)
    - [contrast_stretching_and_power_law.ipynb (File Link)](<HW2 - Intensity-based Operations/contrast_stretching_and_power_law.ipynb>)
    - [histogram_equalization_and_CLAHE.ipynb (File Link)](<HW2 - Intensity-based Operations/histogram_equalization_and_CLAHE.ipynb>)
4. [HW3 - Spatial Operations](#hw3)
    - [mean_median_and_laplacian_isotropic_filters.ipynb (File Link)](<HW3 - Spatial Operations/mean_median_and_laplacian_isotropic_filters.ipynb>)
    - [laplacian_sharpening_sobely_sobely.ipynb (File Link)](<HW3 - Spatial Operations/laplacian_sharpening_sobely_sobely.ipynb>)
5. [HW4 - Frequency Domain Operations](#hw4)
    - [fourier_transform_and_band_reject.ipynb (File Link)](<HW4 - Frequency Domain Operations/fourier_transform_and_band_reject.ipynb>)
    - [low_and_high_ideal_butterworth_guassian_filters.ipynb (File Link)](<HW4 - Frequency Domain Operations/low_and_high_ideal_butterworth_guassian_filters.ipynb>)
6. [HW5 - Image Restoration and Morphological Image Processing](#hw5)
    - [restoration.ipynb (File Link)](<HW5 - Image Restoration and Morphological Image Processing/restoration.ipynb>)
    - [morphological_operations.ipynb (File Link)](<HW5 - Image Restoration and Morphological Image Processing/morphological_operations.ipynb>)
7. [HW6 - Segmentation and Active Contours](#hw6)
    - [non_maximum_suppression_and_hysteresis_thresholding.ipynb (File Link)](<HW6 - Segmentation and Active Contours/non_maximum_suppression_and_hysteresis_thresholding.ipynb>)
    - [hough_circle_detection.ipynb (File Link)](<HW6 - Segmentation and Active Contours/hough_circle_detection.ipynb>)
    - [active_contours_snakes_method.ipynb (File Link)](<HW6 - Segmentation and Active Contours/active_contours_snakes_method.ipynb>)

---

## HW0 - Introduction to Image Analysis with Python <a name="hw0"></a>

In this section, we introduce the basics of Python programming and data visualization, laying the groundwork for advanced image analysis topics.

### Topics Covered

#### `pt-1.ipynb`
- Exploring NumPy functionalities
- Data Types and Memory Management
- Array Manipulations

#### `pt-2.ipynb`
- Populating Matrixes Based on Defined Rules

#### `pt-3.ipynb`
- 2D Matrix Generation with Circle Pattern
- Adding Random Noise to Matrix

#### `pt-4.ipynb`
- Data Distribution Visualization
- Plotting Histograms with Matplotlib

---

## HW1 - Introduction to Operations on Images <a name="hw1"></a>

In this section, we delve into basic image operations, including transformations and adjustments. The notebooks cover a variety of techniques such as affine transformations, image interpolation, and contrast & brightness adjustments.

### Topics Covered

#### `affine_transformations_and_image_interpolation.ipynb`
- Affine Transformations (Rotation, Scaling, Shearing)
- Downsampling
- Resampling & Interpolation (Cubic, Linear, Nearest)

#### `contrast_and_brightness_adjustments.ipynb`
- Images Normalization
- Linear and Non-linear Transformations
- Adjusted Contrast & Brightness

---

## HW2 - Intensity-based Operations <a name="hw2"></a>

This part, explores the basics of intensity-based operations for image enhancement. Techniques ranging from contrast stretching and power law transformations to histogram equalization and CLAHE are covered. Each notebook offers a thorough analysis of histogram techniques and their outcomes, providing a complete understanding of the subject.

### Topics Covered

#### `contrast_stretching_and_power_law.ipynb`
- Contrast Stretching
- Power-Law (Gamma) Transformation
- Different Gamma Value Experimentation
- Comparison between Contrast Stretching and Power-Law Along 

#### `histogram_equalization_and_CLAHE.ipynb`
- Histogram Equalization
- Contrast Limited Adaptive Histogram Equalization (CLAHE)
- Analysis of Histogram Techniques and Their Outcomes

---

## HW3 - Spatial Operations <a name="hw3"></a>

In this part, the focus shifts to spatial filtering techniques that emphasize on specific features in images. We explore various types of filters like mean, median, and Laplacian, along with edge-detection methods such as Sobel operators.

### Topics Covered

#### `mean_median_and_laplacian_isotropic_filters.ipynb`
- Spatial Filters (Mean, Median)
- Image Blurring Techniques
- Laplacian Isotropic Filter
- Image Enhancement

#### `laplacian_sharpening_sobely_sobely.ipynb`
- Laplacian Sharpening
- Sobel Filters (Sobel-X, Sobel-Y)
- Edge Detection Techniques
- Image Enhancement

---

## HW4 - Frequency Domain Operations <a name="hw4"></a>

In this section, we delve into the realm of frequency domain operations, studying the Fourier Transform and its applications in image processing. From basic Fourier Transform techniques to the implementation of various types of filters such as Ideal, Butterworth, and Gaussian, this section provides a comprehensive look into the manipulation of images in the frequency domain.

### Topics Covered

#### `fourier_transform_and_band_reject.ipynb`
- Fourier Transform for Image Analysis
- Band-Reject Filtering
- Frequency Domain Techniques

#### `low_and_high_ideal_butterworth_guassian_filters.ipynb`
- Fourier Transform & Inverse Fourier Transform
- Low- and High-Pass Filters (Ideal, Butterworth, Gaussian)

---

## HW5 - Image Restoration and Morphological Image Processing <a name="hw5"></a>

In this part, we explore various methods for improving image quality and enhancing features through various restoration and morphological techniques. This section covers a range of topics, from eliminating unwanted artifacts to performing operations like dilation and erosion. We explore the fundamentals of these methods, their applications, and their effects on different types of images.

### Topics Covered

#### `restoration.ipynb`
- Noise Distribution Analysis
- Alpha-Trimmed Mean Filtering
- Inverse Filtering for Image Restoration
- High- and Low-Pass Butterworth Filters

#### `morphological_operations.ipynb`
- Dilation and Erosion Functions
- Boundary Identification through Textural Segmentation
- Morphologic Opening and Closing
---

## HW6 - Segmentation and Active Contours <a name="hw6"></a>

The final section focuses on the complex realm of image segmentation and contour detection. We employ a range of algorithms and techniques to identify and isolate specific structures within images. From basic circle detection using the Hough transform to sophisticated active contours known as "snakes". These techniques help us to explore how to extract meaningful information from complex visual scenes.

### Topics Covered

#### `non_maximum_suppression_and_hysteresis_thresholding.ipynb`
- Sobel and Prewitt Operators
- Non-Maximum Suppression
- Hysteresis Thresholding

#### `hough_circle_detection.py`
- Circle Detection using Hough Transform

#### `active_contours_snakes_method.ipynb`
- User Interface for Gathering Initial Contour Points
- Calculating Equally Spaced 2D Contour Points
- Snake External and Internal Energy Calculating
- Contour Evolution

