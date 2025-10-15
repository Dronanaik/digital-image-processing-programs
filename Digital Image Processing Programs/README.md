
# Digital Image Processing Programs

A curated set of standalone Python scripts demonstrating core DIP concepts. Sample images are under `Images/`; scripts live under `Programs/`.

## Prerequisites
- Python 3.8+
- Packages: opencv-python, numpy, matplotlib, scikit-image

Install:
```bash
pip install opencv-python numpy matplotlib scikit-image
```

## Folder structure
```
Digital Image Processing Programs/
├─ Images/
└─ Programs/
   ├─ image_channels_and_convolution.py
   ├─ arithmetic_logical_operations.py
   ├─ gray_level_transformations.py
   ├─ bit_plane_slicing.py
   ├─ histogram_equalization.py
   ├─ frequency_domain_filters.py
   ├─ spatial_domain_filters.py
   ├─ median_filter_salt_pepper.py
   ├─ edge_enhancement_sobel_prewitt_laplacian.py
   ├─ image_sharpening_laplacian.py
   ├─ morphological_operations.py
   ├─ image_segmentation_edge_based.py
   ├─ image_watermarking.py
   ├─ image_restoration_median.py
   ├─ image_compression_btc.py
   └─ edge_detection_sobel.py
```

## Running scripts
From the `Programs/` directory, run any script (paths assume current working directory is `Programs/`).
```bash
cd "Digital Image Processing Programs/Programs"
python3 gray_level_transformations.py
```

If an image path fails (case differences), adjust the filename in the script or rename the file in `Images/`.

## Scripts overview
- image_channels_and_convolution.py: Display RGB channels, grayscale, 1D/2D convolution.
- arithmetic_logical_operations.py: Arithmetic and bitwise ops on two images.
- gray_level_transformations.py: Negative, log, gamma, contrast stretching.
- bit_plane_slicing.py: Bit-plane extraction from grayscale image.
- histogram_equalization.py: Contrast enhancement via histogram equalization.
- frequency_domain_filters.py: FFT-based LPF/HPF in frequency domain.
- spatial_domain_filters.py: LPF/HPF with spatial kernels.
- median_filter_salt_pepper.py: Median filter for salt-and-pepper noise.
- edge_enhancement_sobel_prewitt_laplacian.py: Sobel, Prewitt, Laplacian.
- image_sharpening_laplacian.py: Sharpen using Laplacian HPF.
- morphological_operations.py: Erosion, dilation, opening, closing.
- image_segmentation_edge_based.py: Canny + contours segmentation.
- image_watermarking.py: Repeated text watermark overlay.
- image_restoration_median.py: Median-based restoration.
- image_compression_btc.py: Block truncation coding.
- edge_detection_sobel.py: Sobel edge detection.
