count1 = 0
count2 = 0
names = []
while count1 <5:
    name = input("Please enter a name:")
    names.append(name)
    count1 +=1
while count2 <5:
    print (names[count2]  + " is awesome")
    count2 +=1
for i in range (10,21,2):
    print(i)