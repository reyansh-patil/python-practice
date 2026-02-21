#https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz_1/quiz.php
#Two subroutines Prepare_to_go_home() and Prepare_for_next_lesson() are used to describe your actions in school.
#They include the test condition EndOfSchool.
#In one situation, the prepare_to_go_home() subroutine is called, otherwise the prepare_for_next_lesson() is called.

def prepare_to_go_home(): # This is a function it stores blocks of code
    print("Get your bag ready to go home")

def prepare_for_next_lesson(): 
    print("Get your books ready for next lesson")

q = input("Is it time to go home? (give you answer as y/n): ")
if q.lower() == "y": # The 'lower()' library function makes the input lowercase
    prepare_to_go_home() # This calls the function defined above
elif q.lower() == "n":
    prepare_for_next_lesson() 
else:
    print("Please make sure you give an acceptable answer (y or n): ")
    
