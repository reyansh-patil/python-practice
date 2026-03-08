# https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz14/quiz.php
# A pager device can display a message of up to 30 characters. Allow the user to input a message of up to 30 characters. Truncate the message if more than 30 characters. 
# Pad it out with spaces if less than 30 characters

# In this code I have used stars to make it more visible how much has been added
q = input("Enter your message (please make sure it is less or 30 charecters long): ")
ln = len(q)
print(ln)
if ln > 30:
    print("You have exceeded the maximum charecter limit 30. So no formatting changes.")
elif ln == 30:
    print("You have entered the message with 30 charecters. So no formatting changes.")
else:
    stars = 30-ln # This works out how many starts we need to suffix
    suffix = ""
    for i in range(0, stars):
        suffix = suffix + "*"
    print("Suffixed Message: " + q + suffix)