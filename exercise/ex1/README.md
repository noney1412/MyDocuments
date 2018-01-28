##exercise

Command Line Argument 2 ข้อความ โดยข้อความที่ 1 มีค่าเป็น vowel / alphabet (ไม่นับตัวที่เป็นสระ) / digit / lowercase / uppercase อย่างใดอย่างหนึ่ง ข้อความที่ 2 เป็น alphanumeric และแสดงจำนวนตัวอักษร ในข้อความที่ 2 ตามที่ข้อความที่ 1 กำหนด ทาง Standard Output

****
##How to (***using python***)
****



opt = vowel / alphabet / digit / lowercase / uppercase
args = alphanumeric

***alphanumeric characters**
ตัวอักขระทั้งหมดที่เป็นได้ทั้งตัวอักษร (a, b, c,…) ตัวเลข (1, 2, 3,...) สัญลักษณ์พิเศษ ช่องว่าง และเครื่องหมายวรรคตอนต่าง ๆ ( #, 4,…)

```mermaid

graph LR;
    A(Run: while !Bug)-->|input : opt,args|B1(args=Rawitat)
    B1 --> O1(vowel=3)
    B1 --> O2(alphabet=4)
    B1 --> O3(digit=0)
    B1 --> O4(lowercase=6)
    B1 --> O5(uppercase=1)
    A-->|Error|E(restart)  

```
![cover](ex1-mermaid.png)

