#https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz_1/quiz.php
#Write the code to print out all the even numbers up to 100.

print("Even numbers from 1-100 are as follows:") 

for i in range(1,101): # This will make it run  100 times. For loop will exit at 101st time.
    if i%2 == 0: #this line is checking if it has any remainders, '%' operator gives the remainder if there is none 0 is outputted
        print (i) #if there is zero remainder (which would mean it is a multiple of 2 and an even number) it prints the number as is even
#TIP: the for loop is set too 101 since it will run 1 less than the max count given