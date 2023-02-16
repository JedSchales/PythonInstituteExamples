def mysplit(text):
    list = []
    text = text.strip()                 #Strips away excess whitespace
    while len(text) > 0:                #Handles empty/whitespace-exclusive strings
        nextDelim = text.find(chr(32))  #Finds first space
        if nextDelim == -1:             #Handles no more spaces in string
            list.append(text[0:])       #Appends final word into the list
            return list
        list.append(text[0:nextDelim])  #Appends a word into the list
        text = text[nextDelim+1:]       #Strips off appended word to prepare for next loop
    return list


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

#Expected behavior

#['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
#['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
#[]
#['abc']
#[]
