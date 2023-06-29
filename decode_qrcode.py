# installed pyzbar library using pip command to decode the qr code.
from pyzbar.pyzbar import decode
# installed pillow library using pip command
from PIL import Image


img = Image.open("D:/QRCode_Python_Project/myqrcode1.png")


result = decode(img)
print(result)
