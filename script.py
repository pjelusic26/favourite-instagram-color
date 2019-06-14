import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob
import os
from pathlib import Path

# Source Directory
src_folder = 'images/'
# Source Path
src_pth = Path(src_folder).resolve()

# Defining all JPG images in the folder as a variable
imgs = src_pth.glob('*.jpg')

# Defining empty variables for color systems
img_rgb = 0
img_cmyk = 0
img_gray = 0

# Defining empty variables for separate channels
total_r = 0
total_g = 0
total_b = 0

total_c = 0
total_m = 0
total_y = 0
total_k = 0

# Starting iterating through the folder
for img in imgs:
    img_name = f"{str(img.name)}"
    pic = plt.imread(img)

    # If the image is 2-dimensional, it means it's grayscale, and there are no colors to inspect)
    if(len(pic.shape) <= 2):
        print('Image is grayscale, can not compare color channels.')
        img_gray += 1
    else:
        # Getting number of channels (third value of shape property)
        color_channels = pic.shape[2]
        if(color_channels == 3):
            # Creating variables for each channel
            r = pic[:, :, 0]
            g = pic[:, :, 1]
            b = pic[:, :, 2]
            # Getting mean value for each channel
            total_r += np.mean(r)
            total_g += np.mean(g)
            total_b += np.mean(b)
            # Adding to total number of RGB images
            img_rgb += 1
        elif(color_channels == 4):
            # Creating variables for each channel
            c = pic[:, :, 0]
            m = pic[:, :, 1]
            y = pic[:, :, 2]
            k = pic[:, :, 3]
            # Getting mean value for each channel
            # Subtracting from 255 because in CMYK images, pixels with 0 value are actually the 'strongest'
            total_c += np.abs(255 - np.mean(c))
            total_m += np.abs(255 - np.mean(m))
            total_y += np.abs(255 - np.mean(y))
            total_k += np.abs(255 - np.mean(k))
            # Adding to total number of CMYK images
            img_cmyk += 1
        else:
            print('Image is grayscale, there are no color channels to compare.')

print(f"Found {img_rgb} RGB images, {img_cmyk} CMYK images and {img_gray} grayscale images.")

### RGB ###
### RGB ###
### RGB ###
### RGB ###

if(img_rgb > 0):
    print('RGB')

    rgb_channel_totals = (total_r, total_g, total_b)
    total_rgb = sum(rgb_channel_totals)

    rgb_channels_dictionairy = {
        'R': total_r,
        'G': total_g,
        'B': total_b
    }

    pct_r = total_r / total_rgb * 100
    pct_g = total_g / total_rgb * 100
    pct_b = total_b / total_rgb * 100

    rgb_channel_pct = (pct_r, pct_g, pct_b)

    print(f"Channel with most total pixel values, with percentage of total pixel values in image:")
    print(f"{max(rgb_channels_dictionairy, key = rgb_channels_dictionairy.get)}: {max(rgb_channel_pct)}%")

    print(f"All channels:")
    print(f"R: {pct_r}%")
    print(f"G: {pct_g}%")
    print(f"B: {pct_b}%")

### CMYK ###
### CMYK ###
### CMYK ###
### CMYK ###

if(img_cmyk > 0):
    print('CMYK')

    cmyk_channel_totals = (total_c, total_m, total_y, total_k)
    total_cmyk = sum(cmyk_channel_totals)

    cmyk_channels_dictionairy = {
        'C': total_c,
        'M': total_m,
        'Y': total_y,
        'K': total_k
    }

    pct_c = total_c / total_cmyk * 100
    pct_m = total_m / total_cmyk * 100
    pct_y = total_y / total_cmyk * 100
    pct_k = total_k / total_cmyk * 100

    cmyk_channel_pct = (pct_c, pct_m, pct_y, pct_k)

    print(f"Channel with most total pixel values, with percentage of total pixel values in image:")
    print(f"{max(cmyk_channels_dictionairy, key = cmyk_channels_dictionairy.get)}: {max(cmyk_channel_pct)}%")

    print(f"All channels:")
    print(f"C: {pct_c}%")
    print(f"M: {pct_m}%")
    print(f"Y: {pct_y}%")
    print(f"K: {pct_k}%")


    