import numpy as np
import pytesseract
from pytesseract import Output
#importing required packages and library
import os
import matplotlib.pyplot as plt
import time
import cv2
from pdf2image import convert_from_path

try:
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont
except ImportError:
    import Image

def pdf2images(rootdir):
    pdflist = [f for f in os.listdir(rootdir) if f.endswith('.pdf')]   
    for i in range(len(pdflist)):
        #print(rootdir+pdflist[i]) 
        # 将PDF文件转换为图片
        images = convert_from_path(rootdir+pdflist[i])
        os.remove(rootdir+pdflist[i])
        # 遍历图片列表并保存为图片文件
        for page, pdf in enumerate(images):
            pdf.save(rootdir+pdflist[i]+f'page_{page + 1}.jpg', 'JPEG')  
            pdf.close     
    
def pytesseractimg(path):
    print("打印传入pytesseractimg的图片：",path)
    img = cv2.imread(path)
    #Image.fromarray(img).show()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    img = Image.fromarray(img)
    content = pytesseract.image_to_string(img, lang='eng')
    img.close()
    os.remove(path)
    return content


def jpg2png(path,i):
    # Loading .png image
    png_img = cv2.imread(path)
    # converting to jpg file
    #saving the jpg file
    print(path+'.jpg')
    cv2.imwrite(path+'.jpg', png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

def gif2jpg(path,i):
    gif = cv.VideoCapture(path)
    ret, frame = gif.read()
    cv.imwrite(path+'.jpg', frame)

def imagehandle():
    #读取images文件夹下所有文件的名字
    imagelist = [f for f in os.listdir(rootdir) if f.endswith('.png')]  # 获取所有txt文件的名称
    print(imagelist)
    for i in range(len(imagelist)):
        jpg2png(rootdir+imagelist[i],i)
        os.remove(rootdir+imagelist[i])
    imagelist = [f for f in os.listdir(rootdir) if f.endswith('.gif')]  # 获取所有txt文件的名称
    print(imagelist)
    for i in range(len(imagelist)):
        gif2jpg(rootdir+imagelist[i],i)
        os.remove(rootdir+imagelist[i])
    #print(rootdir+imagelist[0])
    #for i in range(len(imagelist)):
        #img = Image.open(rootdir+imagelist[i])
    #读取images文件夹下所有文件的名字
    imagelist = [f for f in os.listdir(rootdir) if f.endswith('.jpg')]  # 获取所有txt文件的名称
    
    return imagelist
    #print(imagelist)

def readerpic(rootdir):
    imagelist=imagehandle()
    for i in range(len(imagelist)):
        print(rootdir+imagelist[i])        
        result = pytesseractimg(rootdir+imagelist[i])
        result = convert_to_paragraphs(result)
        savetxt(result.encode('utf-8').decode('utf-8'),rootdir)
def savetxt(contents,path):
    #if not os.path.exists(path+".txt"):
        #print(path)
        with open(path+"pic2txt.txt",'a',encoding='utf-8') as f:
            #f.write(path)
            f.write(contents+"\n")        
        f.close()
    #else:
        #print("Files already exists!")
def convert_to_paragraphs(multiline_text):
    # 使用 splitlines() 方法获取每一行
    lines = multiline_text.splitlines()
    # 去除每一行的首尾空白字符
    cleaned_lines = [line.strip() for line in lines]
    # 使用 join() 方法将行连接成一个自然段落
    paragraph = ' '.join(cleaned_lines)
    return paragraph

if __name__ == "__main__":
    rootdir="C:\\Users\\Asun\\Downloads\\"
    while True:
        pdf2images(rootdir)
        readerpic(rootdir)  
        time.sleep(1)   
