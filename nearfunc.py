def near(firstString,lastString):
    for char in firstString:
        
        compare = firstString.replace(char,"")
        print (compare)
        print (lastString)
        if compare == lastString:
            print ("true")
            print (compare)
        else:
            print ("false")
near("rests","rest")