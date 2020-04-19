"""
My Integration Project for COP-1500 at Florida Gulf Coast University
"""

__author__ = "Emily Martin"


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


def main():
    """
    The main function of my project.

    The purpose is to calculate a
    participant's 'synesthesia score' for one grapheme based off of Eagleman's
    classification (2007) after asking a few questions about the participant
    and the chosen RGB values, then exporting the data to an excel file, with
    the option of looping the function.

    Grapheme - letter or number
    RGB values - entered in on 0-255 scale, but converted into 0-1 scale for
    the final score
    """
    # Greeting
    print("Hello! This program will evaluate whether or not you have \na "
          "synesthetic association for a grapheme.")

    # These next 4 sections are bonus to satisfy the class requirements

    # String operator
    print("(This next line is to satisfy a class requirement)")
    a = "This program is useful for my research! "
    b = "Hopefully Dr. DiMattina agrees."
    c = a + b
    print(c)

    # Shortcut operator
    # num_1 = 7
    # num_1 += 8
    # print(num_1)

    # For loop
    for x in range(1):
        print(
            "Supplemental information: RGB is a method to quantify a "
            "specific color in vision science.\n R = Red\n G = Green\n B = "
            "Blue")

    # Parameter passing for class requirement
    # base_of_triangle = int(input("Enter the base of the triangle: "))
    # height_of_triangle = int(input("Enter the height of the triangle: "))
    # def calculate_area_of_triangle(base, height):
    #     area_of_square = base * height
    #     area_of_triangle = area_of_square / 2
    #     return area_of_triangle
    # area_of_triangle = calculate_area_of_triangle(base_of_triangle,
    # height_of_triangle)
    # print("Area of triangle = ", area_of_triangle)

    # Opening file to save to
    def creating_file():
        """
        Creates or opens an existing excel file in .csv format. If new
        file, this function adds titles to the excel columns

        User chooses the name of the file, which is saved under the variable
        file_name

        f - file itself
        file_name - chosen name of file without '.csv'
        """
        file_answer = input(
            "Do you want to...\n 1. Add to an existing file? or\n 2. "
            "Overwrite/create a new file?\n Type either 1 or 2.\n")
        if file_answer == "1":
            file_name = input("Type file name: ")
            f = open(file_name + ".csv", "a")
            f.close()
            return file_name
        elif file_answer == "2":
            file_name = input("Type file name: ")
            f = open(file_name + ".csv", "w")
            f.write("subject" + ", " + "grapheme" + ", " + "RGB of red trial 1"
                    + ", " + "RGB of red trial 2" + ", " + "RGB of red trial 3"
                    + ", " + "RGB of green trial 1" + ", " + "RGB of green "
                    "trial 2" + ", " + "RGB of green trial 3" + ", " + "RGB "
                    "of blue trial 1" + ", " + "RGB of blue trial 2" + ", " +
                    "RGB of blue trial 3" + ", " + "synethesia score")
            f.write("\n")
            f.close()
            return file_name
        else:
            print("Error. Please type either 1 or 2 for your choice.")
            creating_file()

    # Call to creating file function, with returned file name saved as a
    # variable so we can access the name in future functions
    chosen_file = creating_file()

    # Defining function
    def synesthesia_calculator():
        """
        The calculator of the project. This function opens the created
        file again, identifies the subject and grapheme, prompts the user to
        enter in the RGB values, calculates the synesthesia score, prints
        out message to user about the score & saves data to the opened excel
        file
        """

        # Opening file for function
        f = open(chosen_file + ".csv", "a")

        # Identifying the subject
        sub_id = input(
            "Please enter your initials \nIf you have no middle initial, "
            "type x in its place \nThen press enter.\n")

        # Identifying the grapheme
        grapheme = input("Please input the grapheme (letter or number) you "
                         "wish to assess \nThen press enter.\n")

        # Data entry based on their RGB values from Dr. DiMattina's color
        # chooser
        # I used a while loop instead of an if statement so it looped
        # forever if the individual entered an invalid number
        print("For each of the following inputs: \nType the numerical value "
              "(0-255) then press enter.")
        red_1 = int(input("Enter in the R value for trial 1\n")) / 255
        while red_1 > 1 or red_1 < 0:
            # These lines are personalized error messages and restart the
            # data entry when the value entered does not equal 0-255
            red_1 = int(input("Error: RGB must be between 0 and 255. Please "
                              "try again.\n")) / 255
        red_2 = int(input("Enter in the R value for trial 2\n")) / 255
        while red_2 > 1 or red_2 < 0:
            red_2 = int(input("Error: RGB must be between 0 and 255. Please "
                              "try again.\n")) / 255
        red_3 = int(input("Enter in the R value for trial 3\n")) / 255
        while red_3 > 1 or red_3 < 0:
            red_3 = int(input("Error: RGB must be between 0 and 255. Please "
                              "try again.\n")) / 255
        green_1 = int(input("Enter in the G value for trial 1\n")) / 255
        while green_1 > 1 or green_1 < 0:
            green_1 = int(input("Error: RGB must be between 0 and 255. "
                                "Please try again.\n")) / 255
        green_2 = int(input("Enter in the G value for trial 2\n")) / 255
        while green_2 > 1 or green_2 < 0:
            green_2 = int(input("Error: RGB must be between 0 and 255. "
                                "Please try again.\n")) / 255
        green_3 = int(input("Enter in the G value for trial 3\n")) / 255
        while green_3 > 1 or green_3 < 0:
            green_3 = int(input("Error: RGB must be between 0 and 255. "
                                "Please try again.\n")) / 255
        blue_1 = int(input("Enter in the B value for trial 1\n")) / 255
        while blue_1 > 1 or blue_1 < 0:
            blue_1 = int(input("Error: RGB must be between 0 and 255. "
                               "Please try again.\n")) / 255
        blue_2 = int(input("Enter in the B value for trial 2\n")) / 255
        while blue_2 > 1 or blue_2 < 0:
            blue_2 = int(input("Error: RGB must be between 0 and 255. "
                               "Please try again.\n")) / 255
        blue_3 = int(input("Enter in the B value for trial 3\n")) / 255
        while blue_3 > 1 or blue_3 < 0:
            blue_3 = int(input("Error: RGB must be between 0 and 255. "
                               "Please try again.\n")) / 255

        # Calculation of Eagleman's synesthetic score (2007)
        variance_red = (abs(red_1 - red_2) + abs(red_2 - red_3) +
                        abs(red_3 - red_1))
        variance_green = (abs(green_1 - green_2) + abs(green_2 - green_3) +
                          abs(green_3 - green_1))
        variance_blue = (abs(blue_1 - blue_2) + abs(blue_2 - blue_3) +
                         abs(blue_3 - blue_1))
        total_variance = variance_red + variance_green + variance_blue

        # Print results
        print("Your synesthetic score: ", total_variance)
        if total_variance <= 1:
            print("You scored within the range of synesthesia!")
        elif 1 < total_variance <= 2:
            print("You may have a minimal association, or no association.")
        else:
            print("You do not have a synesthetic association for this "
                  "grapheme. :(")
        print(
            "Note: A score between 0.0 and 1.0 indicates a synesthetic "
            "association. \nA score between 1.0 and 2.0 typically indicates "
            "a minimal or no association. \nA score over 2.0 indicates no "
            "synesthetic association.")

        # Write to file
        f.write(sub_id + ", " + grapheme + ", " + str(red_1) + ", " +
                str(red_2) + ", " + str(red_3) + ", " + str(
            green_1) + ", " + str(green_2) + ", " + str(green_3) + ", " +
                str(blue_1) + ", " + str(blue_2) + ", " + str(blue_3) + ", " +
                str(total_variance))
        f.write("\n")
        # These next few lines are commented out because they function as a
        # way to test if the saved file works without opening excel

        # f = open(file_name + ".csv", "r")
        # print(f.read())
        return f

    # Call to the synesthesia score calculation function, with the returned
    # variable f saved as 'excel_file' for future access
    excel_file = synesthesia_calculator()

    # Function for restart menu (with possibility of looping forever)
    def restart_program():
        """
        This function offers an in-program 'menu' for restarting the
        program or ending the program and subsequently closing the file
        """
        user_choice = str(input("Do you want to continue?\n"))
        if user_choice == "yes":
            print("This program will be restarted!")
            synesthesia_calculator()
            restart_program()
        elif user_choice == "no":
            print("This program will now close.")
            excel_file.close()
            exit()
        else:
            print("I didn't quite get that. Note: make sure your answer is "
                  "in lowercase!")
            restart_program()
    # Call to restart program function, the last function to call within main
    restart_program()


# Call to main
main()