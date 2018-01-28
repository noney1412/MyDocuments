bug_count = 3
option_list = ["vowel", "alphabet", "digit", "lowercase", "uppercase"]
optl = []

while (bug_count >= 0):

    try:
        opt,args = input("count ").split()
    except ValueError:
        print("กรุณาใส่ข้อความอีกครั้งค่ะ. ")
    
    if opt in option_list:
        optl.append(opt)
        print(optl)
    
    else:
        print("---- Error_Detected ----")
        print("!! _inputError : ข้อความที่ 1 จะต้องมีค่าเป็น vowel / alphabet (ไม่นับตัวที่เป็นสระ) / digit / lowercase / uppercase ")
        print("!! _inputError : ตัวอย่างเช่น --> count vowel Rawitat ")
        print("กรุณาใส่ข้อความให้ถูกต้อง คุณมีโอกาศ",bug_count,"ครั้ง")
        print(" ")
        bug_count -= 1


# print(x,y)
