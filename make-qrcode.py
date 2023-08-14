import pyqrcode;
from PIL import Image;

url = input("Enter the URL to QR: ")

qr_code = pyqrcode.create(url)
qr_code.png("QRCode.png", scale=4)
Image.open("QRCode.png")
