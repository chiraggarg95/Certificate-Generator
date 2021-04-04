#import the necessary libraries</pre>
  
import cv2 as cv
from PIL import Image
import os
import base64
# import openpyxl
   

def cert_enc_gen(name, compi):

    template_path = ['./certificates/generate_certificate/' + compi + '.png']

    output_path = './certificates/generate_certificate/gen_certifs/'
    
    font_size = 3
    font_color = (0,0,0)
    
    coordinate_y_adjustment = 15
    coordinate_x_adjustment = 7
    
    for path in template_path:
        
        certi_name = name
        img = cv.imread(path)
 
        font = cv.FONT_HERSHEY_PLAIN              
    
        text_size = cv.getTextSize(certi_name, font, font_size, 10)[0]     
    
        text_x = (img.shape[1] - text_size[0]) / 2 + coordinate_x_adjustment 
        text_y = (img.shape[0] + text_size[1]) / 2 - coordinate_y_adjustment
        text_x = int(text_x)
        text_y = int(text_y)
        cv.putText(img, certi_name,
                (text_x ,text_y ), 
                font,
                font_size,
                font_color, 10)
    
        certi_path = output_path + compi + '.png'
        cv.imwrite(certi_path,img)

        encoded = base64.b64encode(open(certi_path, "rb").read())

        os.remove(certi_path)
        return encoded

