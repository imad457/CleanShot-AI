CleanShot AI - Minimal AI Fingerprint Disruptor

    What is CleanShot AI?
    CleanShot AI is a small Python tool that applies minimal, visually subtle changes to an image in order to disrupt AI-based image detection or fingerprinting, while keeping the image looking almost identical to the human eye.

    Features

        Adds very light, fine-grained noise to the image.

        Applies a tiny Gaussian blur and a small sharpening step.

        Performs micro-adjustments to color saturation and brightness.

        Saves output as PNG (lossless) and strips sensitive metadata.

    Usage

        Requirements:

            Python 3

            Pillow (PIL)

            NumPy

        Run:
        python3 CleanShot-AI.py <image_path>

        Example:
        python3 CleanShot-AI.py  photo.jpeg

        Output:
        The tool will create a new file in the same directory:
        minimal_disrupted_<original_name>.png

    Metadata
    The output PNG does not contain EXIF or camera-related metadata. Only basic technical fields like image size, bit depth, and color type remain (these are inherent to the PNG format and not privacy-relevant).

    Tuning the Strength
    If you want to increase the strength against certain AI detection tools, you can:

        Increase the noise slightly (for example, change scale from 0.5 to 0.8).

        Increase the blur radius from 0.3 to 0.5.

    After each change, test the new image on the AI detection website or tool you are using, and find the lowest visible change that gives you the lowest "AI detected" score.

    Disclaimer
    This tool is intended for educational and research purposes only (e.g., privacy, anti-fingerprinting, and understanding AI detectors). Use it responsibly and according to the rules of the platform or challenge you are participating in.

    Contact
    For feedback, ideas, or collaboration:
    Email: imsecure4@gmail.com
