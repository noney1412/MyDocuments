from collections import Counter

option_list = ["vowel", "alphabet", "digit", "lowercase", "uppercase"]


class ifError(object):
    bug_count = 3


print(" ")
print(" วิธีการใช้งาน ")
print("-  count [vowel, alphabet, digit, lowercase, uppercase], alphanumeric")
print("-  หรือคุณสามารถพิมพ์ 0 0 เพื่อออกจากโปรแกรมค่ะ")
print(" ")

while (ifError.bug_count >= 0):

    def handle_error():
        print("error")
        print("---- Error_Detected: ข้อความที่ 1 ไม่ถูกต้อง ----")
        print("!! _inputError : ข้อความที่ 1 จะต้องมีค่าเป็น vowel / alphabet (ไม่นับตัวที่เป็นสระ) / digit / lowercase / uppercase ")
        print("!! _inputError : ตัวอย่างเช่น --> count vowel Rawitat ")
        print(" ")
        print("กรุณาใส่ข้อความให้ถูกต้อง คุณมีโอกาศ", ifError.bug_count, "ครั้ง")
        print(" ")

    try:
        opt, args = input("count ").split()

    except ValueError:
        print(" ")
        print("กรุณาใส่ข้อความให้ถูกต้องค่ะ โปรดลองใหม่อีกครั้ง... ")
        print("ตัวอย่าง : count vowel Rawitat")
        print(" ")

    if opt in option_list:

        if args.isalpha():
            class checkVowel(object):
                vowels = set("aeiou")

            if opt == "vowel":
                counter = Counter(v for v in args.lower() if v in checkVowel.vowels)
                print(sum(counter.values()))

            elif opt == "alphabet":
                counter = Counter(v for v in args.lower() if v not in checkVowel.vowels)
                print(sum(counter.values()))
            
            elif opt == "lowercase":
                counter = Counter(v for v in args if v.islower())
                print(sum(counter.values()))

            elif opt == "uppercase":
                counter = Counter(v for v in args if v.isupper())
                print(sum(counter.values()))
            
            else:
                handle_error()
                ifError.bug_count -= 1

        elif opt == "digit":
                counter = Counter(v for v in args if v in set("0123456789"))
                print(sum(counter.values()))
        
        else:
            print("---- _Warning !! ----")
            print("ข้อความชุดนี้มีตัวเลขประกอบอยู่ข้างใน กรุณาใช้ digit เป็นข้อความ option ที่ 1 เพื่อลดข้อผิดพลาด")
            print("ตัวอย่างเช่น : count digit eiei5558989898")
            print(" ")

    elif opt == "0" and args == "0":
        break

    else:
        handle_error()
        ifError.bug_count -= 1
