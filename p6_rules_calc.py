#https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz_1/quiz.php
#You have found a summer job in a local farm picking apples. You are paid in two ways, by weight and by time. You are paid either £1.50 for every kilogram picked or £9.50 for every hour worked whichever is the higher earnings. Enter the weight and hours worked along with a calculation for each wage. Display both earnings and declare the actual earnings.
hoursworked = int(input("Enter the number of hours you have worked: "))
weigh_collected = int(input("Enter the total weight of the apples you picked up: "))

hoursworked_cost = hoursworked*9.50 # This calculates the price from hours worked and puts it into the variable hoursworked_cost

print(hoursworked_cost)

weigh_collected_cost = weigh_collected*1.50 # This calculates the price for apples collected

print(weigh_collected_cost)


# This will check which is bigger and which one to output
if weigh_collected_cost < hoursworked_cost: 
    print("You have earned £" + str(hoursworked_cost))
elif hoursworked < weigh_collected:
    print("You have earned £" + str(weigh_collected_cost))