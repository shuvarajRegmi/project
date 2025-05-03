from modulefinder import Module
import qrcode
data=input('Enter the text or url:').strip()
filename=input('enter the filename:').strip()
qr=qrcode(data)
image=qr.make_image(file_color='black', black_color='white')
image.save(filename)
print('qr code saved as {filename}')
