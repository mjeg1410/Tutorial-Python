
maths_mark = int(input("Please enter your maths mark:"))
chemistry_mark =int(input("Please enter your chemistry mark:"))
physics_mark = int(input("Please enter your physics mark:"))
percentage = float((maths_mark + chemistry_mark + physics_mark)/3)
print ("Welcome to Grade Calculator")
print ("You scored a percentage of: ", percentage)
if maths_mark < 40 or chemistry_mark < 40 or physics_mark < 40:
    print("You failed")
elif percentage >= 70:
    print("Grade: A")
elif(percentage >=60):
    print("Grade: B")
elif(percentage >=50):
    print ("Grade: C")
elif(percentage >=40):
     print ("Grade: D")
else:
    print ("You failed.")