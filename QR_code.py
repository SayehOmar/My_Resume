import qrcode

# Direct link to the raw PDF on GitHub
url = "https://raw.githubusercontent.com/SayehOmar/My_Resume.io/main/ESSAYEH-Omar%20Eng%20.pdf"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill="black", back_color="white")

# Save the image to a file
img.save("resume_qr_code.png")
