#https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz_1/quiz.php
#Ask the user to input a student grade. If the grade is 70 or above then display, you have passed. Otherwise, it will display, sorry, you have not passed

grade=int(input("Enter your student grade: ")) #This asks the user what grade they got
# the int() on line 4 tell the computer than the input is going to be a number
if grade<70: #This line checks if it less than 70 if it is the code will display "Sorry you have not passed"
    print("Sorry, you have not passed")
elif grade>=70: #Now this check if they did pass ( above or equal to 70) which will display "You have passed!"
    print("You have passed!")
else: #This will display invalid input if the input is not a number
    print("Invalid grade input")
