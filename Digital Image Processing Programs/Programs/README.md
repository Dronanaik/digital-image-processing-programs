
# Digital Image Processing Programs

This folder contains standalone Python scripts demonstrating core digital image processing techniques. Each script reads sample images from the sibling `Images` directory.

## Prerequisites
- Python 3.8+
- Packages: opencv-python, numpy, matplotlib, scikit-image

Install:
```bash
pip install opencv-python numpy matplotlib scikit-image
```

## Scripts
- image_channels_and_convolution.py: Display RGB channels, grayscale, 1D and 2D convolution.
- arithmetic_logical_operations.py: Add, subtract, multiply, divide; bitwise AND/OR/XOR/NOT on two images.
- gray_level_transformations.py: Negative, log, gamma (power-law), contrast stretching.
- bit_plane_slicing.py: Extract specific bit-plane from grayscale image.
- histogram_equalization.py: Histogram equalization for contrast enhancement.
- frequency_domain_filters.py: Low-pass and high-pass filtering in frequency domain via FFT.
- spatial_domain_filters.py: Low-pass (average) and high-pass filtering using spatial kernels.
- median_filter_salt_pepper.py: Remove salt-and-pepper noise with median filter.
- edge_enhancement_sobel_prewitt_laplacian.py: Edge enhancement using Sobel, Prewitt, Laplacian (scikit-image).
- image_sharpening_laplacian.py: Sharpen using Laplacian high-pass filter.
- morphological_operations.py: Erosion, dilation, opening, closing.
- image_segmentation_edge_based.py: Edge-based segmentation using Canny + contours.
- image_watermarking.py: Add repeated text watermark overlay to an image.
- image_restoration_median.py: Simple restoration via median filtering.
- image_compression_btc.py: Block truncation coding (BTC) binary compression.
- edge_detection_sobel.py: Sobel edge detection on X, Y, and XY.

## Example usage
Run any script from this directory. Ensure the working directory is this folder so relative image paths resolve.
```bash
python3 image_channels_and_convolution.py
```

Images used are in `../Images/`. Update paths in scripts if you move files.
