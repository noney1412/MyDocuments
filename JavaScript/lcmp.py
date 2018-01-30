#PrimeFactor By Chanon Panpila

print(" ")
print(" วิธีการใช้งาน ")
print("-  หา PrimeNumber และหา PrimeFactor ของตัวเลข ")
print("[ปรับปรุง] ++ Add PrimeFactor ")
print("[ปรับปรุง] ++ Add ErrorHandling ")
print("[ปรับปรุง] ++ Add Display List Of Prime ")
print("-  ***คอมผู้เขียนสามารถรันได้ที่ 70000 || มากกว่านั้นก็รอนานครับ ")
print(" ")

def primeFactor(a):
    print("จงหา PrimeFactor ของเลข ",a,)
    
    a = int(a)
    
    if a == 0 or a == 1 :
        print(" ")
        print(" Error ! ")
        print("กรุณาใส่ตัวเลขที่มากกว่า 1 ขึ้นไปครับ")

    elif a >= 70000:
        print(" ")
        print(" Python ก็รอนานหน่อยนะครับ ~")
    
    else:
            
        # ตัวแปร p1 เก็บเลขจำนวนเฉพาะจาก Parameter(a) ที่รับมา
        p1 = [x for x in range(2,a+1) if all(x % y != 0 for y in range(2, x))]
        print("PrimeNumber ได้แก่ ",p1) #ลองปริ้นดูซิ

        #step 1 หาจำนวนเฉพาะที่หารเลขที่เราต้องการลงตัว.
        Devided_Prime = [] # list ไว้เก็บเลขจำนวนเฉพาะที่หารเลขเราลงตัว
        i = 0
        for i in p1: #i ในที่นี้คือ p1[i] ใล่ไปเรื่อยๆ {2,3,5,7,11,....} ใน list p1 
            if(a%i == 0): #เราต้องหา a%i == 0 คือค่า a ที่หารจำนวนเฉพาะใน p1 แล้วมีเศษ = 0 หรือหารลงตัวนั้นเอง 
                Devided_Prime.append(i)
        
        print("จำนวนเฉพาะที่หาร '{0}' ลงตัวได้แก่ {1}".format(a,Devided_Prime))

        #พอได้จำนวนเฉพาะที่หารเลขที่เรารับค่ามาจากฟังก์ชั้นได้แล้ว
        #Step 2 คือเอาจำนวนเฉพาะ จาก Step1 มาหาร A หรือหา หรม. ต่อ
        #แนวคิด a = 84 , Devided_Prime = {2,3,7} --> เลขที่จะเอามาหาร(เริ่มจากน้อยไปมาก)
        """
        วิธีทำ :
        1.  84/2 = 42         |{2,3,7} ใช้ Devided_Prime[0] 
        2.  42/2 = 21         |{2,3,7} ใช้ Devided_Prime[0]
        3.  21/3 = 7          |{2,3,7} ใช้ Devided_Prime[1] ใช้ 2 หารไม่ได้ ใช้ 3 แทน
        4.  7/7  = 1          |{2,3,7} ใช้ Devided_Prime[2] ใช้ 3 หารไม่ได้ ใช้ 7 แทน

        กำหนดตัวแปร
        1. a/Devided_Prime[0] = Answer     | a = 84 , Devided_Prime[0] = 2
                .
                .
                .
        4. a/Devided_Prime[2] = 1 --> Answer สุดท้ายเป็น 1

        สรุป : ใช้ while loop เพราะไม่รู้ต้องหารกี่ครั้ง แต่ได้ Answer สุดท้ายเป็น 1
        
        """
        i = 0 #เซ็ทค่า i
        listAns = [] #สร้าง list ไว้เก็บคำตอบของผลหาร
        listPrimeFactor = [] #อันนี้คือ list คำตอบที่เราต้องการจริงๆ

        #ใช้ While จนกว่า Answer สุดท้ายจะเท่ากับ 1

        while a!=1 : #ขณะที่ Answer ไม่ใช่ 1 ให้ทำ ... (เพราะถ้ามันเท่ากับ 1 มันจะหยุด)
            a = a/Devided_Prime[i] #เริ่มหารจาก Devided_Prime[0] เริ่มจากตัวหน้าสุด = 2
            listAns.append(a) #เก็บคำตอบใส่ใน listAns : 84/2 = 42
            listPrimeFactor.append(Devided_Prime[i]) #เก็บตัวหาร i =[0] --> ก็เป็น2
            #ถ้ากรณี Devide_Prime[0] ใช้หารไม่ได้ เราก็เลื่อนให้มันเป็น Devided_Prime[1] มาหารแทน
            if(a%Devided_Prime[i] !=0): #คือถ้ามันหาร a แล้วเศษไม่เป็น 0 หรือหารไม่ลงตัว ให้ทำ...
                i += 1 #ให้ i + 1 ก็คือจาก {2,3,7} จากตัวแรกคือ 2 มาใช้ตัวถัดไปคือ 3 แทน


        #Step 3 เช็คคำตอบ
        print("Answer จากการหารได้แก่ ",listAns)
        print("PrimeFactor ที่เราต้องการได้แก่",listPrimeFactor)

        #Step 4 ทีนี้ก็เก็บรายละเอียด "*".joint(listPrimeFactor)
        print("คำตอบสุดท้ายด้านล่าง")
        print("*".join(str(x) for x in listPrimeFactor))
        #เนื่องจาก  listPrimeFactor = {2,2,3,7} มันเป็นค่า int
        #การจะใช้ join "*" ต้องแปลงตัวใน list เป็น String ให้หมดก่อน
        #(str(x) for x in listPrimeFactor) ทำให้ {2,2,3,7} เป็น String

    

        
a = input("กรุณาใส่จำนวณที่ต้องหา PrimeFactor : ")
primeFactor(a) #สุดท้ายก็ทดสอบ
