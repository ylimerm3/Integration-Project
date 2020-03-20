# Emiy Martin, Florida Gulf Coast University, COP-1500 Integration Project   #
##############################################################################
# Description: this program takes RGB values from 3 trials                   #
# of the same grapheme and calculates if there is                            #
# synesthetic association or not                                             #
##############################################################################
# Special thanks to those who constructed the original                       #
# Synesthesia Battery (Dr. Eagleman & colleagues, 2007), which this          #
# program models.                                                            #
# Also special thanks to w3schools.com for python tutorials of code          #
# that I used in this program, and Prof. Vanselow (and TA's) for instruction #
##############################################################################

# Greeting
print("Hello! This program will evaluate whether or not you have \na synesthetic association for a grapheme.")

# These next 4 sections are bonus to satisfy the class requirements

# String operator
print("(This next line is to satisfy a class requirement)")
a = "This program is useful for my research! "
b = "Hopefully Dr. DiMattina agrees."
c = a + b
print(c)

# Shortcut operator
num_1 = 7
num_1 += 8
# print(num_1)

# For loop
for x in range (1):
    print("Supplemental information: RGB is a method to quantify a specific color in vision science.\n R = Red\n G = Green\n B = Blue")

# Parameter passing
# base_of_triangle = int(input("Enter the base of the triangle: "))
# height_of_triangle = int(input("Enter the height of the triangle: "))
# def calculate_area_of_triangle(base, height):
#     area_of_square = base * height
#     area_of_triangle = area_of_square / 2
#     return area_of_triangle
# area_of_triangle = calculate_area_of_triangle(base_of_triangle, height_of_triangle)
# print("Area of triangle = ", area_of_triangle)

# Opening file to save to
file_name = input("Type file name: ")
f = open(file_name + ".csv", "a")
f.write("subject" + ", " + "grapheme" + ", " + "RGB of red trial 1" + ", " + "RGB of red trial 2" + ", " + "RGB of red trial 3" + ", " + "RGB of green trial 1" + ", " + "RGB of green trial 2" + ", " + "RGB of green trial 3" + ", " + "RGB of blue trial 1" + ", " + "RGB of blue trial 2" + ", " + "RGB of blue trial 3" + ", " + "synethesia score")
f.write("\n")
f.close()

# Defining function
def synesthesia_calculator():
    
    # Opening file for function
    f = open(file_name + ".csv", "a")
    
    # Identifying the subject
    sub_id = input("Please enter your initials \nIf you have no middle initial, type x in its place \nThen press enter.\n")

    # Identifying the grapheme
    grapheme = input("Please input the grapheme (letter or number) you wish to assess \nThen press enter.\n")

    # Data entry based on their RGB values from Dr. DiMattina's color chooser
    # I used a while loop instead of an if statement so it looped forever if the individual entered an invalid number
    print("For each of the following inputs: \nType the numerical value (0-255) then press enter.")
    red_1 = int(input("Enter in the R value for trial 1\n"))/255
    while red_1 > 1 or red_1 < 0:      # These lines are personalized error messages and restart the data entry when the value entered does not equal 0-255
        red_1 = int(input("Error: RGB must be between 0 and 255. Please try again.\n"))/255
    red_2 = int(input("Enter in the R value for trial 2\n"))/255
    while red_2 > 1 or red_2 < 0:
        red_2 = int(input("Error: RGB must be between 0 and 255. Please try again.\n"))/255
    red_3 = int(input("Enter in the R value for trial 3\n"))/255
    while red_3 > 1 or red_3 < 0:
        red_3 = int(input("Error: RGB must be between 0 and 255. Please try again.\n"))/255
    green_1 = int(input("Enter in the G value for trial 1\n"))/255
    while green_1 > 1 or green_1 < 0:
        green_1 = int(input("Error: RGB must be between 0 and 255. Please try again.\n"))/255
    green_2 = int(input("Enter in the G value for trial 2\n"))/255
    while green_2 > 1 or green_2 < 0:
        green_2 = int(input("Error: RGB must be between 0 and 255. Please try again.\n"))/255
    green_3 = int(input("Enter in the G value for trial 3\n"))/255
    while green_3 > 1 or green_3 < 0:
        green_3 = int(input("Error: RGB must be between 0 and 255. Please try again.\n"))/255
    blue_1 = int(input("Enter in the B value for trial 1\n"))/255
    while blue_1 > 1 or blue_1 < 0:
        blue_1 = int(input("Error: RGB must be between 0 and 255. Please try again.\n"))/255
    blue_2 = int(input("Enter in the B value for trial 2\n"))/255
    while blue_2 > 1 or blue_2 < 0:
        blue_2 = int(input("Error: RGB must be between 0 and 255. Please try again.\n"))/255
    blue_3 = int(input("Enter in the B value for trial 3\n"))/255
    while blue_3 > 1 or blue_3 < 0:
        blue_3 = int(input("Error: RGB must be between 0 and 255. Please try again.\n"))/255

    # Calculation of Eagleman's synesthetic score (2007)
    variance_red = abs(red_1 - red_2) + abs(red_2 - red_3) + abs(red_3 - red_1)
    variance_green = abs(green_1 - green_2) + abs(green_2 - green_3) + abs(green_3 - green_1)
    variance_blue = abs(blue_1 - blue_2) + abs(blue_2 - blue_3) + abs(blue_3 - blue_1)
    total_variance = variance_red + variance_green + variance_blue

    # Print results
    print("Your synesthetic score: ", total_variance)
    if total_variance <= 1:
        print("You scored within the range of synesthesia!")
    elif total_variance > 1 and total_variance <= 2:
        print("You may have a minimal association, or no association.")
    else:
        print("You do not have a synesthetic association for this grapheme. :(")
    print("Note: A score between 0.0 and 1.0 indicates a synesthetic association. \nA score between 1.0 and 2.0 typically indicates a minimal or no association. \nA score over 2.0 indicates no synesthetic association.")

    # Write to file
    f.write(sub_id + ", " + grapheme + ", " + str(red_1) + ", " + str(red_2) + ", " + str(red_3) + ", " + str(green_1) + ", " + str(green_2) + ", " + str(green_3) + ", " + str(blue_1) + ", " + str(blue_2) + ", " + str(blue_3) + ", " + str(total_variance))
    f.write("\n")
    #f = open(file_name + ".csv", "r") <------ This is just for me to test to make sure it works (same for next line)
    #print(f.read())                     ------^
    
# Function for restart menu (with possibility of looping forever)
def restart_program():
    user_choice = str(input("Do you want to continue?\n"))
    if user_choice == "yes":
        print("This program will be restarted!")
        synesthesia_calculator()
        restart_program()
    elif user_choice == "no":
        print("This program will now close.")
        f.close()
        exit()
    else:
        print("I didn't quite get that. Note: make sure your answer is in lowercase!")
        restart_program()

# Call to functions
synesthesia_calculator()
restart_program()
