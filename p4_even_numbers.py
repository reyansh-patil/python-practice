#https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz_1/quiz.php
#Write the code to print out all the even numbers up to 100.

print("Even numbers from 1-100 are as follows:") #This displays the text in double quotes ("")

for i in range(1,101): #this will make it run 100 times. 
    if i%2 == 0: #this line is checking if it has any remainders, '%' takes the remainder if there is none 0 is outputted
        print (i)#if there is no remainder (which would mean it is a multiple of 2) it prints the number
#TIP: the for loop is set too 101 since it will run 1 less than the max amount give due to the pirst number being counted when running