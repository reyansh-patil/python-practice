#https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz_1/quiz.php
#Write the pseudocode to ask a user to guess your favourite animal until they get it right (your favourite animal is tiger). Limit entry to five attempts.

target = "tiger" # Sets the target value to be guessed
guessed = False 
for i in range(0, 5): 
    guess = input("Guess my favourite animal!: Attempt " + str(i+1) + "/5 : ") #i+1 is needed due to the forloop starting at 0.
    if guess == target:
        print("YOU GOT IT!")
        guessed = True # This flag is used later to decide whether to print message about guess failed
        break #break stops the program
    else:
        print("Guess is incorrect")

if guessed == False:
    print("Sorry, you have exceeded maximum 5 attempts. Better luck next time.")
