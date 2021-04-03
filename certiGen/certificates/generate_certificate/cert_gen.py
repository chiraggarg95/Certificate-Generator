#import the necessary libraries</pre>
  
import cv2 as cv
from PIL import Image
import os
import base64
# import openpyxl
   

def cert_enc_gen(name, compi):

      
    # template1.png is the template
    # certificate
    # template_path = ['ai_work.jpg', 'blank.jpg', 'bootcamp_2020.png', 'bootcamp_jun_2020.jpg', 'vsm.jpg']
    template_path = [compi+'.png']
    
    # Excel file containing names of 
    # the participants
    # details_path = 'gsocOrgsList.xlsx'
    
    # Output Paths
    output_path = './gen_certifs/'
    
    # Setting the font size and font
    # colour
    font_size = 3
    font_color = (0,0,0)
    
    # Coordinates on the certificate where
    # will be printing the name (set
    # according to your own template)
    coordinate_y_adjustment = 15
    coordinate_x_adjustment = 7
    
    # loading the details.xlsx workbook 
    # and grabbing the active sheet
    # obj = openpyxl.load_workbook(details_path)
    # sheet = obj.active
    
    # printing for the first 10 names in the
    # excel sheet
    for path in template_path:
        
        # grabs the row=i and column=1 cell 
        # that contains the name value of that
        # cell is stored in the variable certi_name
        # get_name = sheet.cell(row = i ,column = 1)
        certi_name = name
        # read the certificate template
        img = cv.imread(path)
 
        # choose the font from opencv
        font = cv.FONT_HERSHEY_PLAIN              
    
        # get the size of the name to be
        # printed
        text_size = cv.getTextSize(certi_name, font, font_size, 10)[0]     
    
        # get the (x,y) coordinates where the
        # name is to written on the template
        # The function cv.putText accepts only
        # integer arguments so convert it into 'int'.
        text_x = (img.shape[1] - text_size[0]) / 2 + coordinate_x_adjustment 
        text_y = (img.shape[0] + text_size[1]) / 2 - coordinate_y_adjustment
        text_x = int(text_x)
        text_y = int(text_y)
        cv.putText(img, certi_name,
                (text_x ,text_y ), 
                font,
                font_size,
                font_color, 10)
    
        # Output path along with the name of the
        # certificate generated

        # im1 = img.convert('RGB')
        # im1.save('./gen_certifs/'+path+'.pdf')

        certi_path = output_path + path
        # Save the certificate                      
        cv.imwrite(certi_path,img)

        encoded = base64.b64encode(open(certi_path, "rb").read())
        # print(encoded)

        # img1 = Image.open(certi_path)
        # im1 = img1.convert('RGB')
        # im1.save('./gen_certifs/0833_'+path+'.pdf')
        os.remove(certi_path)
        return encoded

# enc = func('chirag', 'eureka')
