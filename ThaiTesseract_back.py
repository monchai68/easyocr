import pytesseract
from PIL import Image
from matplotlib import pyplot as plt
import io
import os

def output_file(filename, data):
	file = open(filename, "a" ,encoding='utf8')
	file.write(data)
	file.close()


def get_file(path):
   dir_list = os.listdir(path)
   return dir_list
		
path = "D:\documents\scanDocs\อากงสอนว่า\out"
files = get_file(path)

n=0
for  f in files:
	image_file = path +"\\"+f
	img = Image.open(image_file)
	ocr_result = pytesseract.image_to_string(img,lang='tha')
	output_file("argong.txt",ocr_result)
	n=n+1
	txt = "finished Page {} of {}"
	print(txt.format(n,len(files)))