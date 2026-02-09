import qrcode
from PIL import Image
import argparse
import os

def generate_qr_code(data, output_file='qr_code.png', fg_color='black', bg_color='white', logo_path=None):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    try:
        img = qr.make_image(fill_color=fg_color, back_color=bg_color).convert('RGB')
    except ValueError as e:
        print(f"Error: Invalid color specified. {e}")
        return

    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path)
        qr_size = img.size[0]
        logo_size = int(qr_size * 0.2)
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

        pos = ((qr_size - logo_size) // 2, (qr_size - logo_size) // 2)

        img.paste(logo, pos, logo if logo.mode == 'RGBA' else None)

    img.save(output_file)
    print(f"QR code saved as {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a customizable QR code.")
    parser.add_argument("data", help="Text or URL to encode in the QR code")
    parser.add_argument("-o", "--output", default="qr_code.png", help="Output file name (default: qr_code.png)")
    parser.add_argument("-fg", "--fg_color", default="black", help="Foreground color (default: black)")
    parser.add_argument("-bg", "--bg_color", default="white", help="Background color (default: white)")
    parser.add_argument("-l", "--logo", help="Path to logo image to embed in the center")

    args = parser.parse_args()

    generate_qr_code(args.data, args.output, args.fg_color, args.bg_color, args.logo)
