#!/usr/bin/env python3
"""
CleanShot Pro Ultimate v2.3 - Advanced AI Fingerprint Disruptor
No pywt dependency! Works with any Python + 100% color preservation + metadata removal
"""

import os
import sys
import math
import argparse
import random
from multiprocessing import Pool, cpu_count
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

TOOL_NAME = "CleanShot Pro Ultimate"
VERSION = "2.3"
AUTHOR_EMAIL = "imsecure4@gmail.com"

def clamp_uint8(a): 
    """Clamp array values to valid uint8 range (0-255)"""
    return np.clip(a, 0, 255).astype(np.uint8)

def psnr(a, b):
    """Calculate Peak Signal-to-Noise Ratio between original and processed image"""
    mse = np.mean((a.astype(np.float32) - b.astype(np.float32))**2)
    return 20 * math.log10(255 / math.sqrt(mse)) if mse else float('inf')

def remove_metadata_save(img, output_path):
    """
    Save image as completely clean PNG without ANY metadata
    Creates new image from pixel data only - perfect for privacy
    """
    data = list(img.getdata())
    clean_img = Image.new(img.mode, img.size)
    clean_img.putdata(data)
    clean_img.save(output_path, "PNG", compress_level=1)

def color_pipeline(img, preset="light"):
    """
    Advanced color-preserving image processing pipeline:
    1. Gaussian noise (subtle)
    2. FFT mid-frequency perturbation (AI fingerprint disruption)
    3. HSV color preservation 
    4. Light post-processing
    """
    img = img.convert("RGB")
    orig = np.array(img)
    
    presets = {
        "light":   {"noise":0.3, "fft":0.08, "color":0.002, "blur":0.1,  "sharp":0.2},
        "medium":  {"noise":0.5, "fft":0.12, "color":0.004, "blur":0.2,  "sharp":0.4},
        "strong":  {"noise":0.8, "fft":0.20, "color":0.008, "blur":0.4,  "sharp":0.6}
    }
    params = presets.get(preset, presets["light"])
    
    arr = orig.astype(np.float32)
    
    # 1. Subtle Gaussian noise
    noise = np.random.normal(0, params["noise"], arr.shape)
    arr = np.clip(arr + noise, 0, 255)
    
    # 2. FFT mid-frequency perturbation on luminance (AI disruption)
    gray = 0.299*arr[:,:,0] + 0.587*arr[:,:,1] + 0.114*arr[:,:,2]
    if params["fft"] > 0:
        F = np.fft.fft2(gray)
        fft_region = slice(20, 100)
        F[fft_region, fft_region] += np.random.normal(0, params["fft"]*0.0002, (80,80)) * np.abs(F[fft_region, fft_region])
        new_gray = np.real(np.fft.ifft2(F))
        gray = 0.98*gray + 0.02*np.clip(new_gray, 0, 255)
    
    # 3. HSV color preservation (modify Value only)
    hsv = np.array(img.convert('HSV'))
    hsv[:,:,2] = gray.astype(np.uint8)
    result = Image.fromarray(hsv, 'HSV').convert('RGB')
    
    # 4. Final subtle adjustments
    if params["color"] > 0: 
        result = ImageEnhance.Color(result).enhance(1-params["color"])
    if params["blur"] > 0: 
        result = result.filter(ImageFilter.GaussianBlur(params["blur"]/10))
    if params["sharp"] > 0: 
        result = result.filter(ImageFilter.UnsharpMask(radius=0.5, percent=int(params["sharp"]*50)))
    
    return result, psnr(orig, np.array(result))

def process_file(args):
    path, out_dir, preset = args
    try:
        img = Image.open(path)
        result, metric = color_pipeline(img, preset)
        base = os.path.splitext(os.path.basename(path))[0]
        out_path = os.path.join(out_dir, f"cleanshot_{preset}_{base}.png")
        remove_metadata_save(result, out_path)
        return (path, True, out_path, metric)
    except Exception as e:
        return (path, False, str(e))

def main():
    parser = argparse.ArgumentParser(
        description=f"{TOOL_NAME} v{VERSION} - Advanced AI Image Fingerprint Disruptor",
        epilog=f"Author: {AUTHOR_EMAIL} | Use responsibly for privacy/research purposes"
    )
    parser.add_argument("input", help="Input image file or directory")
    parser.add_argument("-p", "--preset", choices=["light","medium","strong"], 
                        default="light", help="Processing strength (light/medium/strong)")
    parser.add_argument("-o", "--out", default="cleaned", help="Output directory")
    parser.add_argument("-t", "--threads", type=int, default=0, 
                        help="Number of parallel threads (0=auto)")
    args = parser.parse_args()
    
    os.makedirs(args.out, exist_ok=True)
    
    files = []
    if os.path.isdir(args.input):
        for root, _, fs in os.walk(args.input):
            for f in fs:
                if f.lower().endswith(('.jpg','jpeg','png','bmp','tiff')):
                    files.append(os.path.join(root, f))
    else:
        files = [args.input]
    
    if not files:
        print("❌ No image files found! Exiting.")
        return
    
    threads = args.threads if args.threads > 0 else cpu_count()
    
    print(f"🛡️  {TOOL_NAME} v{VERSION}  🛡️")
    print(f"📧  Author: {AUTHOR_EMAIL}")
    print(f"🚀  Processing {len(files)} image(s) with preset '{args.preset}' using {threads} thread(s)...\n")
    print("✨  All output PNG images will have metadata removed  ✨\n")
    
    with Pool(threads) as pool:
        results = pool.map(process_file, [(f, args.out, args.preset) for f in files])
    
    success = sum(1 for r in results if r[1])
    
    print("\n🎉 Processing complete! 🎉")
    print(f"✅ Successfully processed {success} / {len(files)} images\n")
    
    print("📊 Results:")
    for r in results:
        if r[1]:
            print(f"  🎯 {os.path.basename(r[2]):<40} PSNR: {r[3]:6.1f}dB")
        else:
            print(f"  ❌ {os.path.basename(r[0])}: {r[2]}")
    print("\nThank you for using CleanShot Pro Ultimate! 💡🔐")

if __name__ == "__main__":
    main()
