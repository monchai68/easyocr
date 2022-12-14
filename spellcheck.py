#Read in the file

class spellcheck:
    filein = ""
    fileout = ""

    def __init__(self,filein,fileout):
        self.filein = filein
        self.fileout = fileout
    
    def checkspell(self):
        with open(self.filein,'r',encoding="utf8") as file:
            filedata = file.read()

        mydict = {"ตัง":"ตั้ง","เรือง":"เรื่อง","เรอง":"เรื่อง","เหมอน":"เหมือน","นี":"นี้","หมิน":"หมิ่น","เชือ":"เชื้อ","ที":"ที่",
        "ครัง":"ครั้ง" ,"หมัน":"หมั่น","สําเรจ":"สำเร็จ","ซึง":"ซึ่ง","นัน":"นั้น","ขาวสาร":"ข้าวสาร","ญีปุ่น":"ญี่ปุ่น" ,"เมือ":"เมื่อ","เกี่ยรติ":"เกียรติ" ,
        "มันคง":"มั่นคง","ตืน":"ตื่น" ,"เมื่อง":"เมือง","รุ่งเรื่อง":"รุ่งเรือง","โซค":"โชค","ซึง":"ซึ่ง","ซาว":"ชาว" ,"นี้้":"นี้","เพยร":"เพียร","เพิม":"เพิ่ม",
        "ขิน":"ขึ้น","ขึน":"ขึ้น","ยิงขึ้น":"ยิ่งขึ้น","โลกี่่่ยะ":"โลกียะ","นํามนต์":"น้ำมนต์","นัน":"นั้น","ตาง":"ต่าง","อยู":"อยู่","จัดขืน":"จัดขึ้น","ซูมชน":"ชุมชน",
        "ดนเอง":"ตนเอง","พึงตนเอง":"พึ่งตนเอง","ขันตอน":"ขั้นตอน","สินเชิง":"สิ้นเชิง","ตังมัน":"ตั้งมั่น","นำไหล":"น้ำไหล","ทั้งสิน":"ทั้งสิ้น","กลันกรอง":"กลั่นกรอง",
        "น็อย":"น้อย","เวียนรู้":"เรียนรู้","ต่ำรา":"ตำรา","อากัง":"อากง","กลันกรอง":"กลั่นกรอง","เมื่อง":"เมือง","หนังลือ":"หนังสือ","ดิ":"ดี",
        "เนี้ยม":"เนียม","เชียวชาญ":"เชี่ยวชาญ","บริสุทธิ":"บริสุทธิ์","สั่งเกต":"สังเกต","เพี่ยง":"เพียง","ซ้า":"ช้า","หมั่นเพี่ยร":"หมั่นเพียร",
        "โซค":"โชค","ลัมเหลว":"ล้มเหลว","ทันที่":"ทันที","หมั่นเพี่ยร":"หมั่นเพียร","มีคา":"มีค่า","ญีปุ่น":"ญี่ปุ่น","หรื่อก":"หรอก","จะม":"จะมี","เสื่อผ้า":"เสื้อผ้า",
        "ซือ":"ซื้อ","ต่ำรา":"ตำรา","ไน":"ใน","หรื่อ":"หรือ","ไจ้":"ไว้","สินเดือน":"สิ้นเดือน","อยาง":"อย่าง","ดงนน":"ดังนั้น","ซาว":"ชาว","เคลิด":"เคล็ด",
        "บูตร":"บุตร","จวิง":"จริง","ฟ่ม":"ฟุ่ม","นัง":"นั่ง","ทก":"ทุก","แท็กซี":"แท็กซี่","จะม":"จะมี","เหมอน":"เหมือน","เช่นนิ":"เช่นนี้",
        "หลิก":"หลีก","เงน":"เงิน","สูรา":"สุรา","ดืม":"ดื่ม","สินชีวิต":"สิ้นชีวิต","สินเปลือง":"สิ้นเปลือง","มีนงง":"มึนงง","ปารง":"บำรุง","รดนำ":"รดน้ำ",
        "พูใหญ่":"ผู้ใหญ่","ธ่ม":"ร่ม","นำแข็ง":"น้ำแข็ง","หยุดยัง":"หยุดยั้ง","ถิอ":"ถือ","นิง":"นิ่ง","คั้ง":"คั่ง","เปลียน":"เปลี่ยน","อาชพ":"อาชีพ","แลว":"แล้ว",
        "ก็ม":"ก็มี","น์อย":"น้อย","กลืบ":"กลีบ","เยียม":"เยี่ยม","ไซร":"ไซ้ร","ซัดเจน":"ชัดเจน","ตอง":"ต้อง","ซีพ":"ชีพ",
        "พู้":"ผู้","เฟา":"เฝ้า","สถานการณ":"สถานการณ์","ผ่านพัน":"ผ่านพ้น","ดิ":"ดี","เห้":"ให้","วุด":"จุด","สูโขทัย":"สุโขทัย","ความเชือ":"ความเชื่อ",
        "ขืนมา":"ขึ้นมา","ความเชื้อ":"ความเชื่อ","ทัง":"ทั้ง","เรือย":"เรื่อย","เริม":"เริ่ม","พันทุกข์":"พ้นทุกข์","ทัว":"ทั่ว","ซูมชน":"ชุมชน",
        "สิงแวดล้อม":"สิ่งแวดล้อม","หลุดพัน":"หลุดพ้น","ไฝ่":"ใฝ่","นําใจ":"น้ำใจ","สิง":"สิ่ง","นยม":"นิยม","กระทัง":"กระทั่ง","กระทั้ง":"กระทั่ง","พืน":"พื้น",
        "อินๆ":"อื่นๆ","มังคัง":"มั่งคั่ง","บูคคล":"บุคคล","ที่่่่่่ตํา":"ที่ต่ำ","ว้าน":"บ้าน","เผือ":"เผื่อ","เลียงง่าย":"เลี้ยงง่าย","เลือมใส":"เลื่อมใส","เป็น้":"เป็น",
        "เกือ":"เกื้อ","หนึง":"หนึ่ง","เน็น":"เน้น","ขืน":"ขึ้น","อืน":"อื่น","กักตูน":"กักตุน","ผู้อิน":"ผู้อื่น","คนอิน":"คนอื่น","เชื้อม":"เชื่อม" ,"ที่่":"ที่่",
        "ทํา":"ทำ","บูญ":"บุญ","อยู่่":"อยู่","ลิน":"ลิ้น","ตังมัน":"ตั้งมั่น","สามัคิ":"สามัคคี","หนู่ม":"หนุ่ม","มู่งมั่น":"มุ่งมั่น","มังมี":"มั่งมี","หมืน":"หมื่น",
        "ยิมแย้ม":"ยิ้มแย้ม","ศัตร":"ศัตรู","บึงตึง":"บึ้งตึง","เรนะ":"ชนะ","ที่่":"ที่","เครอง":"เครื่อง","ขีน":"ขึ้น","เดีน":"เดิน","คณ":"คุณ","หลิกเลียง":"หลีกเลี่ยง",
        "สูภาพ":"สุภาพ","เพี่่ยง":"เพียง","สินชีวิต":"สิ้นชีวิต","บำธุง":"บำรุง","ถิอ":"ถือ","เปลิยน":"เปลี่ยน","อาชพ":"อาชีพ","ชาต":"ชาติ","หรอ":"หรือ",
        "แหง":"แห่ง","ขีน":"ขึ้น","เด็น":"เดิน","นำตก":"น้ำตก","สดชีน":"สดชื่น","เคิน":"เดิน","อิมเอม":"อิ่มเอม","รีนรมย์":"รื่นรมย์","กิง":"กิ่ง",
        "ตำ":"ต่ำ","เด้นท์":"เด๊นท์","แคด":"แดด","นำค้าง":"น้ำค้าง","พื่น":"พื้น","กะเหรียง":"กะเหรี่ยง","ชวย":"ช่วย","เห็นือ":"เหนือ","ชนิค":"ชนิด",
        "ที่ม":"ทีม","เดีม":"เดิม","ธวย":"รวย","เรีม":"เริ่ม","มธยสถ์":"มัธยัสถ์","พลัก":"ผลัก","ลำยุค":"ล้ำยุค","ซอบ":"ชอบ","จงต้อง":"จึงต้อง",
        "อิม":"อิ่ม","ราบรีน":"ราบรื่น","ราบรีน":"ราบรื่น","ลูล่วง":"ลุล่วง","ฟันเฟื่อง":"ฟันเฟือง","หมูน":"หมุน","บรรลู":"บรรลุ","รูง":"รุง","อยา":"อย่า",
        "บรรทด":"บรรทัด","เปน":"เป็น","หวาดหวัน":"หวาดหวั่น","หลีกเลี้ยง":"หลีกเลี่ยง","นั้นแล":"นั่นแล","ซอสัตย์":"ซื่อสัตย์","น์อม":"น้อม","ต่ำแหน่ง":"ตำแหน่ง",
        "เลิอน":"เลื่อน","เดีอน":"เดือน","ชีอ":"ชื่อ","บูรุษ":"บุรุษ","มูมมอง":"มุมมอง","ซอบ":"ชอบ","จูด":"จุด","ษัด":"ชัด","ธางวัล":"รางวัล","หนั่งสือ":"หนังสือ",
        "อิ่น":"อื่น","เฉลีย":"เฉลี่ย","เอือ":"เอื้อ","เพลิ้น":"เพลิน","เกิดขน":"เกิดขึ้น","สูดท้าย":"สุดท้าย","อิ่น":"อื่น","สถานี้":"สถานี","สินหวัง":"สิ้นหวัง",
        "คลูก":"คลุก","ปฐพี่":"ปฐพี","ทัอ":"ท้อ","ลิม":"ลืม","ซีวิต":"ชีวิต","สั่งคม":"สังคม","ปลิก":"ปลีก","ชนชม":"ชื่นชม","คิอ":"คือ",
        "วิธิ":"วิธี","เกด":"เกิด","เก้าอี":"เก้าอี้","สูขุม":"สุขุม","น์อง":"น้อง","ชัวโมง":"ชั่วโมง","เสริจ":"เสร็จ","เตรยม":"เตรียม","ถี":"ถี่","ดีบ":"ดิบ",
        "ปัอง":"ป้อง","เท่าเที่่ยม":"เท่าเทียม","เดีม":"เดิม","เพ่อ":"เพื่อ","นำใจ":"น้ำใจ","ตีนสาย":"ตื่นสาย","เหยือ":"เหยื่อ","เรือง":"เรื่อง","เทียว":"เที่ยว",
        "เทยว":"เที่ยว","เนื่อหา":"เนื้อหา","เนือหา":"เนื้อหา","ชาติิ":"ชาติ","เคลือน":"เคลื่อน" ,"หนาที่":"หน้าที่","อย่าก":"อยาก","ทั่วร์":"ทัวร์",
        "ยิงใหญ่":"ยิ่งใหญ่","แตงกาย":"แต่งกาย","เบืองหน้า":"เบื้องหน้า","ลืน":"ลื่น","ทีมี":"ที่มี","เกยว":"เกี่ยว","ชีน":"ชื้น",
        "หนาร้อน":"หน้าร้อน","เต้นท์":"เต๊นท์","คี":"ดี","คําน้ำ":"คำนำ","ตัม":"ต้ม","บะหมี":"บะหมี่","หรือก":"หรอก","ซีอิว":"ซีอิ๊ว","น้ำทาง ":"นำทาง",
        "สดซีน":"สดชื่น","วู้":"รู้","เป่าหมาย":"เป้าหมาย","เครดีต":"เครดต","เห็นี้ยว":"เหนียว","หมูน":"หมุน","เจ็ง":"เจ๊ง","เหยือ":"เหยื่อ",
        "ที่่":"ที่","แผ่นดีน":"แผ่นดิน","ปลิก":"ปลีก","เฉิน":"เงิน","ซีง":"ซึ่ง","ธานื":"ธานี","วิถี่":"วิถี","เนน":"เน้น","เนี้ยน":"เนียน","ฉีบ":"ฉิบ",
        "เฉือย":"เฉื่อย","เกี่ยร์":"เกียร์","เที่ยบ":"เทียบ","เล้น":"เส้น","ชัว":"ชั่ว","เนือ":"เนื้อ","ซึน":"ซืน","วิง":"วิ่ง",
        "สวิ่ง":"สวิง","กระทึม":"กระหึ่ม","ตํา":"ต่ำ","ตํ่าแหน่ง":"ตำแหน่ง","ตํ่าหนิ":"ตำหนิ","สะดื้อ":"สะดือ","สต่างค์":"สตางค์","เสถี่ยร":"เสถียร",
        "กลิ้น":"กลิ่น","ประดีษฐ์":"ประดิษฐ์","ดี้น":"ดิ้น","ตั่ง":"ดั่ง","ซาย":"ชาย","นาที่":"นาที","เท่านั่น":"เท่านั้น","กิโมง":"กี่โมง",
        "เชื้อว่า":"เชื่อว่า","ชาติาน":"ซาตาน","สถ้าปัตยกรรม":"สถาปัตยกรรม","มีี":"มี","ยิงยวด":"ยิ่งยวด","เที่ยน":"เที่ยน","เห็นื่อย":"เหนือย",
        "เห็นือย":"เหนือย","เห็นี้ยว":"เหนียว","พั้น":"พ้น","คุณะ":"คณะ","เดื้อด":"เดือด","เที่ยน":"เทียน","หน้ามีด":"หน้ามืด","สถ้าน":"สถาน","มีา":"มา",
        "เรียน์":"เรียน","ง่าน":"งาน","ซั้า":"ซ้ำ","อิ้ม":"ยิ้ม","ก้นเอง":"กันเอง","ถ้าม":"ถาม","สักที่":"สักที","ดีน":"ดิน","ยื้น":"ยืน","ถ้ากถ้าง":"ถากถาง",
        "งาน์":"งาน","จืะ":"จ๊ะ","ท่าน์":"ท่าน","หนั่ง":"หนัง","บุย":"ปุย","มัน้":"มัน","แนะน้ำ":"แนะนำ","ชืน":"ชื่น","เกื้อบ":"เกือบ","ร์า":"รำ",
        "ปั่ม":"ปั๊ม","เมี่ยน":"เฆี่ยน","เที่ยน":"เทียน","ห็บ":"หีบ","เดื้อน":"เดือน","ต่ำหมาก":"ตำหมาก","สัปดาห":"สัปดาห์","เกียว":"เกี่ยว",
        "เหนือย":"เหนื่อย","สือสาร":"สื่อสาร","หรอ":"หรือ" ,"ที่วี":"ทีวี","หนาย":"หน่าย","เครยด":"เครียด","สราง":"สร้าง","ขึ่น":"ขึ้น",
        "อืเมล":"อีเมล","ผอน":"ผ่อน","พงพา":"พึ่งพา","หนง":"หนึ่ง","เตม":"เต็ม","ไช้":"ใช้","เครดต":"เครดิต","ดอกเบีย":"ดอกเบี้ย","เอื่อม":"เอื้อม",
        "หรอ":"หรือ","หรือก":"หรอก","เลอก":"เลือก","ซื้อสัตย์":"ซื่อสัตย์","ถิน":"ถิ่น","อาบน้า":"อาบน้ำ","เหนี้ยว":"เหนี่ยว","สมำ":"สม่ำ",
        "สินสุด":"สิ้นสุด","มหือมา":"มหึมา" ,"น้อยู่":"นอยู่" ,"เดื้อด":"เดือด" ,"ต่ำแหน่ง":"ต่ำแหน่ง","เก้าอี้้":"เก้าอี้","น้อย่า":"นอย่า","ซึดเซียว":"ซีดเซียว"}   # ,"":""
        #Replace the target string
    
        print("Spellcheck Processing...")

            #write the file out again

        for x in mydict:
            k= mydict.get(x)
            filedata = filedata.replace(x,k)
            

        with open(self.fileout,'w',encoding="utf8") as file:
            file.write(filedata)

        print("finished Spellcheck")