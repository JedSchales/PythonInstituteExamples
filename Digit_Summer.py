birthDate = 0
stringIter = ''
tempSum = 0
digitOfLife = 0

while birthDate == 0:
    try:
        birthDate = int(input("Please enter your birthdate (YYYMMDD, YYYDDMM, or MMDDYYYY): "))
        if len(str(birthDate)) == 8:
            stringIter = str(birthDate)
    except:
        print("The date provided contained non-numeric characters.  Please try again.")
    
for num in stringIter:
    tempSum += int(num)
digitOfLife = tempSum

while digitOfLife > 9:
    stringIter = str(digitOfLife)
    tempSum = 0
    for num in stringIter:
        tempSum += int(num)
    digitOfLife = tempSum

print(digitOfLife)