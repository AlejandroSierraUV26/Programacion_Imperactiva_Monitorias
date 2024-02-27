import qrcode
# Link -> Formulario = https://forms.gle/TgSZXYy4eHtjzaECA
def generar_qr_desde_link(link,nombre_codigo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)

    qr_code = qr.make_image(fill_color="red", back_color="white")

    qr_code.save(f"{nombre_codigo}.png")

if __name__ == "__main__":
    enlace = input("Ingresa el enlace: ")
    nombre_codigo = input("Ingresa el titulo del código QR: ")
    generar_qr_desde_link(enlace,nombre_codigo)

    print("Se ha generado el código QR exitosamente.")