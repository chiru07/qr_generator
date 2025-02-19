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