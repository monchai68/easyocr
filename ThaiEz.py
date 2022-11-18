import easyocr
from tkinter import *
from PIL import Image
from matplotlib import pyplot as plt
import io
import os

class ThaiEz:

	n=0
	path = "D:\ocr\in"
	path_out = "D:\ocr\out"
	files = [""]
	status = ""
	lang = "th"
	
	def __init__(self,path_in,path_out,language):
		self.path = path_in
		self.path_out = path_out
		self.files = [""]
		self.status ="Start OCR"
		self.lang = language
				
	def get_status(self):
		return self.status

	def output_file(self,filename, data):
		file = open(filename, "a" ,encoding='utf8')
		file.write(data)
		file.close()


	def get_file(self, path):
		dir_list = os.listdir(path)
		self.files = dir_list
		return self.files

	def remove_Blank_Line(self):
		#เอาบรรทัดว่างออก
		filein = self.path_out+"/"+"out.txt"
		fileout = self.path_out+"/"+ "blank.txt"
		
		# opening and creating new .txt file
		with open(filein, 'r',encoding="utf8") as r, open(fileout, 'w',encoding="utf8") as o:
			for line in r:
				if line.strip():
					o.write(line)
		print("finish Remove Blank Line")

	def ocr_array(self,result):
		k=""
		for x in result:
			k = k+x[1] +"\n"
		return k
	
	def Run(self):
		n=0
		self.get_file(self.path)
		#image_file = StringVar()
		for  f in self.files:
			image_file = self.path +"/"+f
			img = Image.open(image_file) 
			if self.lang != "2":
				reader = easyocr.Reader([self.lang])
				result = reader.readtext(img)
			if self.lang == "2":
				reader = easyocr.Reader(['th','en'])
				result = reader.readtext(img)
			ocr_result = self.ocr_array(result)
			fileout = self.path_out+"/"+"out.txt"
			self.output_file(fileout ,ocr_result)
			n=n+1
			txt = "finished Page {} of {}"
			self.status = txt.format(n,len(self.files))
			print(txt.format(n,len(self.files)))
		self.remove_Blank_Line()  #เอาบรรทัดว่างออก 

		

	

		
		

	# get_file(path)
	
	# for  f in files:
	# 	image_file = path +"\\"+f
	# 	img = Image.open(image_file)
	# 	ocr_result = pytesseract.image_to_string(img,lang='tha')
	# 	output_file("argong.txt",ocr_result)
	# 	n=n+1
	# 	txt = "finished Page {} of {}"
	# 	print(txt.format(n,len(files)))



