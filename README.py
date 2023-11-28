# BMICalcualtor
#BMI calculator with advice
#input
a=int(input("น้ำหนัก kg :"))

b=int(input("ส่วนสูง cm :"))/100
#function BMI formular  BMI=weight/m2
c=a/b**2
c="{:.2f}".format(c)
print("ค่า BMI :",c)
#comparison
if float(c)<=18.50:
    print("ผลลัพธิ์ที่ได้ :"+""+"ผอมมาก")
    print("คำแนะนำเบื้องต้น กินให้เยอะๆ")

if float(c)>=18.50 and float(c)<=22.90:
    print("ผลลัพธิ์ที่ได้ :"+""+"สุขภาพดี")

if float(c)>=22.90 and float(c)<=24.90:
     print("ผลลัพธิ์ที่ได้ :"+""+"ท้วม")

if float(c)>=24.90 and float(c)<=29.90:
   print("ผลลัพธิ์ที่ได้ :"+""+"อ้วน")

if float(c)>=30.0:
    print("ผลลัพธิ์ที่ได้ :"+""+"อ้วนมาก")
