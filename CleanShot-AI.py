*# -*- coding: utf-8 -*-
"""
CleanShot AI - Minimal AI Fingerprint Disruptor
Author: imsecure4@gmail.com
"""

import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
import os
import sys

TOOL_NAME = "CleanShot AI"
AUTHOR_EMAIL = "imsecure4@gmail.com"

def print_banner():
    print("=" * 60)
    print(f"{TOOL_NAME}  -  Image Fingerprint Disruption Tool")
    print(f"Author / Contact: {AUTHOR_EMAIL}")
    print("=" * 60)

def minimal_ai_disruption(image_path):
    """
    Apply minimal, visually subtle changes to break AI detection fingerprints
    while preserving the original look of the image as much as possible.
    """
    try:
        print("🔄 Loading image...")
        img = Image.open(image_path).convert("RGB")
        
        # 1) Add very slight noise (almost invisible)
        print("🔬 Adding fine-grained noise...")
        img_arr = np.array(img, dtype=np.float32)
        noise = np.random.normal(loc=0, scale=0.5, size=img_arr.shape)
        img_arr = np.clip(img_arr + noise, 0, 255)
        img = Image.fromarray(img_arr.astype(np.uint8))
        
        # 2) Apply a very light blur
        print("✨ Applying slight smoothing...")
        img = img.filter(ImageFilter.GaussianBlur(radius=0.3))
        
        # 3) Slight color desaturation (1% only)
        print("🎨 Slight color adjustment...")
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(0.99)
        
        # 4) Slight brightness tweak
        print("💡 Slight brightness adjustment...")
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.005)
        
        # 5) Light sharpening to recover fine details
        print("🔪 Restoring sharpness slightly...")
        img = img.filter(ImageFilter.UnsharpMask(radius=0.5, percent=50, threshold=2))
        
        # Save as PNG (lossless)
        base = os.path.basename(image_path)
        name, _ = os.path.splitext(base)
        output_name = f"minimal_disrupted_{name}.png"
        output_path = os.path.join(os.path.dirname(image_path) or ".", output_name)
        
        img.save(output_path, format="PNG", compress_level=1)
        print(f"✅ Saved: {output_path}")
        print("📊 Processed by:", TOOL_NAME)
        print("📧 Contact:", AUTHOR_EMAIL)
        
        return img
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    print_banner()
    
    if len(sys.argv) < 2:
        print("Usage:")
        print(f"  python3 {os.path.basename(__file__)} <image_path>")
        print("\nExample:")
        print(f"  python3 {os.path.basename(__file__)} mine.jpeg")
        sys.exit(1)
    
    minimal_ai_disruption(sys.argv[1])
