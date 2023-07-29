import qrcode

# Define the URL of the document
document_url = "###"

# Create the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(document_url)
qr.make(fit=True)

# Generate the QR code image
image = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image as a file
image.save("qr_code.png")
