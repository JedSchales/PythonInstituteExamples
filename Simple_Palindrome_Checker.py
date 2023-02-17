string = input("Please provide a potential palindrome: ")
filteredString = ''

for ltr in string:
    if (ord(ltr) >= 97 and ord(ltr) <= 122) or (ord(ltr) >= 65 and ord(ltr) <= 90):
        filteredString += ltr
    else:
        continue

STRING = filteredString.upper()
GNIRTS = STRING[-1::-1]

if STRING == GNIRTS:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
