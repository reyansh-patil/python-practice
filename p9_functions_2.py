#https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz_1/quiz.php
#Three subroutines Prepare_to_go_home() and Prepare_for_next_lesson() and Visit_Cafeteria() are used to describe your actions in school with the test conditions EndOfSchool and Lunchtime.
#In one situation, the prepare_to_go_home() subroutine is called, otherwise the prepare_for_next_lesson() or the Visit_Cafteria() is called.
#Set out the pseudocode for this.

#this code is a continuation to p8

def prepare_to_go_home():
    print("Get your bag ready to go home")

def prepare_for_next_lesson():
    print("Get your books ready for next lesson")

def visit_cafeteria(): # Here we have added a new function
    print("Visit the cafeteria for lunch")

q = input("Is it the end of school time? (give you answer as y/n): ")
if q.lower() == "y":
    prepare_to_go_home()
elif q.lower() == "n":
    lt = input("Is it lunchtime? (give your answer as y or n): ")
    if lt == "n":
        prepare_for_next_lesson()
    elif lt == "y":
        visit_cafeteria() #here is where thenew function is called
    else:
        print("Please make sure you give an acceptable answer (y or n): ")
else:
    print("Please make sure you give an acceptable answer (y or n): ")
