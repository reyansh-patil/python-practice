#https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz12/quiz.php
#Your passport is in a locked hotel room safe with an LED display, initially displaying ‘Enter Code’. You have to enter the correct 4 digit code.
#You can only make three attempts whereby the safe resets itself to a default number. The correct code is 3423 and the default code is 9999.
#Assume a subroutine pressed_button() returns the pressed button number, open_safe() opens the safe and LED_Display(text) controls the display.
guessed = False
password = 3423 #this is the begginning set password


def pressed_button():
    return int(input("Please enter the code: "))

def open_safe():
    print("You have been granted access!!")

def LED_Display(text):
    print (text)


LED_Display("Enter Code")
attempts = 3
i = 1
while i <= attempts: #this is a while loop it never stops until the condition is met
    q = pressed_button()
    if q == password:
        print("You have accessed the safe")
        guessed = True
        break
    else:
        print("This is the wrong code")
    i = i+1 #this is to count the amount of attempts
    LED_Display("Enter Code")

if (i>3):
    print ("You have exceeded maximum 3 attempts. Password is now reset")
    password = 9999 # This now changes it to the default password

