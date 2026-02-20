#https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz_1/quiz.php
#Ask the user to input a student grade. If the grade is 70 or above then display, you have passed. Otherwise, it will display, sorry, you have not passed

grade=int(input("Enter your student grade: ")) # Ask user to input the grade and convert to int

if grade>=70: #Now check if they did pass ( above or equal to 70) which will display "You have passed!"
    print("You have passed!")
elif grade<70: #This line checks if it less than 70 then it's a fail
    print("Sorry, you have not passed")
else: #This will display invalid input if the input is not a number
    print("Invalid grade input")

