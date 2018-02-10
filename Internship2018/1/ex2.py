## by Chanon Panpila FB: Chanon Panpila Github : Noney1412

from collections import Counter

print(" ")
print(" วิธีการใช้งาน formatter [ digit ] [ pattern ]")
print("-  formatter [ 0912345678 ] [ xxx-xxx-xxxx , 111x111x1111 ]")
print("-  091-234-5678 , 091x234x5678 ")
print("   ทำ Error_Handling ไว้แล้วฮะ ลองใส่  ---xxx-xxx-&&&&H&&&&H& มั่วๆ ได้ตามสบายครับ อิอิ")
print("-  หรือคุณสามารถพิมพ์ x1 x1 เพื่อออกจากโปรแกรมค่ะ")
print(" ")


class ifError(object):
    bug_count = 3

class format_ptrn(object):
    val = set("x1")
    index = 0
    result = []

def handle_error(case):

    if case == RuntimeError:
        print("error")
        print("---- Error_Detected: ข้อความที่ 1 ไม่ถูกต้อง ----")
        print("!! _inputError : ข้อความที่ 1 จะต้องมีค่าเป็นตัวเลขใด ๆ ")
        print("!! _inputError : ตัวอย่างเช่น --> formatter 123456 xxx-xxx ")
        print(" ")
        print("กรุณาใส่ข้อความให้ถูกต้อง คุณมีโอกาศ", ifError.bug_count, "ครั้ง หรือพิมพ์ x1 x1 เพื่อออกจากโปรแกรมค่ะ")
        print(" ")

    elif case == RuntimeWarning:
        print("---- _Warning !! ----")
        print("ข้อความชุดที่สอง กรุณาใช้ Pattern ทีใช้ในการ format ให้ถูกต้อง เช่น xxx-xxx-xxx , 111-111-111")
        print("ตัวอย่างเช่น : count 555555 xxx-xxx")
        print(" 555-555 ")
        print(" ")

    elif case == ValueError:
        print(" ")
        print("กรุณาใส่ข้อความให้ถูกต้องค่ะ โปรดลองใหม่อีกครั้ง... ")
        print("ตัวอย่าง : formatter 0912345678 xxx-xxx-xxxx")
        print(" 091-234-5678 ")
        print(" ")
    
while (ifError.bug_count >= 0):

    try:
        args, ptrn = input("formatter ").split()
        list_args = list(args)
        list_result = list(ptrn)
    
    except ValueError:
        handle_error(ValueError)
        continue
    
    if args.isdigit():
        if [v for v in ptrn if v in format_ptrn.val] :

            count_args = len(args)
            count_ptrn = Counter(v for v in ptrn if v in format_ptrn.val)
            count_ptrn_most = count_ptrn.most_common(1)[0]
        
            if count_args == count_ptrn_most[1] :
                for i,element in enumerate(list_result) :
                    if element == count_ptrn_most[0] :
                        list_result[i] = list_args[format_ptrn.index]
                        format_ptrn.index += 1
                    else:
                        pass
                
                print(''.join(list_result))
                print(" ")

                format_ptrn.index = 0 #clear_index b/c using while-loop

            else:
                if count_ptrn_most[1] > count_args :
                    value = count_ptrn_most[1] - count_args   
                    print("ตัวเลขขาดอยู่",value,"ตัว กรุณาใส่ตัวเลขให้ตรงตามจำนวนแม่แบบ")  
                    print(" ")
                
                else:
                    value = count_args - count_ptrn_most[1] 
                    print("รูปแบบ Formatter ขาดอยู่",value,"ตัว กรุณาเติมจำนวนแม่แบบ '",count_ptrn_most[0],"'ให้ครบ")
                    print(" ")

        else:
            handle_error(RuntimeWarning)

    elif args == "x1" and ptrn == "x1":
        break

    else:
        handle_error(RuntimeError)
        ifError.bug_count -= 1

