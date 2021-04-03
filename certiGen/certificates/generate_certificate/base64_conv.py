import base64
import os
def base64Conv(compi):
    
    a = os.listdir('./')
    print(a)
    # encoded = base64.b64encode(open(path, "rb").read())
    return a

base64Conv('bootcamp_2020')