# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: UOW - w1811026 , IIT 20201217

# Date:  2020 / 12 / 11

pass_credits = 0
defer_credits = 0
fail_credits = 0

progress = []
trailer = []
retriever = []
exclude = []

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


def histogram(pass_credits, defer_credits):
    if pass_credits == 120:
        progress.append(0)
    elif pass_credits == 100:
        trailer.append(0)
    elif pass_credits == 80:
        retriever.append(0)
    elif pass_credits == 60:
        retriever.append(0)
    elif pass_credits == 40 and defer_credits != 0:
        retriever.append(0)
    elif pass_credits == 40 and defer_credits == 0:
        exclude.append(0)
    elif pass_credits == 20 and defer_credits >= 40:
        retriever.append(0)
    elif pass_credits == 20 and defer_credits <= 20:
        exclude.append(0)
    elif pass_credits == 0 and defer_credits >= 60:
        retriever.append(0)
    elif pass_credits == 0 and defer_credits <= 40:
        exclude.append(0)


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
            histogram(pass_credits, defer_credits)
            break


def histogram_print():
    print("\n")
    print("-" * 60)
    print("Horizontal Histogram\n")
    print("Progress", len(progress), " :", "*" * len(progress))
    print("Trailer", len(trailer), "  :", "*" * len(trailer))
    print("Retriever", len(retriever), ":", "*" * len(retriever))
    print("Excluded", len(exclude), " :", "*" * len(exclude))
    total_outcomes = len(progress) + len(trailer) + len(retriever) + len(exclude)
    print("\n")
    print(total_outcomes, "outcomes in total.")
    print("-" * 60)


close = ""


def run_again():
    global close
    while True:
        print("\n")
        try:
            close = input("Would you like to enter another set of data?\n"
                          "Enter 'y' for yes or 'q' to quit and view results: ")
        except ValueError:
            print("Please Enter 'y' or 'q'")
        else:
            if close == "q":
                histogram_print()
                break

            elif close == "y":
                pass
                break

            else:
                print("Please Enter 'y' or 'q'")

    return close
