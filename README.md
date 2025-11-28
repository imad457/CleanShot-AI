CleanShot AI Pro v1.2

Advanced AI Fingerprint Disruptor + Metadata Remover

CleanShot AI Pro automatically disrupts AI image recognition fingerprints while removing all metadata (EXIF, GPS, camera info) and saving as clean PNG files. Perfect for privacy-conscious users.
✨ Key Features
Feature	Description
3 Strength Presets	light (subtle), medium (balanced), strong (aggressive)
Auto Metadata Removal	Strips EXIF/GPS/device info completely
Multiprocessing	Process entire folders in parallel (-t 4)
Batch Processing	Single files or entire directories
Clean PNG Output	Lossless PNG with zero metadata
🎯 Quick Start
Prerequisites

bash
# Required Python packages (usually pre-installed)
pip install numpy pillow

Usage Examples

bash
# Single image - light preset (default)
python3 cleanshot.py image.jpg

# All 3 presets
python3 cleanshot.py image.jpg -p light -o output/
python3 cleanshot.py image.jpg -p medium -o output/
python3 cleanshot.py image.jpg -p strong -o output/

# Process entire folder with 4 parallel threads
python3 cleanshot.py images/ -p medium -o cleaned/ -t 4

📋 Full Command Reference

bash
python3 cleanshot.py <input> [OPTIONS]

Positional Arguments:
  input                  Image file or directory of images

Optional Arguments:
  -h, --help             Show this help message
  -p, --preset {light,medium,strong}
                         Disruption strength (default: light)
  -o, --out DIR          Output directory (default: current)
  -t, --threads N        Parallel processes (default: auto-detect)

🔧 Preset Comparison
Parameter	light	medium	strong	Visual Impact
Noise	0.3	0.8	1.8	Subtle → Noticeable → Strong
Blur	0.3	0.6	1.2	Minimal → Medium → Heavy
Color	1%	2%	5% desat.	Natural → Slightly dull → Washed
Brightness	+0.5%	+1%	+2.5%	Neutral → Brighter → Very bright
Sharpen	50%	80%	120%	Natural → Enhanced → Aggressive
🛡️ Privacy & Security Benefits

text
✅ Disrupts AI/ML image fingerprinting
✅ Removes ALL EXIF/GPS metadata
✅ No camera/device info leakage
✅ Clean PNG output (no hidden data)
✅ Parallel processing = fast bulk cleaning

📁 Example Output

text
Input:  mine.jpg (2.5MB with EXIF)
Output: clean_light_mine.png (1.8MB, NO metadata)
        clean_medium_mine.png
        clean_strong_mine.png

Verify metadata removal:

bash
exiftool clean_light_mine.png  # Should show NO personal data

🚀 Processing Pipeline

text
1. Load image → Convert to RGB
2. Add Gaussian noise (preset strength)
3. Apply Gaussian blur (preset radius)
4. Reduce color saturation (preset %)
5. Adjust brightness (preset %)
6. Apply sharpening filter (preset strength)
7. Create NEW image → Copy pixels only
8. Save as PNG → ZERO metadata

💾 Requirements
Package	Purpose
numpy	Image array processing
Pillow	Image loading/saving/filtering
multiprocessing	Parallel batch processing

No other dependencies! Works on any Python 3.8+ system.
📊 Performance
Images	Threads	Time
10	1	8s
10	4	2s
100	8	12s
🤝 Contributing

    Fork the repository

    Create feature branch (git checkout -b feature/AmazingFeature)

    Commit changes (git commit -m 'Add some AmazingFeature')

    Push to branch (git push origin feature/AmazingFeature)

    Open Pull Request

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Author

imsecure4@gmail.com

Made with ❤️ for privacy-conscious developers.
<div align="center">

<sub>Star this repo if it helps you! ⭐</sub>
</div>
