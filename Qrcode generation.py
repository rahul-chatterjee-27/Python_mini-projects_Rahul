import qrcode

url=input("Enter the url: ").strip() 
filename=input("Enter the file name: ").strip()

qr=qrcode.QRCode(box_size=20,  border=5)
qr.add_data(url)
qr.make(fit=True)

image=qr.make_image(fill_color="black", back_color="white")
image.save(filename)

print(f"QR code is saved as {filename}")