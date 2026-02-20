#https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz_1/quiz.php
#Ask the user to enter their first name and surname(s). The result should be combined into a full name and displayed along with a suitable message.
fn = input("Please enter your first name: ")#this takes in an input (a question)
sn = input("Please enter your surname: ")

print("Hello " + fn.capitalize() + " " + sn.capitalize() + ", hope you have a good day") #this will put the two names together eg, first name = john second name = johnson,that would equal to 'john johnson'.
