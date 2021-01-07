# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: UOW - w1811026 , IIT 20201217

# Date:  2020 / 12 / 11

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



