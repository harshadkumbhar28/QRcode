import qrcode as qr

img = qr.make("https://en.wikipedia.org/wiki/Python_(programming_language)")
img.save("Wikipedia_Python.png")