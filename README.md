
CleanShot Pro v2.3

# CleanShot Pro v2.3  
### Advanced AI Fingerprint Disruptor  
**Author:** imsecure4@gmail.com  
**Status:** Research / Privacy Tool  
**License:** Free for personal use – attribution required

---

## 🛡️ What is CleanShot Pro Ultimate?

CleanShot Pro Ultimate is an advanced image preprocessing tool designed to  
**disrupt AI-based fingerprinting** while keeping the image visually identical  
to the human eye.

It adds **minimal adversarial perturbations**, removes **all metadata**,  
and applies subtle transformations that degrade AI detectors without  
destroying image quality.

This project is part of the field known as:

### **Adversarial Image Perturbation (AIP)**  
(AI vs AI privacy protection)

---

## ✨ Key Features


### ✔ Minimal & high-quality adversarial noise  
Weak but strategically placed noise to confuse ML models.

### ✔ FFT mid-frequency perturbations  
AI detectors rely heavily on mid-band patterns.

### ✔ HSV Color Preservation  
Maintains natural colors — no ugly distortions.

### ✔ Metadata removal  
Output PNG contains **zero EXIF** or camera fingerprints.

### ✔ Strong presets  
- `light` → subtle anti-AI  
- `medium` → balanced  
- `strong` → maximum AI fingerprint disruption  

### ✔ Multiprocessing for fast batch processing  
Process entire folders using all CPU cores.

### ✔ 100% compatible (no extra heavy libraries)  
No `pywt` or deep-learning dependencies.

---

## 📦 Requirements

Install dependencies with:

```bash
pip install pillow numpy

Python version:

Python 3.7+ (Linux, macOS, Windows)


---

🚀 Usage

Process a single image:

python3 cleanshot_pro.py input.jpg

Choose strength:

python3 cleanshot_pro.py input.jpg --preset medium
python3 cleanshot_pro.py input.jpg --preset strong

Process an entire folder:

python3 cleanshot_pro.py images/ --preset strong --out cleaned/

Use all CPU cores:

python3 cleanshot_pro.py images/ -t 0

Custom output directory:

python3 cleanshot_pro.py input.jpg --out protected/


---

🗂️ Output

All processed images are saved as:

cleanshot_<preset>_<original_name>.png

Examples:

cleanshot_light_photo1.png
cleanshot_strong_profile.png


These PNGs contain:

No EXIF

No device metadata

No camera information

No GPS

Modified luminance fingerprint

Distorted mid-frequency signature



---

⚠️ Disclaimer

This project is created strictly for:

privacy research

anti-fingerprinting experiments

understanding AI detection models

academic adversarial ML research


You are fully responsible for any misuse.

By using this tool, you agree:

I 'imsecure4'am not responsible for any illegal or harmful usage

You must include attribution (“Created by : imsecure4@gmail.com")
if you redistribute, modify, or extend the tool



---

🤝 Contribution

You may modify or improve the tool only if you credit the original author:

Original Author: imsecure4@gmail.com

Pull requests for improvements are welcome.


---

⭐ Future Planned Features

Adaptive per-image adversarial search

Face-recognition targeted evasion

Deep gradient-free perturbation engine

Multi-model resistance mode



---

📧 Contact

For collaboration, research use, or improvements:
imsecure4@gmail.com


---

🛡️ Final Note

CleanShot Pro is part of the new era of
AI vs AI Cybersecurity.

Use it responsibly.

---

# إذا تريد 
