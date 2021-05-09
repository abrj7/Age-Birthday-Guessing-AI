import time
from colored import fg 
import sys
import os

color1 = fg("red")
color2 = fg("yellow")
color3 = fg("blue")
color4 = fg("orange_4a")
color5 = fg("sky_blue_2")
color6 = fg("purple_1b")
color7 = fg("dark_violet_1b")
color8 = fg("indian_red_1a")

for x in (f"{color1}Hi.\n\n{color2}In this program, I will try to guess your birthday and/or your age using a math trick.\nYou probably know them both of course, but this program is made just for fun.\n\n"):
	sys.stdout.write(x)
	sys.stdout.flush()
	time.sleep(0.03)

time.sleep(2)

age_list = ['age', 'Age', 'AGE']


# Finding age
while True:
    user_input = input(color4 + "What do you want to find out, your age or your birthday: (age/birthday)\n>>> ")
    while user_input in age_list:
        if user_input == "age" or user_input == "age".upper():
            number_input = input("Pick a number between 1 and 10:\n>>> ")

            num_input_int = int(number_input)

            print(color3 + f"I am going to multiply your number by 2\n{num_input_int * 2}\n")
            math1 = num_input_int * 2

            time.sleep(2)
            print(f"Now, I will add the answer by 5\n{num_input_int * 2 + 5}\n")
            math2 = math1 + 5

            time.sleep(2)
            print(f"Next, I will times the answer by 50\n{(num_input_int *2 + 5) *50}\n")
            math3 = math2 * 50
            
            time.sleep(2)

            birthday_confirm = input("Have you already had your bithday this year? (yes/no)\n>>> ")
            year_born = input("What year were you born?\n>>> ")

            year_born_int = int(year_born)
            break
            #Birthday done
            if birthday_confirm == "yes" or birthday_confirm == "yes".upper():
                print(color5 + f"Beacuse you have had your birthday this year, I will add the answer by 1770\n{((num_input_int *2 + 5) *50) + 1770}\n")
                math4 = math3 + 1770
                time.sleep(2)

                print(f"Finally, I will subtract the number by {year_born_int}, your year of birth.\n")
                final = math4 - year_born_int

                time.sleep(2) 

                for x in (color6 + f"The answer is {final}.\n\nThe first digit in the three/four digit number is the one you picked in the first step.\n\nThe last two digits are your age"):
                    sys.stdout.write(x)
                    sys.stdout.flush()
                    time.sleep(0.03)  

                break
                
            # Birthday not done
            if birthday_confirm == "no" or birthday_confirm == "no".upper():
                print(color5 + f"Beacuse you have not had your birthday this year, I will add the answer by 1769\n{((num_input_int *2 + 5) *50) + 1769}\n")
                math4 = math3 + 1769
                time.sleep(2)

                print(f"Finally, I will subtract the number by {year_born_int}, your year of birth.\n")
                final = math4 - year_born_int

                time.sleep(2)


                for x in (color6 + f"The answer is {final}.\n\nThe first digit in the three/four digit number is the one you picked in the first step.\n\nThe last two digits is your age"):
                    sys.stdout.write(x)
                    sys.stdout.flush()
                    time.sleep(0.03)

            break


# Finding age
if user_input == "birthday" or user_input == "birthday".upper():
    birthday_date = input(color8 + "What date were you born? \n\nFor example if you were born on January 16st thean enter 16\n>>> ")
    birthday_date_int = int(birthday_date)

    print(color3 + f"First I am going time your birthdate by 2\n{birthday_date_int * 2}\n")
    maths1 = birthday_date_int * 2
    time.sleep(2)

    print(f"Now I am going to add 5 to your birthdate\n{maths1 + 5}\n")
    maths2 = maths1 + 5
    time.sleep(2)

    print(f"Next I will times 50 by the answer\n{maths2 * 50}\n")
    maths3 = maths2 * 50
    time.sleep(2)

    month_input = input("What month were you born? Enter the number of that month. For example if you were born in July, enter 7\n>>> ")
    month_input_int = int(month_input)

    time.sleep(2)

    print(f"Now I am going to add the number of month to the answer\n{maths3 + month_input_int}\n")
    maths4 = maths3 + month_input_int

    time.sleep(2)

    print(f"Finally, I am going to subtract 250 from the answer\n{maths4 - 250}\n\n\n")
    final_birthday = maths4 - 250

    for x in (color6 + f"The answer is {final_birthday}.\n\nThe first one/two digits in the three/four digit number is/are the date of you birthday\n\nThe last two digits are the month of your birthday"):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.03)
