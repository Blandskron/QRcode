import qrcode

# Definir la URL del documento
documento_url = "https://drive.google.com/file/d/1U31wT7suVgbBD80GCGpdZ7Aty-CgewJK/view?usp=sharing"

# Crear el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(documento_url)
qr.make(fit=True)

# Generar la imagen del código QR
imagen = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen del código QR como archivo
imagen.save("codigo_qr.png")
