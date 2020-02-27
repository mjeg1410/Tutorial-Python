num = input("Please enter the first 12 numbers of your ISBN: ")
if len(num) != 12:
    num = input("Please enter exactly the first 12 numbers of your ISBN: ")
res = list(map(int, str(num))) 
print (res)
total = 0
for x in res:
    if ((res.index(x)+1) % 2) >0:
        total = (total + x)
    else:
        total = total +(x*3)
print (total)
total = total%10
print (total)
total = (10-total)
print (str(num) + str(total))