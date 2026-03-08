https://www.teach-ict.com/v/revision/pseudocode_ocr/quiz11/quiz.php
#Write an algorithm to: Enter the radius of a circle. Work out its area. Enter the length of a square. Work out its area. 
#Identify the shape with the larger area and what it is

r = int(input("Enter the radius of your circle: "))
circ_area = 3.14*r*r # Calculate the area of the circle using this formula pi*r*r
print("Circle Area: " + circ_area)

square_side = int(input("Enter one side of you square: "))
square_area = square_side*square_side # This works out the area of the square
print("Square Area: " + square_area)
print("")
if square_area < circ_area: #now we will compare them and output the bigger integer
    print("Circle area " + str(circ_area) + " is bigger than Sqaure")
elif square_area > circ_area:
    print("Sqauare area " + str(square_area) + " is bigger than Circle")
else # square_area == circ_area:
    print("Circle and Square area is exactly same")
