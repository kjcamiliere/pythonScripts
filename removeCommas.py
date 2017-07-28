# Jessica Camiliere
# Used to turn commas into spaces
alive = 1
while alive == 1:
    print ("==============================================================")
    print ("  Right Mouse Button copies and pastes text from this window  ")
    print ("==============================================================")

    newString = ''
    x = 0
    i = 0

    unformattedList = input ("Paste Text: \n")


    alist = unformattedList.split(",")

    listSize = len(alist)

    while listSize > i :
        alist[i] = alist[i].strip()
        i = i + 1

    while listSize > x :
        
        newString += alist[x]
        newString += ' '
        
        x = x + 1 
    print ('\n')
    print (newString)
    print ('\n')
    

