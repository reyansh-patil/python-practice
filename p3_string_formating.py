#https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz_1/quiz.php
#Ask the user to enter their first name and surname(s). The result should be combined into a full name and displayed along with a suitable message.
fn = input("Please enter your first name: ") 
sn = input("Please enter your surname: ")

# Concatenate firstname and lastname together eg, firstname = john, secondname = johnson, that would equal to 'john johnson'.
print("Hello " + fn.capitalize() + " " + sn.capitalize() + ", hope you have a good day") 
