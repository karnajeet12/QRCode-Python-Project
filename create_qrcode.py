# installed qrcode library using pip command to make qrcode
import qrcode
# side note: try to add your resume instead of "resume"


data = "https://bucketforresume.s3.ca-central-1.amazonaws.com/Karnajeet+Sawant.pdf"

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color="orange", back_color="white")

img.save("D:/QRCode_Python_Project/myqrcode1.png")
