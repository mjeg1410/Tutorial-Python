def input_function():
    firstString = str(input("Enter the word you wish to remove a character from: "))
    lastString = str(input("Enter the word you are comparing to: "))
    return firstString,lastString
def near():
    firstString,lastString = input_function()
    first = list(firstString)
    last = list(lastString)
    
    for i in range(len(first)):
        item = first[i]
        del first[i]
        print (str(first))
        if first == last:
            print("True")
        else:
            first.insert(i,item)
            print ("False")
            
near()