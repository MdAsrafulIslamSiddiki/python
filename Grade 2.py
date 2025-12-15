print("-------------Grade Calculator--------------")
print("Enter your marks:")
bangla=int(input("Enter your marks in Bangla: "))
english=int(input("Enter your marks in English: "))
math=int(input("Enter your marks in Mathematics: "))
physics=int(input("Enter your marks in Physics: "))
chemistry=int(input("Enter your marks in Chemistry: "))

bangla_gp=0
english_gp=0
math_gp=0
physics_gp=0
chemistry_gp=0

if(bangla_gp>=96 and bangla_gp<=100):
    bangla_gp=5.00
elif(bangla_gp>=90 and bangla_gp<=95):
    bangla_gp=4.00
elif(bangla_gp>=80 and bangla_gp<=89):
    bangla_gp=3.00
elif(bangla_gp>=70 and bangla_gp<=79):
    bangla_gp=3.50
elif(bangla_gp>=60 and bangla_gp<=69):
    bangla_gp=2.00   
elif(bangla_gp>=50 and bangla_gp<=59):
    bangla_gp=1.00
else:
    bangla_gp=0.00


if(english_gp>=96 and english_gp<=100):
    english_gp=5.00
elif(english_gp>=90 and english_gp<=95):
    english_gp=4.00
elif(english_gp>=80 and english_gp<=89):
    english_gp=3.00
elif(bangla_gp>=70 and bangla_gp<=79):
    bangla_gp=3.50
elif(english_gp>=60 and english_gp<=69):
    english_gp=2.00   
elif(english_gp>=50 and english_gp<=59):
    english_gp=1.00
else:
    english_gp=0.00



if(math_gp>=96 and math_gp<=100):
    math_gp=5.00
elif(math_gp>=90 and math_gp<=95):
    math_gp=4.00
elif(math_gp>=80 and math_gp<=89):
    math_gp=3.00
elif(math_gp>=70 and math_gp<=79):
    math_gp=3.50
elif(math_gp>=60 and math_gp<=69):
    math_gp=2.00   
elif(math_gp>=50 and math_gp<=59):
    math_gp=1.00
else:
    math_gp=0.00
    


if(physics_gp>=96 and physics_gp<=100):
    physics_gp=5.00
elif(physics_gp>=90 and physics_gp<=95):
    physics_gp=4.00
elif(physics_gp>=80 and physics_gp<=89):
    physics_gp=3.00
elif(physics_gp>=70 and physics_gp<=79):
    physics_gp=3.50
elif(physics_gp>=60 and physics_gp<=69):
    physics_gp=2.00   
elif(physics_gp>=50 and physics_gp<=59):
    physics_gp=1.00
else:
    physics_gp=0.00



if(chemistry_gp>=96 and chemistry_gp<=100):
    chemistry_gp=5.00
elif(chemistry_gp>=90 and chemistry_gp<=95):
    chemistry_gp=4.00
elif(chemistry_gp>=80 and chemistry_gp<=89):
    chemistry_gp=3.00
elif(chemistry_gp>=70 and chemistry_gp<=79):
    chemistry_gp=3.50
elif(chemistry_gp>=60 and chemistry_gp<=69):
    chemistry_gp=2.00   
elif(chemistry_gp>=50 and chemistry_gp<=59):
    chemistry_gp=1.00
else:
    chemistry_gp=0.00
    
#For total GP

print("Your grade points in subjects....")
print("Bangla=",bangla_gp)
print("English=",english_gp)
print("Math=",math_gp)
print("Physics=",physics_gp)
print("Chemistry=",chemistry_gp)

#finding GPA
if bangla_gp>0 and english_gp>0 and math_gp>0 and physics_gp>0 and chemistry_gp>0:
    GPA=(bangla_gp + english_gp + math_gp + physics_gp + chemistry_gp)/5
else:
    GPA=0.00
    
#finding Grade
    
Grade=""

if GPA>0:
    if(GPA==5.00):
        Grade="A+"
    elif(GPA>=4.00 and GPA<5.00):
        Grade="A"
    elif(GPA>=3.50 and GPA<4.00):
        Grade="A-"
    elif(GPA>=3.00 and GPA<3.50):
        Grade="B"
    elif(GPA>=2.00 and GPA<3.00):
        Grade="C"
    elif(GPA>=1.00 and GPA<2.00):
        Grade="D"
else:
    Grade="F"

print("Final result\n")

print("Your GPA=",GPA,"and Grade=",Grade)