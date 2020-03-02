file = open("teams.txt","w")
teams =["MU","MC","WG","SA","DD"]
for i in range (5):
    
    file.write(teams[i])
    file.write("\n")
file = open("teams.txt", "r")
for i in range (5):
    if i == 0 or i == 2:

        print(file.readline())
    file.readline()
file.close()