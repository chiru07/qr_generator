# QR Code Generator

This project generates QR codes using Python. It allows you to embed URLs or any text into a QR code that can be scanned using a mobile device.

## Features
- Generate QR codes for any URL or text.
- Customize QR code size and border.
- Save the QR code as an image file.
- Display the QR code instantly.

## Installation
Make sure you have Python installed. Then, install the required dependency:

sh
pip install qrcode[pil]


## Usage
Run the Python script to generate a QR code:

python
import qrcode

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the website URL
qr.add_data('https://github.com/chiru07')
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save or show the QR code
img.show()  # Opens the image
img.save("chiru07_qr.png")  # Saves the QR code as an image file


## Output
After running the script, a QR code image will be generated and saved as `chiru07_qr.png`.

## License
This project is open-source and available under the MIT License.

## Author
[chiru07](https://github.com/chiru07)

