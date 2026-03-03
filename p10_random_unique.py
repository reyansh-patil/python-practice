#https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz_1/quiz.php

#Assume there is a subroutine available that returns an unique (no repeats) random integer, given an upper and lower limit, Random(low_number, high_number).
#Use this to produce a six number lottery ticket, in the range 1 to 49. Store the numbers in an array. Use a FOR loop to load each number.
#Then display with a WHILE loop.
import random # This lets us use a function to generate a random number

lottery_list = [] # Numbers will be stored here to check for repeats and to print

def get_unique_random_number():
    r = random.randint(1, 49) # This generates a random number from 1 - 49
    while r in lottery_list: # regenerate random number if its repeat number
         print ("Repeat number ignored: " + str(r))
         r = random.randint(1, 49) 
    return r

     
for i in range(0, 6): # Generate six lottery numbers
    lottery_list.append(get_unique_random_number())

# Display random numbers using WHILE loop as asked in this question
idx = 0
len = len(lottery_list)
print ("Your lucky numbers are: ")
while idx < len:
    print(str(lottery_list[idx]))
    idx += 1

print ("lottery_list: " + str(lottery_list))