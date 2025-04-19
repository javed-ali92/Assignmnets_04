import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


data = "Hello, this is a QR code!"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
)

# Generate QR Code
qr.add_data(data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="red", back_color="white")
qr_img.save("E:/qr_code/qrcode.png")




# # print the QR code
img =  Image.open("E:/qr_code/qrcode.png")
result = decode(img)
print(result)