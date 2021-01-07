# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: UOW - w1811026 , IIT 20201217

# Date:  2020 / 12 / 11

pass_credits = 0
defer_credits = 0
fail_credits = 0

numbers = [0, 20, 40, 60, 80, 100, 120]


def progress_outcome(pass_credits, defer_credits):
    if pass_credits == 120:
        print("Progress")
    elif pass_credits == 100:
        print("Progress (module trailer)")
    elif pass_credits == 80:
        print("Do not Progress - module retriever")
    elif pass_credits == 60:
        print("Do not Progress - module retriever")
    elif pass_credits == 40 and defer_credits != 0:
        print("Do not Progress - module retriever")
    elif pass_credits == 40 and defer_credits == 0:
        print("Exclude")
    elif pass_credits == 20 and defer_credits >= 40:
        print("Do not Progress - module retriever")
    elif pass_credits == 20 and defer_credits <= 20:
        print("Exclude")
    elif pass_credits == 0 and defer_credits >= 60:
        print("Do not Progress - module retriever")
    elif pass_credits == 0 and defer_credits <= 40:
        print("Exclude")


def validation():
    global pass_credits, defer_credits, fail_credits
    while True:
        try:
            pass_credits = int(input("Please enter your credits at pass: "))
        except ValueError:
            print("Integer required")
            continue
        else:
            if pass_credits not in numbers:
                print("Out of range")
            elif pass_credits in numbers:
                break

    while True:
        try:
            defer_credits = int(input("Please enter your credits at defer: "))
        except ValueError:
            print("Integer required")
            continue
        else:
            if defer_credits not in numbers:
                print("Out of range")
            elif defer_credits in numbers:
                break

    while True:
        try:
            fail_credits = int(input("Please enter your credits at fail: "))
        except ValueError:
            print("Integer required")
            continue
        else:
            if fail_credits not in numbers:
                print("Out of range")
            elif fail_credits in numbers:
                break

    while True:
        total_credits = pass_credits + defer_credits + fail_credits
        if total_credits != 120:
            print("Total incorrect")
            validation()
            break
        else:
            progress_outcome(pass_credits, defer_credits)
            break

