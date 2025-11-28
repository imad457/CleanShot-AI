#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
CleanShot AI Pro v1.2 - Light/Medium/Strong presets + Automatic Metadata Removal
Author: imsecure4@gmail.com
✅ Automatically removes all Metadata + saves as 100% clean PNG
"""

import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
import os
import sys
import argparse
import random
from multiprocessing import Pool, cpu_count

TOOL_NAME = "CleanShot AI Pro"
AUTHOR_EMAIL = "imsecure4@gmail.com"

def print_banner():
    """Prints program banner with tool name and author contact info."""
    print("=" * 70)
    print(f"{TOOL_NAME} v1.2 - 3 Presets + AUTO Metadata Removal ✅")
    print(f"Author / Contact: {AUTHOR_EMAIL}")
    print("=" * 70)

# 🎯 Preset parameters for light, medium, and strong image disruption
PRESETS = {
    "light": {
        'noise': 0.3,   # Standard deviation for Gaussian noise
        'blur': 0.3,    # Gaussian blur radius
        'color': 0.01,  # Color desaturation fraction
        'brightness': 0.005,  # Brightness increase fraction
        'sharp': 50     # Sharpening intensity percent
    },
    "medium": {
        'noise': 0.8,
        'blur': 0.6,
        'color': 0.02,
        'brightness': 0.01,
        'sharp': 80
    },
    "strong": {
        'noise': 1.8,
        'blur': 1.2,
        'color': 0.05,
        'brightness': 0.025,
        'sharp': 120
    }
}

def remove_metadata_save(img, output_path):
    """
    Save PNG image without any metadata by creating a new image and copying pixel data.
    
    Args:
        img (PIL.Image): Image to save
        output_path (str): Path to save the PNG file
    
    Returns:
        bool: True if saved successfully
    """
    data = list(img.getdata())
    clean_img = Image.new(img.mode, img.size)
    clean_img.putdata(data)
    clean_img.save(output_path, format="PNG", compress_level=1)
    return True

def process_image(args):
    """
    Process a single image applying the preset's distortions,
    then save it as a clean PNG without metadata.

    Args:
        args (tuple): (image_path, preset_name, output_directory)

    Returns:
        tuple: (image_path, success_bool, output_name_or_error)
    """
    image_path, preset_name, output_dir = args
    params = PRESETS[preset_name]
    
    try:
        print(f"🔄 {preset_name.upper()}: {os.path.basename(image_path)}")
        img = Image.open(image_path).convert("RGB")
        img_arr = np.array(img, dtype=np.float32)
        
        # 1️⃣ Apply Gaussian noise with preset std deviation
        noise = np.random.normal(0, params['noise'], img_arr.shape)
        img_arr = np.clip(img_arr + noise, 0, 255)
        img = Image.fromarray(img_arr.astype(np.uint8))
        
        # 2️⃣ Apply Gaussian blur with preset radius
        img = img.filter(ImageFilter.GaussianBlur(radius=params['blur']))
        
        # 3️⃣ Reduce color saturation by preset fraction
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(1.0 - params['color'])
        
        # 4️⃣ Increase brightness by preset fraction
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.0 + params['brightness'])
        
        # 5️⃣ Apply sharpening filter with preset strength and radius
        radius = 0.8 if preset_name == "strong" else 0.5
        threshold = 3 if preset_name == "strong" else 2
        img = img.filter(ImageFilter.UnsharpMask(radius=radius, percent=params['sharp'], threshold=threshold))
        
        # 🔧 Save the image without any metadata
        base = os.path.basename(image_path)
        name, _ = os.path.splitext(base)
        output_name = f"clean_{preset_name}_{name}.png"
        output_path = os.path.join(output_dir, output_name)
        
        remove_metadata_save(img, output_path)
        print(f"✅ {output_name} | 🧹 Metadata REMOVED")
        return (image_path, True, output_name)
        
    except Exception as e:
        print(f"❌ {preset_name}: {os.path.basename(image_path)} - {e}")
        return (image_path, False, str(e))

def get_image_files(path):
    """
    Recursively get all image files in a directory or a single file.

    Args:
        path (str): Path to a file or directory

    Returns:
        list: List of image file paths
    """
    if os.path.isfile(path) and path.lower().endswith(('.png','.jpg','.jpeg','.bmp','.tiff')):
        return [path]
    files = []
    for root, _, filenames in os.walk(path):
        for f in filenames:
            if f.lower().endswith(('.png','.jpg','.jpeg','.bmp','.tiff')):
                files.append(os.path.join(root, f))
    return files

def main():
    """
    Parse arguments, process images using multiprocessing,
    and report success summary.
    """
    print_banner()
    
    parser = argparse.ArgumentParser(description=f"{TOOL_NAME} - 3 Presets + Metadata Cleaner")
    parser.add_argument("input", help="Image file or directory containing images")
    parser.add_argument("-p", "--preset", choices=["light", "medium", "strong"], default="light",
                       help="Effect strength preset: light, medium, or strong")
    parser.add_argument("-o", "--out", default=".", help="Output directory")
    parser.add_argument("-t", "--threads", type=int, default=0, 
                       help="Number of parallel processes (0 for auto)")
    
    args = parser.parse_args()
    
    params = PRESETS[args.preset]
    print(f"🎯 {args.preset.upper()}: noise={params['noise']} | 🧹 AUTO Metadata Removal")
    
    files = get_image_files(args.input)
    if not files:
        print("❌ No images found!")
        sys.exit(1)
    
    os.makedirs(args.out, exist_ok=True)
    threads = args.threads if args.threads > 0 else cpu_count()
    
    print(f"⚡ Processing {len(files)} images with {threads} threads | PNG output without Metadata\n")
    
    tasks = [(f, args.preset, args.out) for f in files]
    with Pool(threads) as pool:
        results = pool.map(process_image, tasks)
    
    success = sum(1 for _, ok, _ in results if ok)
    print(f"\n🎉 Completed! {success}/{len(files)} images processed successfully | All PNGs metadata cleaned!")
    
    for path, ok, result in results:
        if ok:
            print(f"✅ {result}")
        else:
            print(f"❌ {os.path.basename(path)}: {result}")

if __name__ == "__main__":
    main()
