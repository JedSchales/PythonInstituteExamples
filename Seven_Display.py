def LEDify(integer):
    LEDList = []                                        #Create empty LEDList
    LEDList.append(["###","# #","# #","# #","###",])    #Construct 0
    LEDList.append(["  #","  #","  #","  #","  #",])    #Construct 1
    LEDList.append(["###","  #","###","#  ","###",])    #Construct 2
    LEDList.append(["###","  #","###","  #","###",])    #Construct 3
    LEDList.append(["# #","# #","###","  #","  #",])    #Construct 4
    LEDList.append(["###","#  ","###","  #","###",])    #Construct 5
    LEDList.append(["###","#  ","###","# #","###",])    #Construct 6
    LEDList.append(["###","  #","  #","  #","  #",])    #Construct 7
    LEDList.append(["###","# #","###","# #","###",])    #Construct 8
    LEDList.append(["###","# #","###","  #","###",])    #Construct 9
    
    LEDText = str(integer)                              #Convert integer to string
    for i in range(5):                                  #Loop 5 times for height of ASCII art
        for char in LEDText:
            print(LEDList[int(char)][i],end=" ")        #Look up number in indexed list and return respective row of art
        print()                                         #Prepare new line of art

LEDify(123)
LEDify(9081726354)
