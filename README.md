# QR Code Generator

A Python-based command-line tool to generate customizable QR codes with support for custom colors, logo embedding, and high error correction.

---

## ✨ Features

- Generate QR codes from text or URLs  
- Customize foreground and background colors  
- Embed a logo in the center of the QR code  
- High error correction for better scan reliability  
- Save QR codes as PNG image files  

---

## 🛠️ Requirements

- Python 3.x  
- `qrcode` library  
- `Pillow (PIL)` library  

---

## 📂 Project Structure


---

## 📦 Installation (Beginner-Friendly)

### Step 1 — Clone the repository


### Step 2 — Install dependencies

Option 1 (recommended):


OR (if you have a requirements file):


---

## ▶️ Usage

Run the script from the command line using:


---

## 🔧 Options

| Option | Description |
|--------|-------------|
| `-o, --output` | Output file name (default: `qr_code.png`) |
| `-fg, --fg_color` | Foreground color (default: `black`) |
| `-bg, --bg_color` | Background color (default: `white`) |
| `-l, --logo` | Path to logo image to embed in the center |

---

## 📌 Examples

### 1️⃣ Basic QR Code


### 2️⃣ Custom Colors


### 3️⃣ QR Code with Logo


### 4️⃣ Full Customization


---

## 📷 Screenshots (Optional — Add later)

> You can add images like this in GitHub:


Suggested screenshots to add:
- Input command in terminal  
- Generated QR code image  
- QR code with logo  

---

## 📝 Notes

- Supported color formats:  
  - Color names (e.g., `red`, `blue`, `green`)  
  - Hex codes (e.g., `#FF5733`)  
- The logo should preferably be a **square image** for best appearance  
- High error correction is used so that embedding a logo does not affect scanability  

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## 📄 License

This project is open-source.
