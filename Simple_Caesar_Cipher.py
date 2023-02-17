unencrypted_text = input("Please provide a message to be encrypted: ")
caesar_shift = 0

while caesar_shift < 1 or caesar_shift > 25:
    try:
        caesar_shift = int(input("Provide the shift value (between 0 and 26) to use for the cipher: "))
        if caesar_shift < 1:
            print("The shift value provided is too low.  Please try again.")
        elif caesar_shift > 25:
            print("The shift value provided is too high.  Please try again.")
    except:
        print("An invalid amount was provided for the shift value.  Please try again.")

encrypted_text = ''

for ltr in unencrypted_text:
    if ord(ltr) >= 97 and ord(ltr) <= 122:  #Lowercase determination
        if ord(ltr) + caesar_shift > 122:   #Handle wrap-around of lowercase alphabet
            ltr = chr(97 + (ord(ltr) + caesar_shift - 123))
        else:
            ltr = chr(ord(ltr) + caesar_shift)
    elif ord(ltr) >= 65 and ord(ltr) <= 90: #Uppercase determination
        if ord(ltr) + caesar_shift > 90:    #Handle wrap-around of uppercase alphabet
            ltr = chr(65 + (ord(ltr) + caesar_shift - 91))
        else:
            ltr = chr(ord(ltr) + caesar_shift)
    else:                                   #Pass non-alphabetic characters as is
        pass
    encrypted_text += ltr

print(encrypted_text)
