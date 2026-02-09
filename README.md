# QR Code Generator

A Python-based tool to generate customizable QR codes with colors, logos, and high error correction.

## Features

- Generate QR codes from text or URLs
- Customize foreground and background colors
- Embed a logo in the center of the QR code
- High error correction for better scan accuracy
- Save QR codes as image files

## Requirements

- Python 3.x
- qrcode library
- Pillow (PIL) library

## Installation

1. Clone or download the project files.
2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line with the following syntax:

```
python qr_generator.py "Your text or URL here" [options]
```

### Options

- `-o, --output`: Output file name (default: qr_code.png)
- `-fg, --fg_color`: Foreground color (default: black)
- `-bg, --bg_color`: Background color (default: white)
- `-l, --logo`: Path to logo image to embed in the center

### Examples

1. Generate a basic QR code:

   ```
   python qr_generator.py "https://www.example.com"
   ```

2. Generate a QR code with custom colors:

   ```
   python qr_generator.py "Hello World" -fg red -bg yellow
   ```

3. Generate a QR code with a logo:

   ```
   python qr_generator.py "https://www.example.com" -l logo.png -o custom_qr.png
   ```

4. Full customization:

   ```
   python qr_generator.py "Your message" -fg blue -bg white -l logo.png -o my_qr.png
   ```

## Notes

- Supported color formats: color names (e.g., 'red', 'blue') or hex codes (e.g., '#FF0000')
- Logo should be a square image for best results
- High error correction allows for logo embedding without affecting scanability
