# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: UOW - w1811026 , IIT 20201217

# Date:  2020 / 12 / 11

import part1
import part2
import part3
import part4
import part5

menu_open = ""
close = ""


def menu():
    global menu_open, close
    while True:
        print("\n")
        try:
            menu_open = input("Enter '1' to Open Students Version: \n"
                              "Enter '2' to Open Student Version (Validation): \n"
                              "Enter '3' to Open Staff Version with Histogram: \n"
                              "Enter '4' to Open Staff Version with Histogram (Optional Extension): \n"
                              "Enter '5' to Open Alternative Staff Version (Optional Extension): \n"
                              "Enter 'q' to Quit: ")
        except ValueError:
            print("Please Enter '1' '2' '3' '4' '5' or 'q'")
        else:
            if menu_open == "q":
                print("'q' Pressed, Quit Programme")
                quit()
            elif menu_open == "1":
                print("-" * 60)
                print("Student Version\n")
                pass_credits = int(input("Please enter your credits at pass: "))
                defer_credits = int(input("Please enter your credits at defer: "))
                fail_credits = int(input("Please enter your credits at fail: "))
                part1.progress_outcome(pass_credits, defer_credits)
                print("-" * 60)
            elif menu_open == "2":
                print("-" * 60)
                print("Student Version (Validation)\n")
                part2.validation()
                print("-" * 60)
            elif menu_open == "3":
                print("-" * 60)
                print("Staff Version with Histogram\n")

                while True:
                    part3.validation()
                    close = part3.run_again()

                    if close == 'q':
                        break

                print("-" * 60)
            elif menu_open == "4":
                print("-" * 60)
                print("Staff Version with Histogram (Optional Extension)\n")

                while True:
                    part4.validation()
                    close = part4.run_again()

                    if close == 'q':
                        break

                print("-" * 60)
            elif menu_open == "5":
                data = [[120, 0, 0], [100, 20, 20], [100, 0, 20], [80, 20, 20], [60, 40, 20],
                        [40, 40, 40], [20, 40, 60], [20, 20, 80], [20, 0, 100], [0, 0, 120]]
                print("-" * 60)
                print("Alternative Staff Version (Optional Extension)\n")

                part5.validation(data)
                part5.histogram_print()

                print("-" * 60)
            else:
                print("Please Enter '1' '2' '3' '4' '5' or 'q'")


menu()
