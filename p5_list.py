#https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz_1/quiz.php
#An array holds months of the year (0 is Jan, 1 is Feb etc). The user enters the month number. If it is a valid month number, then the name of the month is displayed. If it is not valid, then a message is displayed.

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] #this is a list 
#it is very similiar to your average shopping list it can store data but unlike variables it can store multiple data points

monthnum = int(input("Enter the desired month number: "))#this asks number for month eg January == 1

if (monthnum >= 1) and (monthnum <=12): #this checks if it is a actual month number
    print(str(monthnum) + " is " + month[monthnum-1]) # Array index starts from 0 so substract 1 from monthnum to match the list index
else:
    print("Please enter a valid month number between 1-12")#this is the error message
