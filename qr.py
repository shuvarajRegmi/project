import qrcode

data = input("Enter the text or url: ")
filename = input("Enter the filename: ")

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save(f"{filename}.png")

