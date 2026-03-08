#https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz13/quiz.php
#Create an array of numbers 1 to 11, in that order. Array[0] holds number 1. Create an algorithm to reverse the order so that 11 is now in array[0] and one is in array[10].
#Use iteration to do this.

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] 
ln= int(len(n)) #this checks the length
print ("Length = " + str(ln) + " " + str(ln//2)) # Actual lenth is 12 but we need to traverse till half to swap
for i in range (0, (ln//2)): # It will run 6 since it will swap 2 numbers each time it is run
    print ("Iteration i=" + str(i))
    temp = n[i] # This temporarily stores the number
    n[i] = n[ln-1-i] 
    n[ln-1-i] = temp
print(n)