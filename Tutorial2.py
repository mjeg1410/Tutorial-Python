number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))
print(number1)
print(number2)
print(round_number)
number3 = float(input("Enter first number: "))
number4 = float(input("Enter second number: "))
if number3 > number4:
    number3bigger= True
else:
    number3bigger= False
print("number3bigger","=",number3bigger)