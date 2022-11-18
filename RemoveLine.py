#เอาบรรทัดว่างออก

# opening and creating new .txt file
with open("D:\\code\\python\\argong.txt", 'r',encoding="utf8") as r, open('D:\\code\\python\\ex\\argong_Blank.txt', 'w',encoding="utf8") as o:
    for line in r:
#strip() function
        if line.strip():
            o.write(line)
print("finish")
