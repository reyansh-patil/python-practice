# https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz15/quiz.php
# A coach hire firm charges £10 per person per mile for the first 100 miles, and an extra £2 per mile per person after that. 
# However if there are fewer than twenty people, an additional charge of £5 per person is included.
# Ask for journey miles and the number of people and display the total cost, in a neat format.

total_cost=0
miles=int(input("Enter the miles traveled: "))
ppl=int(input("Enter the amount of people present: "))

mcp1=miles*10 # Base rate 10

mcp2=0 # Above 100miles
pc=0 # People cost

if miles>100:
    mcp2=(miles-100)*2 # if >100 m
else:
    print("Extra cost not applicable")

if ppl<20:
    pc=ppl*5 #if less than 20 people
else:
    print("No extra cost applicable for the people count")

total_cost = mcp1 + mcp2 + pc
print("Total Cost: " + total_cost)