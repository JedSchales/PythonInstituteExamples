def nonAlphaStripper(text):
    processedText = ''
    for ltr in text:
        if (ord(ltr) >= 97 and ord(ltr) <= 122) or (ord(ltr) >= 65 and ord(ltr) <= 90):
            processedText += ltr
        else:
            continue
    return processedText.upper()

def Listify(string):
    list = []
    for ltr in string:
        list.append(ltr)
    list.sort()
    return list

string1 = nonAlphaStripper(input("Please provide your first word: "))
string2 = nonAlphaStripper(input("Please provide a potential anagram: "))

list1 = Listify(string1)
list2 = Listify(string2)

if list1 == list2:
    print("Anagrams")
else:
    print("Not anagrams")
