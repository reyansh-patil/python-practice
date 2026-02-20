#https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz_1/quiz.php
#Ask a user to input two integers and then cast them into the integer data type. The program should output the smallest number . If the numbers are equal, then it will inform the user.
a=int(input("Enter you first desired number: "))# This takes in an input 
b=int(input("Enter you second desired number: "))# This takes in an input

if a<b:# line 6 to 13: this compares the numbers and gives output accordingly
    print(str(a) + "is smaller")
elif b<a:
    print(b)
elif a == b:
    print("They are both equal")
else:
    print("Please make sure your inputs are numbers") 