from ThaiTesseract  import ThaiTesseract
from Remove_unused_Line import Remove_unused_Line

pathin = "D:/ocr/in"
pathout = "D:/ocr/out"
filein = "D:/ocr/out/blank.txt"
fileout = "D:/ocr/out/end.txt"

# ts = ThaiTesseract(pathin,pathout)
# ts.Run()

rl = Remove_unused_Line(filein,fileout)
rl.remove_line()

