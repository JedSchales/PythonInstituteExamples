# This program will convert a decimal number into binary and display the corresponding letter.
# The program needs error handling for numbers provided that aren't between 1 and 26.

import math

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
binary_array = [0,0,0,0,0]

while True:
    dec_num = int(input("Which number do you want to convert into a binary letter?"))
    next_num = dec_num
    counter = math.floor(dec_num ** 0.5)+1 # This line creates a counter based on how many times you are going to perform division.
    for i in range(counter):
        next_digit = next_num % 2       # This line determines the remainder of division, or the binary digit provided to the binary_array for this iteration.
        next_num = next_num // 2        # This line determines the dividend for the next iteration.
        binary_array[4-i] = next_digit  # This line stores the binary digit determined two lines previously.

    binary_string = str(binary_array[0])+str(binary_array[1])+str(binary_array[2])+str(binary_array[3])+str(binary_array[4])  #This line re-interprets the array as a single 5-digit string.
    print(binary_string,alphabet[dec_num-1])    # Arrays are 0-indexed, so we have to say "alphabet[dec_num-1]" since the first item of this list would be "element 0".
    pass
