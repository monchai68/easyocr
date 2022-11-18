import easyocr


reader = easyocr.Reader(['th'])
result = reader.readtext('334.jpg')
print(result)

for x in result:
    print(x[1])