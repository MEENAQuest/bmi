def BMI(name,weight,height):
    bmi=weight/(height*height)
    print(name," your bmi is ",bmi)
    return bmi

name=input("Enter Your Name: ")
weight=float(input("Enter Your Weight (kg): "))
height=float(input("Enter Your Height (m): "))
bmi=BMI(name,weight,height)

if bmi<=18.4:
    print("Under weight")
if bmi>18.4 and bmi<=24.9:
    print("Normal weight")
if bmi>24.9 and bmi<=29.9:
    print("Over weight")
if bmi>29.9 and bmi<=34.9:
    print("Obese")
if bmi>34.9:
    print("Highly Obese")                