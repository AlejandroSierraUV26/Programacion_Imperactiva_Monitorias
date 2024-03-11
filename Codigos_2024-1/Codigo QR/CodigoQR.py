import qrcode

# Grupo 51 -> https://chat.whatsapp.com/Kf5VcxbSYwu5jDZtbnozP0
# Grupo 52 -> https://chat.whatsapp.com/D7bQ2fRvYVSBWnsEDIZLb0
# Grupo 53 -> https://chat.whatsapp.com/Ik34vT6AVM35IgFlptsLkW
# Grupo 54 -> https://chat.whatsapp.com/Huz5hveBtOHENnk2drirpA

# Test 1 -> https://forms.gle/hZrDRCZTfGPF2HhZ8
# Test 2 -> https://forms.gle/Da9FchGXojjmBMbv6

def generar_qr_desde_link(link,nombre_codigo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    qr_code = qr.make_image(fill_color="black", back_color="white")
    qr_code.save(f"{nombre_codigo}.png")

if __name__ == "__main__":
    enlace = input("Ingresa el enlace: ")
    nombre_codigo = input("Ingresa el titulo del código QR: ")
    generar_qr_desde_link(enlace,nombre_codigo)

    print("Se ha generado el código QR exitosamente.")
