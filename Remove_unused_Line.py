from pickle import TRUE
from turtle import clear
import pythainlp.util
from pythainlp import word_tokenize
import re



class Remove_unused_Line:

    
    filein = ""
    fileout = ""

    def __init__(self,filein,fileout):
        self.filein = filein
        self.fileout = fileout
        

    def find(self,string):
            special_char=re.compile('[@_!$%^&*()<>?\|}{~:#a-zA-Z0-9+=]')
            
            if special_char.search(string) == None:
                return "NO"
            else:
                return "YES"




    def remove_line(self):
        fp =  open(self.fileout, 'w',encoding='utf8')  
        with open(self.filein,encoding='utf8') as file:
            lines = [line.rstrip() for line in file]
        #print(lines)

        ln=[0]  # กำหนดหมายเลขบรรทัด ที่จะลบ อักขระที่อ่านไม่ออก
        tmp=[0]
        l=0  #ใช้นับบรรทัดว่าเกิน 3 บรรทัดหรือยัง
        for i in lines:
            
            n=0
            # if find(i)== "YES":
            #     n=n+3
            if i== "เร      ๑ ๕     1        ะ2  น ญฉ4  ๕-  ส  ๑ -  ส": n=3
            if i != " ":
                tok = word_tokenize(i)
                if len(tok) > 0:
                    res2 = pythainlp.util.isthai(tok[0])
                    if res2 == False and tok[0] !=" " and tok[0]!="“"and tok[0]!="”" and tok[0] != "-" and tok[0] != "(" and tok[0] != "%": n = n+1
                    if len(tok[0]) == 1 and tok[0]!="“"and tok[0]!="”" and tok[0] != "-"and tok[0] !=" " and tok[0] !="."and tok[0] != "(" and tok[0] != "%" :
                        n = n+1
                if len(tok) > 1:
                    res3 = pythainlp.util.isthai(tok[1])
                    if res3 == False and tok[1] !=" " and tok[1]!="“"and tok[1]!="”" and tok[1] != "-"and tok[1] != "(" and tok[1] != "%": n = n+1
                    if len(tok[1]) == 1 and tok[1]!="“"and tok[1]!="”" and tok[1] != "-"and tok[1] !=" "and tok[1] !="." and tok[1] != "(" and tok[1] != "%":
                        n = n+1
                if len(tok) > 2:
                    res4 = pythainlp.util.isthai(tok[2])
                    if res4 == False and tok[2] !=" " and tok[2]!="“"and tok[2]!="”" and tok[2] != "-" and tok[2] != "(" and tok[2] != "%": n = n+1
                    if len(tok[2]) == 1 and tok[2]!="“"and tok[2]!="”" and tok[2] != "-" and tok[2] !=" " and tok[2] !="." and tok[2] != "(" and tok[2] != "%":
                        n = n+1
                if len(tok) > 3:
                    res5 = pythainlp.util.isthai(tok[3])
                    if res5 == False and tok[3] !=" " and tok[3]!="“"and tok[3]!="”" and tok[3] != "-" and tok[3] != "(" and tok[3] != "%": n = n+1
                    if len(tok[3]) == 1 and tok[3]!="“"and tok[3]!="”"  and tok[3] != "-"and tok[3] !=" "  and tok[3] !="." and tok[3] != "(" and tok[3] != "%":
                        n = n+1
                if len(tok) > 4:
                    res6 = pythainlp.util.isthai(tok[4])
                    if res6 == False and tok[4] !=" " and tok[4]!="“"and tok[4]!="”" and tok[4] != "-" and tok[4] != "(" and tok[4] != "%": n = n+1
                
                

                if n >= 3 or len(i) <=2 :   #มีคำผิดเยอะ ไม่ใช่ภาษาไทย
                    if l < 1:     # เรากำหนด array 3 ตัวแรก เป็น 0 
                        ln[l]=l
                        tmp[0]=l     #กำหนดบรรทัดที่ผิด
                    if l > 0:
                        ln.append(l)  # หลังจาก 3 บรรทัด จะเป็นการเพิ่มเข้าไป
                
                    
                # print(i)
                # print(res2)
                # print(res3)
                # print(res4)
                # print(res5)
                # print("n={}".format(n))
                # print("array line number: {}".format(l))
                # print( "Value of ln:".format(ln))
                l=l+1
        ln.pop(0)  
        ln.append(tmp[0])
        # print(ln)
        with open(self.fileout, 'w',encoding='utf8') as fp:
            # iterate each line
            for number, line in enumerate(lines):
                # delete line 5 and 8. or pass any Nth line you want to remove
                # note list index starts from 0
                if number not in ln or number == 0:
                    fp.write(line + "\n")
                    #print(line + "\n")
        print("finished remove unused line")
            
    
    
    
    
    
    
