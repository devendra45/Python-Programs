import pyqrcode
from pyqrcode import QRCode
s="www.geeeksforgeeks.org"
url=pyqrcode.create(s)
url.svg("gfg.png",scale=8)
#print(url.svg)
